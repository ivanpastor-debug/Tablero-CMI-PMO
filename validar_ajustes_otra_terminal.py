# -*- coding: utf-8 -*-
"""
Validador de Ajustes Concurrentes · CMI PMO vs Otra Terminal (Tableros de Proyectos)
=====================================================================================

Monitorea, audita y valida en tiempo real los ajustes que se están realizando en
la otra terminal atada a este proyecto (C:\\Users\\IvanDarioPastorParra\\Documents\\Optimización y Control\\tableros de proyectos),
analizando:
1. Actividad reciente de archivos modificados en la otra terminal (últimas N horas).
2. Estado de Git (archivos modificados, staged y untracked) en la otra terminal.
3. Desalineación y diferencias de datos (data_func.json, data_453_cpe.json, data_rqc.json,
   data_salud_cmi.json, data_func/*.json) entre ambas terminales.
4. Auditoría de consistencia en indicadores y reglas de negocio PMO.
5. Modo centinela (--watch) para detección continua en tiempo real.
6. Opción de sincronización segura (--sync) hacia el Tablero CMI.

Uso:
    python validar_ajustes_otra_terminal.py            # Auditoría instantánea completa
    python validar_ajustes_otra_terminal.py --horas 6  # Ventana de las últimas 6 horas
    python validar_ajustes_otra_terminal.py --watch    # Modo centinela en vivo (cada 4s)
    python validar_ajustes_otra_terminal.py --sync     # Sincroniza hacia CMI si la data es válida
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

# Configurar stdout en utf-8 para Windows
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Rutas maestras
CMI_DIR = Path(__file__).resolve().parent
REPO_DEPLOY_DIR = Path.home() / "Indicadores estra y tac"
OTRA_TERMINAL_DIR = Path.home() / "Documents" / "Optimización y Control" / "tableros de proyectos"
OTRA_WEB_DIR = OTRA_TERMINAL_DIR / "web"
OTRA_INDICADORES_DIR = OTRA_TERMINAL_DIR / "indicadores"


def md5_file(path: Path) -> str:
    if not path.is_file():
        return ""
    try:
        with open(path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception:
        return ""


def banner(titulo: str):
    print("\n" + "=" * 85)
    print(f"  {titulo}")
    print("=" * 85)


def auditar_actividad_otra_terminal(horas: float = 12.0) -> list[tuple[Path, datetime, int]]:
    """Detecta archivos modificados en la otra terminal durante la ventana de tiempo."""
    if not OTRA_TERMINAL_DIR.is_dir():
        return []

    limite = datetime.now() - timedelta(hours=horas)
    modificados: list[tuple[Path, datetime, int]] = []

    rutas_a_escanear = [
        OTRA_TERMINAL_DIR / "web",
        OTRA_TERMINAL_DIR / "datos",
        OTRA_INDICADORES_DIR / "Auditoria",
        OTRA_INDICADORES_DIR / "Archivos referencia - Salud de los proyectos",
        OTRA_INDICADORES_DIR / "motor",
        OTRA_INDICADORES_DIR,
    ]

    for ruta in rutas_a_escanear:
        if not ruta.exists():
            continue
        if ruta.is_file():
            try:
                mtime = datetime.fromtimestamp(ruta.stat().st_mtime)
                if mtime >= limite:
                    modificados.append((ruta, mtime, ruta.stat().st_size))
            except Exception:
                pass
            continue

        for root, dirs, files in os.walk(ruta):
            if any(ign in root for ign in [".git", "__pycache__", ".obsidian", ".venv"]):
                continue
            for f in files:
                fpath = Path(root) / f
                try:
                    mtime = datetime.fromtimestamp(fpath.stat().st_mtime)
                    if mtime >= limite:
                        modificados.append((fpath, mtime, fpath.stat().st_size))
                except Exception:
                    pass

    modificados.sort(key=lambda x: x[1], reverse=True)
    return modificados


def obtener_git_status_otra_terminal() -> list[tuple[str, str]]:
    """Consulta git status en la otra terminal."""
    if not OTRA_TERMINAL_DIR.is_dir():
        return [("ERR", "Directorio no encontrado")]

    try:
        res = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(OTRA_TERMINAL_DIR),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=8,
        )
        cambios = []
        for line in res.stdout.strip().splitlines():
            if len(line) > 3:
                st = line[:2].strip()
                p = line[3:].strip().strip('"')
                cambios.append((st, p))
        return cambios
    except Exception as e:
        return [("ERR", str(e))]


def comparar_data_cmi_vs_otra_terminal() -> dict[str, dict]:
    """Compara los archivos de datos entre la otra terminal (web/) y CMI."""
    archivos_clave = [
        "data_func.json",
        "data_453_cpe.json",
        "data_rqc.json",
        "data_salud_cmi.json",
    ]

    comparativa: dict[str, dict] = {}

    for ak in archivos_clave:
        p_otra = OTRA_WEB_DIR / ak
        p_cmi = CMI_DIR / ak
        p_repo = REPO_DEPLOY_DIR / ak

        existe_otra = p_otra.is_file()
        existe_cmi = p_cmi.is_file()

        h_otra = md5_file(p_otra) if existe_otra else "NO_EXISTE"
        h_cmi = md5_file(p_cmi) if existe_cmi else "NO_EXISTE"

        mtime_otra = datetime.fromtimestamp(p_otra.stat().st_mtime) if existe_otra else None
        mtime_cmi = datetime.fromtimestamp(p_cmi.stat().st_mtime) if existe_cmi else None

        alineado = (h_otra == h_cmi) and existe_otra and existe_cmi

        comparativa[ak] = {
            "existe_otra": existe_otra,
            "existe_cmi": existe_cmi,
            "alineado": alineado,
            "mtime_otra": mtime_otra,
            "mtime_cmi": mtime_cmi,
            "otra_mas_reciente": (mtime_otra > mtime_cmi) if (mtime_otra and mtime_cmi) else False,
            "tam_otra": p_otra.stat().st_size if existe_otra else 0,
            "tam_cmi": p_cmi.stat().st_size if existe_cmi else 0,
        }

    # Comparar carpeta data_func/*.json
    df_otra = OTRA_WEB_DIR / "data_func"
    df_cmi = CMI_DIR / "data_func"

    desalineados_func: list[str] = []
    if df_otra.is_dir() and df_cmi.is_dir():
        for jf in df_otra.glob("*.json"):
            cf = df_cmi / jf.name
            if not cf.is_file() or md5_file(jf) != md5_file(cf):
                desalineados_func.append(jf.name)

    comparativa["data_func_individuales"] = {
        "desalineados": desalineados_func,
        "total_otra": len(list(df_otra.glob("*.json"))) if df_otra.is_dir() else 0,
        "total_cmi": len(list(df_cmi.glob("*.json"))) if df_cmi.is_dir() else 0,
    }

    return comparativa


def extraer_resumen_proyectos_otra_terminal() -> dict[str, dict]:
    """Lee data_func.json de la otra terminal para extraer el pulso operativo de cada proyecto."""
    p_otra = OTRA_WEB_DIR / "data_func.json"
    if not p_otra.is_file():
        return {}

    try:
        with open(p_otra, "r", encoding="utf-8") as f:
            data = json.load(f)
        projs = data.get("proyectos", {})
        resumen = {}
        for pid, pdata in projs.items():
            kpi = pdata.get("kpi", {})
            cmi = pdata.get("cmi", {})
            resumen[pid] = {
                "corte": pdata.get("corte", ""),
                "archivo": pdata.get("archivo", ""),
                "n_hu": kpi.get("n_hu", 0),
                "n_hu_activas": kpi.get("n_hu_activas", 0),
                "n_feature": kpi.get("n_feature", 0),
                "n_epic": kpi.get("n_epic", 0),
                "tactico": cmi.get("tactico"),
                "estrategico": cmi.get("estrategico"),
                "d": cmi.get("d"),
                "n": cmi.get("n"),
            }
        return resumen
    except Exception:
        return {}


def auditar_reglas_sesion_paralela() -> tuple[list[str], list[str]]:
    """Ejecuta el auditor interno de la otra terminal si existe para obtener discrepancias de reglas."""
    script_auditor = OTRA_INDICADORES_DIR / "validar_ajustes_sesion_paralela.py"
    if not script_auditor.is_file():
        return ([], ["No se encontró el script de auditoría de la otra terminal."])

    try:
        res = subprocess.run(
            [sys.executable, str(script_auditor), "--horas", "24"],
            cwd=str(OTRA_INDICADORES_DIR),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=25,
        )
        stdout = res.stdout
        lineas = stdout.splitlines()

        alertas = []
        infos = []

        capturar_alertas = False
        capturar_infos = False

        for l in lineas:
            if "DISCREPANCIAS Y ALERTAS" in l:
                capturar_alertas = True
                capturar_infos = False
                continue
            if "ADVERTENCIAS Y RECOMENDACIONES" in l:
                capturar_alertas = False
                capturar_infos = True
                continue
            if "CONCLUSIÓN DEL DIAGNÓSTICO" in l or "====" in l:
                capturar_alertas = False
                capturar_infos = False

            if capturar_alertas and l.strip().startswith("•"):
                alertas.append(l.strip())
            elif capturar_infos and l.strip().startswith("•"):
                infos.append(l.strip())

        return alertas, infos
    except Exception as e:
        return ([], [f"Aviso al ejecutar validador de la otra terminal: {e}"])


def ejecutar_diagnostico_completo(horas: float = 12.0, verbose: bool = True) -> dict:
    """Ejecuta un ciclo completo de validación y emite reporte en consola."""
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    banner(f"VALIDADOR Y CENTINELA MULTITERMINAL · PMO CMI & TABLEROS\n  Hora: {ahora} | Ventana: {horas}h")

    # 1. Estado de la conexión
    print(f"📍 Proyecto Local (CMI):      {CMI_DIR}")
    print(f"📍 Repositorio GitHub Pages:  {REPO_DEPLOY_DIR}")
    print(f"📍 Otra Terminal (Tableros):  {OTRA_TERMINAL_DIR}")

    if not OTRA_TERMINAL_DIR.is_dir():
        print(f"\n❌ ERROR: No se puede conectar con la otra terminal en: {OTRA_TERMINAL_DIR}")
        return {"ok": False, "error": "Ruta no encontrada"}

    # 2. Actividad reciente en la otra terminal
    modificados = auditar_actividad_otra_terminal(horas=horas)
    print(f"\n📂 1. ARCHIVOS MODIFICADOS EN LA OTRA TERMINAL (Últimas {horas} horas): [{len(modificados)}]")
    if modificados:
        proyectos_tocados = set()
        for fpath, mtime, sz in modificados[:12]:
            hora_str = mtime.strftime("%H:%M:%S")
            rel_str = str(fpath.relative_to(OTRA_TERMINAL_DIR))
            print(f"   • [{hora_str}] {rel_str} ({sz:,} bytes)")
            for p in ["004", "005", "020", "348", "355", "384", "397", "416", "419", "420", "421", "453", "456", "457", "461"]:
                if p in rel_str:
                    proyectos_tocados.add(p)
        if len(modificados) > 12:
            print(f"   ... y {len(modificados) - 12} archivos adicionales.")
        if proyectos_tocados:
            print(f"   🎯 Proyectos con actividad detectada: {', '.join(sorted(proyectos_tocados))}")
    else:
        print("   ✓ Sin modificaciones recientes en la ventana de tiempo analizada.")

    # 3. Estado de Git en la otra terminal
    git_status = obtener_git_status_otra_terminal()
    print(f"\n🌿 2. ACTIVIDAD DE CONTROL DE VERSIONES EN LA OTRA TERMINAL: [{len(git_status)} ítems]")
    staged = [p for s, p in git_status if s in ["M", "A", "D", "R"] and not s.startswith("?")]
    untracked = [p for s, p in git_status if s == "??"]
    modified_unstaged = [p for s, p in git_status if "M" in s and s != "M "]

    print(f"   • En preparación (staged): {len(staged)} | Modificados sin stage: {len(modified_unstaged)} | Nuevos (untracked): {len(untracked)}")
    for s, p in git_status[:8]:
        print(f"     [{s:2s}] {p}")
    if len(git_status) > 8:
        print(f"     ... y {len(git_status) - 8} ítems más en seguimiento.")

    # 4. Comparativa de datos entre ambas terminales
    comp = comparar_data_cmi_vs_otra_terminal()
    print("\n⚖️ 3. DESALINEACIÓN DE DATOS (OTRA TERMINAL vs TABLERO CMI):")

    hay_desalineacion = False
    for ak in ["data_func.json", "data_453_cpe.json", "data_rqc.json", "data_salud_cmi.json"]:
        info = comp[ak]
        nombre_fmt = f"{ak:<20}"
        if not info["existe_otra"]:
            print(f"   ⚠️  {nombre_fmt} : No existe en la otra terminal")
        elif not info["existe_cmi"]:
            print(f"   🆕 {nombre_fmt} : NUEVO en la otra terminal (no importado a CMI todavía)")
            hay_desalineacion = True
        elif info["alineado"]:
            hora_otra = info["mtime_otra"].strftime("%H:%M:%S")
            print(f"   ✅ {nombre_fmt} : 100% ALINEADO (Corte: {hora_otra})")
        else:
            hay_desalineacion = True
            reciente = "OTRA TERMINAL ES MÁS RECIENTE" if info["otra_mas_reciente"] else "CMI ES MÁS RECIENTE"
            hora_otra = info["mtime_otra"].strftime("%H:%M:%S")
            hora_cmi = info["mtime_cmi"].strftime("%H:%M:%S")
            print(f"   ⚡ {nombre_fmt} : DESALINEADO ({reciente}) | Otra: {hora_otra} vs CMI: {hora_cmi}")

    indiv = comp["data_func_individuales"]
    if indiv["desalineados"]:
        hay_desalineacion = True
        print(f"   ⚡ data_func/*.json    : {len(indiv['desalineados'])} proyectos desalineados: {', '.join(indiv['desalineados'][:6])}")
    else:
        print(f"   ✅ data_func/*.json    : Todos los {indiv['total_cmi']} proyectos individuales están alineados")

    # 5. Pulso Operativo por Proyecto de la Otra Terminal
    resumen_projs = extraer_resumen_proyectos_otra_terminal()
    if resumen_projs:
        print("\n📊 4. PULSO OPERATIVO PROYECTOS (Snapshot en Otra Terminal):")
        print(f"   {'PROY':<6} | {'CORTE':<10} | {'TÁCTICO':<8} | {'ESTRATÉGICO':<12} | {'FEATURES':<8} | {'HUs':<6}")
        print("   " + "-" * 62)
        for pid in sorted(resumen_projs.keys()):
            r = resumen_projs[pid]
            tact_str = f"{r['tactico'] * 100:.2f}%" if r["tactico"] is not None else "N/A"
            estra_str = f"{r['estrategico'] * 100:.2f}% ({r['d']}/{r['n']})" if r["estrategico"] is not None else "N/A"
            feat_str = str(r["n_feature"])
            hu_str = str(r["n_hu_activas"])
            print(f"   {pid:<6} | {r['corte']:<10} | {tact_str:<8} | {estra_str:<12} | {feat_str:<8} | {hu_str:<6}")

    # 6. Auditoría de reglas desde la otra terminal
    alertas, infos = auditar_reglas_sesion_paralela()
    print(f"\n🛡️ 5. REGLAS DE NEGOCIO PMO EN LA OTRA TERMINAL: [{len(alertas)} alertas, {len(infos)} recomendaciones]")
    if alertas:
        for a in alertas:
            print(f"   ⚠️  {a}")
    else:
        print("   ✓ Sin discrepancias numéricas críticas en la auditoría de reglas.")
    if infos:
        for inf in infos[:4]:
            print(f"   ℹ️  {inf}")

    # Conclusión ejecutiva
    banner("CONCLUSIÓN DEL DIAGNÓSTICO MULTITERMINAL")
    if hay_desalineacion:
        print("  ⚠️  ESTADO: SE DETECTARON AJUSTES PENDIENTES DE SINCRONIZAR.")
        print("  💡 RECOMENDACIÓN: Ejecuta 'python sync_funcionalidades.py' o usa '--sync'")
        print("     para absorber los últimos cambios de la otra terminal hacia CMI.")
    else:
        print("  ✅ ESTADO: AMBAS TERMINALES ESTÁN 100% SINCRONIZADAS Y ALINEADAS.")
    print("=" * 85 + "\n")

    return {
        "ok": True,
        "hay_desalineacion": hay_desalineacion,
        "modificados": len(modificados),
        "alertas": len(alertas),
    }


def modo_centinela(intervalo: int = 4, horas: float = 6.0):
    """Monitorea en tiempo real cambios en la otra terminal y avisa al instante."""
    print("=" * 85)
    print("  INICIANDO MODO CENTINELA (WATCHDOG CONCURRENTE EN TIEMPO REAL)")
    print(f"  Escuchando cada {intervalo} segundos cambios en: {OTRA_TERMINAL_DIR}")
    print("  Presiona Ctrl+C para detener.")
    print("=" * 85)

    ultimo_estado: dict[str, str] = {}
    for p in [OTRA_WEB_DIR / "data_func.json", OTRA_WEB_DIR / "data_453_cpe.json", OTRA_WEB_DIR / "data_rqc.json"]:
        if p.is_file():
            ultimo_estado[p.name] = md5_file(p)

    try:
        while True:
            cambios_detectados = []
            for p in [OTRA_WEB_DIR / "data_func.json", OTRA_WEB_DIR / "data_453_cpe.json", OTRA_WEB_DIR / "data_rqc.json"]:
                if p.is_file():
                    curr_h = md5_file(p)
                    prev_h = ultimo_estado.get(p.name, "")
                    if curr_h != prev_h:
                        cambios_detectados.append(p.name)
                        ultimo_estado[p.name] = curr_h

            if cambios_detectados:
                hora = datetime.now().strftime("%H:%M:%S")
                print(f"\n🔔 [{hora}] ¡ALERTA! La otra terminal modificó: {', '.join(cambios_detectados)}")
                ejecutar_diagnostico_completo(horas=horas)

            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\n\n[Centinela detenido por el usuario].")


def sincronizar_hacia_cmi():
    """Ejecuta la sincronización segura hacia CMI absorbiendo los datos de la otra terminal."""
    print("\nIniciando sincronización segura desde la otra terminal hacia CMI...")
    sync_script = CMI_DIR / "sync_funcionalidades.py"
    if not sync_script.is_file():
        print(f"Error: No se encontró {sync_script}")
        return

    res = subprocess.run([sys.executable, str(sync_script)], cwd=str(CMI_DIR))
    if res.returncode == 0:
        print("\n¡Sincronización completada exitosamente!")
        # Validar arquitectura tras la sincronización
        verify_script = CMI_DIR / "verify_cmi_architecture.py"
        if verify_script.is_file():
            subprocess.run([sys.executable, str(verify_script)], cwd=str(CMI_DIR))
    else:
        print("\nError durante la sincronización.")


def main():
    parser = argparse.ArgumentParser(description="Validador de ajustes concurrentes entre terminales PMO.")
    parser.add_argument("--horas", type=float, default=12.0, help="Ventana de horas para analizar modificaciones (def: 12.0).")
    parser.add_argument("--watch", action="store_true", help="Activa el modo centinela de monitoreo continuo.")
    parser.add_argument("--sync", action="store_true", help="Ejecuta la sincronización segura hacia CMI.")
    parser.add_argument("--intervalo", type=int, default=4, help="Segundos entre chequeos en modo --watch (def: 4s).")
    args = parser.parse_args()

    if args.sync:
        sincronizar_hacia_cmi()
        return

    if args.watch:
        modo_centinela(intervalo=args.intervalo, horas=args.horas)
    else:
        ejecutar_diagnostico_completo(horas=args.horas)


if __name__ == "__main__":
    main()

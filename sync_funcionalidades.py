"""
Script de sincronización de datos de funcionalidades desde el repositorio Tableros
hacia el Tablero CMI PMO.
"""
import glob
import json
import os
import shutil
import subprocess
from pathlib import Path


def pull_latest_source(src_web):
    """Realiza git pull en el repositorio origen Tableros para traer el último corte diario."""
    repo_root = os.path.dirname(src_web)
    git_dir = os.path.join(repo_root, ".git")
    if not os.path.exists(git_dir):
        return
    home = str(Path.home())
    git_exe = os.path.join(home, "AppData", "Local", "Programs", "Git", "cmd", "git.exe")
    git_cmd = git_exe if os.path.exists(git_exe) else "git"
    try:
        print(f"Actualizando repositorio fuente ({repo_root}) desde GitHub...")
        subprocess.run([git_cmd, "-C", repo_root, "pull", "--ff-only", "origin", "main"], check=False)
    except Exception as e:
        print(f"Aviso git pull en Tableros: {e}")


def build_consolidated_419(target_dir):
    """Genera data_func/419.json en target_dir combinando 419-DEP.json y 419-RAMA.json del corte vigente."""
    df_dir = os.path.join(target_dir, "data_func")
    dep_path = os.path.join(df_dir, "419-DEP.json")
    rama_path = os.path.join(df_dir, "419-RAMA.json")
    out_path = os.path.join(df_dir, "419.json")
    idx_path = os.path.join(target_dir, "data_func.json")

    if not (os.path.exists(dep_path) and os.path.exists(rama_path)):
        return

    with open(dep_path, "r", encoding="utf-8") as f:
        dep = json.load(f)
    with open(rama_path, "r", encoding="utf-8") as f:
        rama = json.load(f)

    epics = (dep.get("epics") or []) + (rama.get("epics") or [])
    features = (dep.get("features") or []) + (rama.get("features") or [])
    hus = (dep.get("hus") or []) + (rama.get("hus") or [])

    kd = dep.get("kpi") or {}
    kr = rama.get("kpi") or {}

    n_hu = (kd.get("n_hu") or 0) + (kr.get("n_hu") or 0)
    n_hu_act = (kd.get("n_hu_activas") or 0) + (kr.get("n_hu_activas") or 0)
    pct_glob = (
        ((kd.get("n_hu_activas") or 0) * (kd.get("pct_global") or 0.0)
         + (kr.get("n_hu_activas") or 0) * (kr.get("pct_global") or 0.0))
        / n_hu_act
        if n_hu_act
        else 0.0
    )

    kpi_419 = {
        "n_hu": n_hu,
        "n_hu_activas": n_hu_act,
        "hu_sin_feature": (kd.get("hu_sin_feature") or 0) + (kr.get("hu_sin_feature") or 0),
        "n_feature": (kd.get("n_feature") or 0) + (kr.get("n_feature") or 0),
        "n_epic": (kd.get("n_epic") or 0) + (kr.get("n_epic") or 0),
        "n_feature_con_hu": (kd.get("n_feature_con_hu") or 0) + (kr.get("n_feature_con_hu") or 0),
        "feature_sin_hu": (kd.get("feature_sin_hu") or 0) + (kr.get("feature_sin_hu") or 0),
        "hu_omitidas": (kd.get("hu_omitidas") or 0) + (kr.get("hu_omitidas") or 0),
        "pct_global": round(pct_glob, 4),
        "term_global": (kd.get("term_global") or 0) + (kr.get("term_global") or 0),
        "feature_sin_frente": (kd.get("feature_sin_frente") or 0) + (kr.get("feature_sin_frente") or 0),
        "hu_sin_frente": (kd.get("hu_sin_frente") or 0) + (kr.get("hu_sin_frente") or 0),
        "feature_100_sin_cerrar": (kd.get("feature_100_sin_cerrar") or 0) + (kr.get("feature_100_sin_cerrar") or 0),
        "feature_estado_ajeno": (kd.get("feature_estado_ajeno") or 0) + (kr.get("feature_estado_ajeno") or 0),
        "feature_removido_con_hu": (kd.get("feature_removido_con_hu") or 0) + (kr.get("feature_removido_con_hu") or 0),
    }

    corte = max(dep.get("corte") or "", rama.get("corte") or "")
    consolidated = {
        "codigo": "419",
        "corte": corte,
        "generado": dep.get("generado") or rama.get("generado") or "",
        "archivo": f"Consolidado 419 (DEP + RAMA · {corte})",
        "epics": epics,
        "features": features,
        "hus": hus,
        "kpi": kpi_419,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(consolidated, f, ensure_ascii=False, indent=2)

    if os.path.exists(idx_path):
        with open(idx_path, "r", encoding="utf-8") as f:
            idx = json.load(f)
        idx.setdefault("proyectos", {})["419"] = {
            "corte": corte,
            "archivo": f"Consolidado 419 (DEP + RAMA · {corte})",
            "kpi": kpi_419,
        }
        with open(idx_path, "w", encoding="utf-8") as f:
            json.dump(idx, f, ensure_ascii=False, indent=2)


def main():
    home = str(Path.home())
    src_patterns = [
        os.path.join(home, "Documents", "Optimizaci*n y Control", "tableros de proyectos", "web"),
        os.path.join(home, "Documents", "Optimizaci*n y Control", "tableros-front", "web"),
    ]
    src_web = None
    for pat in src_patterns:
        matches = glob.glob(pat)
        if matches and os.path.exists(matches[0]):
            src_web = matches[0]
            break

    if not src_web:
        print("ERROR: No se encontró la carpeta web del repositorio Tableros.")
        return

    pull_latest_source(src_web)

    dest_dirs = [
        os.path.join(home, "Indicadores estra y tac"),
        os.path.join(home, "Documents", "PMO INDICADORES", "CMI"),
        os.path.join(home, "Downloads"),
    ]

    files_to_copy = ["data_func.json", "data_453_cpe.json"]
    dirs_to_copy = ["data_func"]

    print(f"Origen de datos: {src_web}")
    for d in dest_dirs:
        if not os.path.exists(d):
            continue
        print(f"Sincronizando hacia: {d}")
        for f in files_to_copy:
            s = os.path.join(src_web, f)
            target = os.path.join(d, f)
            if os.path.exists(s):
                shutil.copy2(s, target)
                print(f"  -> {f} ({os.path.getsize(target)} bytes)")
        for folder in dirs_to_copy:
            s = os.path.join(src_web, folder)
            target = os.path.join(d, folder)
            if os.path.exists(s):
                if os.path.exists(target):
                    shutil.rmtree(target)
                shutil.copytree(s, target)
                print(f"  -> {folder}/ ({len(os.listdir(target))} archivos)")
        build_consolidated_419(d)

    print("Sincronización completada con éxito.")
    try:
        import enrich_func_cmi
        print("Ejecutando enriquecimiento CMI de indicadores...")
        enrich_func_cmi.main()
    except Exception as e:
        print(f"Aviso: No se pudo ejecutar el enriquecimiento CMI: {e}")


if __name__ == "__main__":
    main()

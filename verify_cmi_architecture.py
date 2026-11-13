# -*- coding: utf-8 -*-
"""
Script de Verificación y Auditoría de Arquitectura del Tablero CMI PMO.

Valida exhaustivamente:
1. Integridad estructural y de regex de Tablero_CMI_PMO.html.
2. Certificación de indicadores tácticos y estratégicos de todos los proyectos.
3. Reglas de negocio y filtros estrictos (348: 20 func, 421: 56 func sin transversales, 419: 466 func, 456: 2 columnas).
4. Integridad de los archivos JSON de Azure DevOps (data_func.json, data_453_cpe.json, data_rqc.json, data_func/*.json).
5. Sincronía exacta entre las 3 visuales (Libre, Master PMO, Vista por Clave) y las 4 rutas espejo maestras.
"""

from __future__ import annotations

import glob
import hashlib
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO_ROOT = Path.home() / "Indicadores estra y tac"
DOWNLOADS = Path.home() / "Downloads"

HTML_PATH = ROOT / "Tablero_CMI_PMO.html"
DATA_FUNC_PATH = ROOT / "data_func.json"
DATA_453_PATH = ROOT / "data_453_cpe.json"
DATA_RQC_PATH = ROOT / "data_rqc.json"


def md5(p: Path) -> str:
    with open(p, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def test_structural_integrity(errors: list[str]):
    print("[1/5] Verificando integridad estructural y sintaxis de Tablero_CMI_PMO.html...")
    if not HTML_PATH.is_file():
        errors.append(f"No existe el archivo maestro: {HTML_PATH}")
        return

    content = HTML_PATH.read_text(encoding="utf-8")

    # 1.1 Verificar FR_PATTERN estricto
    fr_pattern = re.compile(r"const FR=(\{[\s\S]*?\});\s*const BOOK416=")
    fr_match = fr_pattern.search(content)
    if not fr_match:
        errors.append("FALLO CRÍTICO: No se encontró la declaración 'const FR=...; const BOOK416='")
    else:
        try:
            fr_data = json.loads(fr_match.group(1))
            required_keys = ["005", "355", "416", "384", "419", "453", "421", "397", "348", "456", "457", "020", "461"]
            for rk in required_keys:
                if rk not in fr_data:
                    errors.append(f"Falta la clave '{rk}' en const FR")
        except Exception as e:
            errors.append(f"const FR contiene JSON inválido: {e}")

    # 1.2 Verificar presencia de componentes clave
    checks = [
        ('const BOOK416=', "const BOOK416"),
        ('FIN=', "Variable FIN (Financiera)"),
        ('PROJ_CALLOUT_META', "Objeto PROJ_CALLOUT_META"),
        ('BUGS_419_DATA', "Objeto BUGS_419_DATA"),
        ('id="sem-op"', "Contenedor de tarjetas operativas #sem-op"),
        ('updateTopOpTiles', "Función de actualización de tiles operativos updateTopOpTiles"),
        ('id="fncBody"', "Cuerpo del desglose funcional de Azure DevOps #fncBody"),
    ]
    for pattern, name in checks:
        if pattern not in content:
            errors.append(f"Falta componente estructural: {name}")


def test_business_rules(errors: list[str]):
    print("[2/5] Verificando reglas de negocio certificadas por proyecto...")
    if not HTML_PATH.is_file():
        return

    content = HTML_PATH.read_text(encoding="utf-8")

    # 2.1 Proyecto 005 (Positiva SGDEA): 63 funcionalidades, 44 en prod
    if 'Azure · 63 Func.' not in content:
        errors.append("005: El callout no muestra 'Azure · 63 Func.'")
    if '44 en prod.' not in content:
        errors.append("005: El callout no muestra '44 en prod.'")

    # 2.2 Proyecto 348 (SGDEA Acueducto): 20 funcionalidades, 17 en prod, av:0.9085
    if 'Azure · 20 Func.' not in content:
        errors.append("348: El callout no muestra 'Azure · 20 Func.'")
    if 'av:0.9085' not in content:
        errors.append("348: Indicador táctico en P[348].op no está en 0.9085")

    # 2.3 Proyecto 421 (Balú): 56 funcionalidades (excluye transversales y QA), 13 en prod, 74.88%
    if 'Azure · 56 Func.' not in content:
        errors.append("421: El callout no muestra 'Azure · 56 Func.'")
    if 'av:0.7488' not in content:
        errors.append("421: Indicador táctico en P[421].op no está en 0.7488")

    # 2.4 Proyecto 419 (Depósitos Judiciales): 466 funcionalidades locales, 80 en prod, 11.96%
    if 'Local · 466 Func.' not in content:
        errors.append("419: El callout o badge no muestra 'Local · 466 Func.'")
    if 'av:0.1195' not in content and 'av:0.1196' not in content:
        errors.append("419: Indicador táctico en P[419].op no está en ~0.1196")

    # 2.5 Proyecto 456 (Aeronáutica): 2 columnas en ficha operativa
    if 'tbl-crono-456' not in content:
        errors.append("456: No se encontró la clase de tabla cronograma 'tbl-crono-456'")

    # 2.6 Proyecto 397 (Core Andina): 57 épicas, 52 entregadas
    if 'Azure · 57 Épicas' not in content and 'Azure · 57 Epicas' not in content:
        errors.append("397: El callout o badge no muestra 'Azure · 57 Épicas'")


def test_json_pipeline(errors: list[str]):
    print("[3/5] Verificando tubería de datos JSON de Azure DevOps...")

    # data_func.json
    if not DATA_FUNC_PATH.is_file():
        errors.append(f"Falta el archivo principal {DATA_FUNC_PATH}")
    else:
        try:
            with open(DATA_FUNC_PATH, "r", encoding="utf-8") as f:
                df = json.load(f)
            projs = df.get("proyectos", {})
            for p in ["005", "348", "384", "419", "421", "397", "457", "020", "461"]:
                if p not in projs:
                    errors.append(f"data_func.json no incluye metadata para proyecto {p}")
        except Exception as e:
            errors.append(f"data_func.json contiene JSON inválido: {e}")

    # data_func/348.json
    f348 = ROOT / "data_func" / "348.json"
    if f348.is_file():
        try:
            with open(f348, "r", encoding="utf-8") as f:
                d348 = json.load(f)
            n_features = len(d348.get("features", []))
            if n_features != 20:
                errors.append(f"data_func/348.json debe contener exactamente 20 funcionalidades, tiene: {n_features}")
        except Exception as e:
            errors.append(f"data_func/348.json inválido: {e}")

    # data_func/421.json
    f421 = ROOT / "data_func" / "421.json"
    if f421.is_file():
        try:
            with open(f421, "r", encoding="utf-8") as f:
                d421 = json.load(f)
            epics = d421.get("epics", [])
            for e in epics:
                title = str(e.get("t") or "").lower()
                if "transversal" in title or "automatizaci" in title:
                    errors.append(f"data_func/421.json contiene épica que debió ser excluida: '{title}'")
            n_features = len(d421.get("features", []))
            if n_features != 56:
                errors.append(f"data_func/421.json debe contener exactamente 56 funcionalidades, tiene: {n_features}")
        except Exception as e:
            errors.append(f"data_func/421.json inválido: {e}")

    # data_453_cpe.json
    if not DATA_453_PATH.is_file():
        errors.append(f"Falta el archivo CPE {DATA_453_PATH}")
    else:
        try:
            with open(DATA_453_PATH, "r", encoding="utf-8") as f:
                cpe = json.load(f)
            if "focos" not in cpe or "cus" not in cpe:
                errors.append("data_453_cpe.json no contiene estructura válida de focos/cus")
        except Exception as e:
            errors.append(f"data_453_cpe.json inválido: {e}")

    # data_rqc.json
    if not DATA_RQC_PATH.is_file():
        errors.append(f"Falta el archivo RQC {DATA_RQC_PATH}")


def test_three_views_and_mirrors(errors: list[str]):
    print("[4/5] Verificando sincronía de las 3 visuales y rutas espejo...")

    # Archivos maestros en CMI
    master_cmi = ROOT / "master.html"
    consulta_cmi = ROOT / "consulta.html"
    if not master_cmi.is_file():
        errors.append("Falta master.html en el directorio CMI")
    if not consulta_cmi.is_file():
        errors.append("Falta consulta.html en el directorio CMI")

    # Archivos en el repositorio GitHub Pages
    if REPO_ROOT.is_dir():
        index_repo = REPO_ROOT / "index.html"
        tablero_repo = REPO_ROOT / "Tablero_CMI_PMO.html"
        master_repo = REPO_ROOT / "master.html"
        consulta_repo = REPO_ROOT / "consulta.html"

        if not index_repo.is_file():
            errors.append("Falta index.html en el repositorio GitHub Pages")
        elif md5(index_repo) != md5(HTML_PATH):
            errors.append("DESALINEACIÓN: index.html en GitHub Pages no es idéntico a Tablero_CMI_PMO.html")

        if not tablero_repo.is_file():
            errors.append("Falta Tablero_CMI_PMO.html en el repositorio GitHub Pages")
        elif md5(tablero_repo) != md5(HTML_PATH):
            errors.append("DESALINEACIÓN: Tablero_CMI_PMO.html en repo no es idéntico al de CMI")

        if master_cmi.is_file() and master_repo.is_file() and md5(master_cmi) != md5(master_repo):
            errors.append("DESALINEACIÓN: master.html en repo no es idéntico al de CMI")

        if consulta_cmi.is_file() and consulta_repo.is_file() and md5(consulta_cmi) != md5(consulta_repo):
            errors.append("DESALINEACIÓN: consulta.html en repo no es idéntico al de CMI")


def test_repo_cleanliness(errors: list[str]):
    print("[5/5] Verificando limpieza de archivos en workspace y repositorio...")

    # Scratch scripts que no deben estar en la raíz de CMI
    stray_scripts = [
        "check_diff_rf.py", "check_dim.py", "check_mockup_mode.py", "check_modes.py",
        "check_opcards.py", "check_syntax.py", "inspect_020_hus.py", "inspect_348_target_epics.py",
        "show_5_objs.py", "test_run.py", "temp_test.js"
    ]
    for s in stray_scripts:
        if (ROOT / s).is_file():
            errors.append(f"El archivo temporal '{s}' debe estar archivado en 'scratch/'")

    # En el repositorio GitHub Pages no debe haber .pycache ni archivos gitignored huérfanos
    if REPO_ROOT.is_dir():
        pycache = REPO_ROOT / "__pycache__"
        if pycache.is_dir() and any(pycache.iterdir()):
            errors.append("El directorio __pycache__ en el repositorio contiene archivos de caché")


def main() -> int:
    print("=" * 65)
    print("  AUDITORÍA DE ARQUITECTURA E INTEGRIDAD DEL TABLERO CMI PMO")
    print("=" * 65)

    errors: list[str] = []
    test_structural_integrity(errors)
    test_business_rules(errors)
    test_json_pipeline(errors)
    test_three_views_and_mirrors(errors)
    test_repo_cleanliness(errors)

    print("\n" + "=" * 65)
    if errors:
        print(f"  RESULTADO: SE DETECTARON {len(errors)} DESALINEACIONES / ERRORES:")
        print("=" * 65)
        for i, err in enumerate(errors, 1):
            print(f"  {i}. {err}")
        return 1
    else:
        print("  RESULTADO: ARQUITECTURA 100% BLINDADA, LIMPIA Y SIN ERRORES")
        print("=" * 65)
        return 0


if __name__ == "__main__":
    sys.exit(main())

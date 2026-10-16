# -*- coding: utf-8 -*-
"""
Script de Actualización Integral del Tablero CMI PMO.

Alinea en una sola ejecución:
1. Actualización operativa y financiera desde los libros Excel locales (ACTUALIZAR.py).
2. Sincronización de Épicas, Funcionalidades y HUs desde Azure DevOps (sync_funcionalidades.py).
3. Enriquecimiento oficial CMI de las funcionalidades (enrich_func_cmi.py).
4. Sincronización automática de todas las rutas espejo del HTML.
5. Publicación opcional en GitHub Pages (git push).

Uso:
    python actualizar_todo.py
    python actualizar_todo.py --dry-run
    python actualizar_todo.py --push
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT_REPO = Path(r"c:\Users\Usuario1\Indicadores estra y tac")
DOCS_CMI = Path(r"C:\Users\Usuario1\Documents\PMO INDICADORES\CMI")
DOWNLOADS = Path(r"C:\Users\Usuario1\Downloads")

SCRIPT_ACTUALIZAR_PY = DOCS_CMI / "ACTUALIZAR.py"
SCRIPT_SYNC_FUNC = ROOT_REPO / "sync_funcionalidades.py"
HTML_SOURCE = ROOT_REPO / "index.html"
HTML_MASTER_CMI = DOCS_CMI / "Tablero_CMI_PMO.html"

MIRROR_FILES = [
    ROOT_REPO / "index.html",
    ROOT_REPO / "Tablero_CMI_PMO.html",
    DOCS_CMI / "Tablero_CMI_PMO.html",
    DOWNLOADS / "Tablero_CMI_PMO.html",
]


def print_banner(msg: str):
    print("\n" + "=" * 65)
    print(f"  {msg}")
    print("=" * 65)


def run_cmi_update(dry_run: bool = False) -> bool:
    print_banner("1. Actualización de Indicadores CMI y Financieros desde Excel")
    if not SCRIPT_ACTUALIZAR_PY.is_file():
        print(f"ERROR: No se encontró {SCRIPT_ACTUALIZAR_PY}")
        return False

    cmd = [sys.executable, str(SCRIPT_ACTUALIZAR_PY)]
    if dry_run:
        cmd.append("--dry-run")

    res = subprocess.run(cmd, cwd=str(DOCS_CMI))
    return res.returncode == 0


def run_azure_sync(dry_run: bool = False) -> bool:
    print_banner("2. Sincronización de Épicas y Funcionalidades desde Azure DevOps")
    if dry_run:
        print("[Dry-run] Se omitió la copia de archivos de Azure DevOps.")
        return True

    if not SCRIPT_SYNC_FUNC.is_file():
        print(f"ERROR: No se encontró {SCRIPT_SYNC_FUNC}")
        return False

    res = subprocess.run([sys.executable, str(SCRIPT_SYNC_FUNC)], cwd=str(ROOT_REPO))
    return res.returncode == 0


def sync_mirrors(dry_run: bool = False) -> bool:
    print_banner("3. Sincronización de Archivos Espejo")
    if dry_run:
        print("[Dry-run] No se copiaron archivos espejo.")
        return True

    src = HTML_SOURCE if HTML_SOURCE.is_file() else HTML_MASTER_CMI
    if not src.is_file():
        print("ERROR: No se encontró el archivo HTML de origen.")
        return False

    print(f"Origen del tablero: {src}")
    for dest in MIRROR_FILES:
        try:
            if dest != src:
                shutil.copy2(src, dest)
                print(f"  -> Sincronizado: {dest}")
            else:
                print(f"  -> (Es el archivo base): {dest}")
        except Exception as e:
            print(f"  Aviso al copiar a {dest}: {e}")
    return True


def git_publish() -> bool:
    print_banner("4. Publicación en Producción (GitHub Pages)")
    try:
        subprocess.run(["git", "add", "."], cwd=str(ROOT_REPO), check=True)
        commit_res = subprocess.run(
            ["git", "commit", "-m", "actualizacion integral CMI y Azure DevOps"],
            cwd=str(ROOT_REPO)
        )
        if commit_res.returncode == 0:
            print("Commit realizado con éxito. Enviando a GitHub Pages...")
        else:
            print("No se detectaron cambios pendientes para commit.")

        push_res = subprocess.run(["git", "push", "origin", "main"], cwd=str(ROOT_REPO), check=True)
        print("¡Publicación en GitHub Pages completada exitosamente!")
        print("URL en vivo: https://ivanpastor-debug.github.io/Tablero-CMI-PMO/")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error durante git push: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Actualización integral del Tablero CMI PMO.")
    parser.add_argument("--dry-run", action="store_true", help="Valida los cálculos sin modificar archivos.")
    parser.add_argument("--push", action="store_true", help="Publica automáticamente en GitHub Pages.")
    parser.add_argument("--skip-cmi", action="store_true", help="Omite la actualización desde el Excel PMO.")
    parser.add_argument("--skip-azure", action="store_true", help="Omite la sincronización de Azure DevOps.")
    args = parser.parse_args()

    ok = True
    if not args.skip_cmi:
        ok = run_cmi_update(dry_run=args.dry_run) and ok

    if not args.skip_azure:
        ok = run_azure_sync(dry_run=args.dry_run) and ok

    ok = sync_mirrors(dry_run=args.dry_run) and ok

    if args.push and not args.dry_run:
        ok = git_publish() and ok

    print_banner("Resumen del Proceso")
    if ok:
        print("¡Proceso completado exitosamente y todo el tablero quedó alineado!")
    else:
        print("El proceso finalizó con advertencias o errores. Revisa el registro arriba.")


if __name__ == "__main__":
    main()


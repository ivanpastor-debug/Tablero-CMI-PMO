"""Actualiza los indicadores operativos del tablero desde el consolidado PMO."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from datetime import date, datetime
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "Información Operativa consolidada"
HTML_PATH = ROOT / "Tablero_CMI_PMO.html"
FR_PATTERN = re.compile(r"const FR=(\{[\s\S]*?\});\s*const BOOK416=")


def source_date(path: Path) -> date:
    match = re.search(r"(?<!\d)(\d{8})(?!\d)", path.stem)
    if match:
        value = match.group(1)
        try:
            if 1900 <= int(value[:4]) <= 2100:
                return date(int(value[:4]), int(value[4:6]), int(value[6:8]))
            return date(int(value[4:]), int(value[2:4]), int(value[:2]))
        except ValueError as exc:
            raise ValueError(f"Fecha inválida en el nombre del archivo: {path.name}") from exc
    return date.fromtimestamp(path.stat().st_mtime)


def find_latest_source() -> Path:
    candidates = [
        path for path in SOURCE_DIR.glob("Consolidado Indicadores PMO*.xlsx")
        if not path.name.startswith("~$")
    ]
    if not candidates:
        raise FileNotFoundError(f"No hay consolidados PMO en: {SOURCE_DIR}")
    return max(candidates, key=lambda path: (source_date(path), path.stat().st_mtime))


def get_cmi_indicators(sheet, project_code: str) -> tuple[float, float]:
    columns = (3, 9, 15)
    for row in sheet.iter_rows():
        for cell in row:
            value = str(cell.value or "")
            if re.search(rf"(?<!\d){re.escape(project_code)}(?!\d)", value):
                column = cell.column
                if column not in columns:
                    continue
                indicator_row = cell.row + 4
                tactical = sheet.cell(indicator_row, column).value
                strategic = sheet.cell(indicator_row, column + 2).value
                if not isinstance(tactical, (int, float)) or not isinstance(strategic, (int, float)):
                    raise ValueError(f"Indicadores CMI incompletos para el proyecto {project_code}")
                return float(tactical), float(strategic)
    raise ValueError(f"No se encontró el proyecto {project_code} en la hoja CMI")


def get_acueducto_fronts(sheet) -> list[list[object]]:
    fronts: list[list[object]] = []
    for row in sheet.iter_rows(min_row=2, min_col=10, max_col=17, values_only=True):
        label = row[0]
        if not isinstance(label, str):
            continue
        label = label.strip()
        if label.startswith("▾"):
            fronts.append(["§ " + label[1:].strip()])
        elif label.startswith("▸"):
            function_count, hu_count = row[2], row[3]
            count = function_count if isinstance(function_count, (int, float)) else hu_count
            if not isinstance(count, (int, float)):
                continue
            scale = row[7]
            fronts.append([label[1:].strip(), int(count), float(scale) if isinstance(scale, (int, float)) else None])
    if not any(len(front) > 1 for front in fronts):
        raise ValueError("No se encontraron frentes funcionales en la hoja de Acueducto")
    return fronts


def infer_deliverable_counts(strategic: float) -> tuple[int, int]:
    ratio = Fraction(strategic).limit_denominator(500)
    if abs(float(ratio) - strategic) > 0.000001:
        raise ValueError(f"No se puede derivar el conteo de entregables desde {strategic:.8f}")
    return ratio.denominator, ratio.numerator


def replace_project_op(html: str, project_code: str, op: str) -> str:
    pattern = re.compile(
        rf'(\{{id:"{re.escape(project_code)}",[\s\S]*?op:\{{)[^}}]*(\}})'
    )
    updated, count = pattern.subn(lambda match: match.group(1) + op + match.group(2), html, count=1)
    if count != 1:
        raise ValueError(f"No se pudo localizar el objeto operativo del proyecto {project_code}")
    return updated


def get_419_tactical_without_internal(workbook, fallback_tactical: float) -> float:
    sheet_419 = next(
        (workbook[name] for name in workbook.sheetnames if name.startswith("419") and "dep" in name.lower()),
        None,
    )
    if sheet_419 is None:
        return fallback_tactical
    q_vals: list[float] = []
    skip_children = False
    for row in sheet_419.iter_rows(min_row=2, max_row=528, min_col=10, max_col=17, values_only=True):
        label = str(row[0] or "").strip()
        q_val = row[7]
        if label.startswith("▾") or label == "Otras funcionalidades":
            if "seguimiento_transversal_linktic" in label.lower():
                skip_children = True
                continue
            skip_children = False
        if skip_children:
            continue
        if isinstance(q_val, (int, float)):
            q_vals.append(float(q_val))
    return sum(q_vals) / len(q_vals) if q_vals else fallback_tactical


def update_html(html: str, source: Path, workbook) -> tuple[str, tuple[float, float], tuple[float, float], tuple[float, float], int]:
    cmi = workbook["CMI"]
    raw_tactical_419, strategic_419 = get_cmi_indicators(cmi, "419")
    tactical_419 = get_419_tactical_without_internal(workbook, raw_tactical_419)
    tactical_348, strategic_348 = get_cmi_indicators(cmi, "348")
    tactical_456, strategic_456 = get_cmi_indicators(cmi, "456")
    deliverables_419, delivered_419 = infer_deliverable_counts(strategic_419)
    deliverables_456, delivered_456 = infer_deliverable_counts(strategic_456)

    sheet_348 = next(
        (workbook[name] for name in workbook.sheetnames if name.startswith("348") and "acueducto" in name.lower()),
        None,
    )
    if sheet_348 is None:
        raise ValueError("El consolidado no incluye la hoja 348-SGDEA Acueducto")
    fronts_348 = get_acueducto_fronts(sheet_348)
    deliverables_348, delivered_348 = infer_deliverable_counts(strategic_348)

    fr_match = FR_PATTERN.search(html)
    if fr_match is None:
        raise ValueError("No se encontró la sección FR del tablero")
    fronts_by_project = json.loads(fr_match.group(1))
    fronts_by_project["348"] = fronts_348
    fr_replacement = "const FR=" + json.dumps(fronts_by_project, ensure_ascii=False, separators=(",", ":")) + ";\nconst BOOK416="
    html = html[:fr_match.start()] + fr_replacement + html[fr_match.end():]

    html = replace_project_op(
        html,
        "419",
        f'av:{tactical_419:.10g},ent:{strategic_419:.10g},n:{deliverables_419},d:{delivered_419},u:"funcionalidades"',
    )
    diagnostic_start = html.find('{id:"419",')
    diagnostic_end = html.find('{id:"453",', diagnostic_start)
    if diagnostic_start == -1 or diagnostic_end == -1:
        raise ValueError("No se pudo localizar el diagnóstico de Depósitos Judiciales")
    diagnostic = html[diagnostic_start:diagnostic_end]
    diagnostic, diagnostic_count = re.subn(
        r"avance (?:táctico )?CMI \d{1,3},\d{2}%",
        f"avance táctico CMI {tactical_419 * 100:.2f}%".replace(".", ","),
        diagnostic,
        count=1,
    )
    if diagnostic_count != 1:
        raise ValueError("No se encontró el avance CMI para corregir en el diagnóstico de 419")
    html = html[:diagnostic_start] + diagnostic + html[diagnostic_end:]

    tactical_label = f"{tactical_419 * 100:.2f}%".replace(".", ",")
    strategic_label = f"{strategic_419 * 100:.2f}%".replace(".", ",")
    val_pattern = re.compile(r'"419":\{src:"[^"]*",av:\[[^\]]*\],ent:\[[^\]]*\]\}')
    val_entry = (
        f'"419":{{src:"CMI!I34 = {tactical_label} · K34 = {strategic_label} ({delivered_419}/{deliverables_419})",'
        'av:["p","Indicador táctico tomado directamente de la hoja CMI."],'
        f'ent:["p","Indicador estratégico puntual del CMI: {delivered_419} de {deliverables_419} funcionalidades."]' + "}"
    )
    html, _ = val_pattern.subn(lambda _: val_entry, html, count=1)

    if not re.search(r'\{id:"348",', html):
        acueducto = (
            ' {id:"348",name:"SGDEA Acueducto",opOnly:true,'
            'finNote:"El consolidado operativo no incluye información financiera para este proyecto.",'
            f'op:{{av:{tactical_348:.10g},ent:0.10,n:10,d:1,u:"épicas",isAzure:true,isEpics:true}},'
            'diag:["warn","Información operativa tomada del consolidado de referencia."]},\n'
        )
        anchor = ' {id:"397",'
        if anchor not in html:
            raise ValueError("No se encontró el punto de inserción de proyectos sin libro financiero")
        html = html.replace(anchor, acueducto + anchor, 1)

    html = replace_project_op(
        html,
        "456",
        f'av:{tactical_456:.10g},ent:{strategic_456:.10g},n:{deliverables_456},d:{delivered_456},u:"entregables"',
    )

    return html, (tactical_419, strategic_419), (tactical_348, 0.10), (tactical_456, strategic_456), len(
        [front for front in fronts_348 if len(front) > 1]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Actualiza el HTML desde el consolidado operativo PMO.")
    parser.add_argument("--source", type=Path, help="Archivo Excel de referencia; por defecto usa el más reciente.")
    parser.add_argument("--dry-run", action="store_true", help="Valida y muestra los cambios sin modificar archivos.")
    args = parser.parse_args()

    try:
        import openpyxl
    except ImportError as exc:
        raise RuntimeError("Falta openpyxl. Instálelo con: py -m pip install openpyxl") from exc

    source = args.source.resolve() if args.source else find_latest_source()
    if not source.is_file():
        raise FileNotFoundError(f"No existe el archivo de referencia: {source}")
    if not HTML_PATH.is_file():
        raise FileNotFoundError(f"No existe el tablero: {HTML_PATH}")

    workbook = openpyxl.load_workbook(source, data_only=True, read_only=True)
    try:
        html = HTML_PATH.read_text(encoding="utf-8-sig")
        updated, indicator_419, indicator_348, indicator_456, front_count = update_html(html, source, workbook)
    finally:
        workbook.close()

    if args.dry_run:
        print(f"Referencia: {source.name}")
        print(f"419 táctico/estratégico: {indicator_419[0]:.2%} / {indicator_419[1]:.2%}")
        print(f"348 táctico/estratégico: {indicator_348[0]:.2%} / {indicator_348[1]:.2%}")
        print(f"456 táctico/estratégico: {indicator_456[0]:.2%} / {indicator_456[1]:.2%}")
        print(f"Frentes Acueducto a incorporar: {front_count}")
        print("Dry run: no se modificaron archivos.")
        return 0

    if updated != html:
        history_dir = ROOT / "Histórico tablero"
        history_dir.mkdir(exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup = history_dir / f"Tablero_CMI_PMO_{stamp}.html"
        shutil.copy2(HTML_PATH, backup)

        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", newline="", dir=ROOT, suffix=".tmp", delete=False
        ) as temporary:
            temporary.write(updated)
            temporary_path = Path(temporary.name)
        try:
            temporary_path.replace(HTML_PATH)
        finally:
            temporary_path.unlink(missing_ok=True)
        print(f"Tablero actualizado desde: {source.name} (backup en {backup.name})")
    else:
        print(f"El tablero ya está actualizado con {source.name}.")

    # Sincronización automática de rutas espejo
    home = Path.home()
    mirror_paths = [
        home / "Indicadores estra y tac" / "index.html",
        home / "Indicadores estra y tac" / "Tablero_CMI_PMO.html",
        home / "Downloads" / "Tablero_CMI_PMO.html",
    ]
    for mp in mirror_paths:
        try:
            mp.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(HTML_PATH, mp)
            print(f"Espejo actualizado: {mp}")
        except Exception as e:
            print(f"Aviso espejo ({mp.name}): {e}")

    # Sincronización automática de Épicas y Funcionalidades de Azure DevOps
    sync_script = ROOT / "sync_funcionalidades.py"
    if not sync_script.is_file():
        sync_script = home / "Indicadores estra y tac" / "sync_funcionalidades.py"
    if sync_script.is_file():
        try:
            import subprocess
            print("Sincronizando Épicas y Funcionalidades de Azure DevOps...")
            subprocess.run([sys.executable, str(sync_script)], check=False)
        except Exception as e:
            print(f"Aviso sincronización Azure: {e}")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)

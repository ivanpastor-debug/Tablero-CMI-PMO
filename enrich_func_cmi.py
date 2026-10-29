"""
Enriquece data_func.json, cada data_func/*.json y data_453_cpe.json con el cálculo oficial del
Indicador Táctico y Estratégico de la PMO bajo la Escala CMI por entregable.

Gobernanza de Entregables:
  - Los ENTREGABLES principales de los proyectos se miden formalmente sobre las ÉPICAS (Epics / Frentes)
    en Azure DevOps (004, 348, 355, 384, 397, 416, 419, 421, 457).
  - En el proyecto 453 (Monitoreo CPE), se mide frente a CASOS DE USO (CU) según Estado Interno estados_453.
  - En el proyecto 456 (Aeronáutica Civil), se mide frente a los 6 HITOS CONTRACTUALES en 3 fases.
  - Simultáneamente, se calcula el desglose técnico de FUNCIONALIDADES (Features en Azure) con
    feat_total, feat_ent y porcentaje de cierre para visualización en el contenedor Callout.
"""
import glob
import json
import os
import shutil
from pathlib import Path

EI_453_MAP = {
    "00. en levantamiento/entendimiento": (0.025, "REQUERIMIENTOS"),
    "02. cu registrado en herramienta": (0.075, "REQUERIMIENTOS"),
    "02. rq-artefacto registrado en herramienta": (0.075, "REQUERIMIENTOS"),
    "03. cu en refinamiento": (0.06, "REQUERIMIENTOS"),
    "05. en elaboración escenarios": (0.125, "REQUERIMIENTOS"),
    "06. escenarios registrados en herramienta": (0.15, "REQUERIMIENTOS"),
    "08. escenarios en revisión cliente": (0.175, "REQUERIMIENTOS"),
    "08. pdte aprobación cliente": (0.175, "REQUERIMIENTOS"),
    "09. aprobado por cliente": (0.20, "REQUERIMIENTOS"),
    "10. transversal": (None, "TRANSVERSAL"),
    "13. aprobado por cliente": (0.20, "REQUERIMIENTOS"),
    "15. en desarrollo": (0.50, "DESARROLLO"),
    "16. ajustes": (0.65, "DESARROLLO"),
    "17. ejecución pruebas qa": (0.80, "QA"),
    "17. ejecución pruebas": (0.80, "QA"),
    "18. despliegue qa a uat": (0.90, "UAT"),
    "19. entregado": (1.0, "Terminado o Producción"),
}


def escala_pmo(pct, estado=''):
    if pct is None:
        return 0.0
    if pct >= 0.999:
        return 1.0
    est = str(estado or '').lower()
    if 'uat' in est:
        return 0.75
    if pct > 0.80:
        return 0.50
    if pct >= 0.50:
        return 0.20
    return 0.0


def calc_cmi_project(epics, features, cod):
    valid_epics = [
        e for e in (epics or [])
        if e.get('i') != '_sin_frente'
        and e.get('t') != '(sin frente)'
        and 'seguimiento_transversal_linktic' not in str(e.get('t') or '').lower()
        and str(e.get('i') or '') != '327682'
    ]
    feats = [
        f for f in (features or [])
        if (f.get('n', 0) or 0) > 0
        and 'seguimiento_transversal_linktic' not in str(f.get('ept') or '').lower()
        and str(f.get('ep') or '') != '327682'
    ]
    feat_tot = len(feats)
    feat_ent = sum(1 for f in feats if (f.get('pct') or 0) >= 0.999)

    # 1. 397: Medición oficial acordada sobre 57 Épicas globales (52 al 100%)
    if cod == '397':
        return {
            'tactico': 0.9706,
            'estrategico': 0.9118,
            'n': 57,
            'd': 52,
            'u': 'épicas',
            'isEpics': True,
            'feat_total': 233,
            'feat_ent': 228,
            'buckets': {'100': 52, '75': 2, '50': 2, '20': 1, '0': 0}
        }

    # 2. 419: Depósitos Judiciales - Excepción PMO: mantener archivo local (125 entregadas / 466 entregables)
    # Excluye la épica de seguimiento interno 419DPJ_EP_LT_Seguimiento_Transversal_Linktic y sus 5 funcionalidades
    if cod == '419':
        return {
            'tactico': 0.1195777351,
            'estrategico': 0.2682403433,
            'n': 466,
            'd': 125,
            'u': 'funcionalidades',
            'isEpics': False,
            'feat_total': feat_tot,
            'feat_ent': feat_ent,
            'buckets': {'100': 125, '75': 0, '50': 40, '20': 18, '0': 278}
        }

    # 3. 421: BALÚ Frentes contractuales: Afiliaciones y Novedades (0.5), Recaudo y Cartera (0.2)
    if cod == '421':
        return {
            'tactico': 0.3500,
            'estrategico': 0.0,
            'n': 2,
            'd': 0,
            'u': 'frentes',
            'isEpics': True,
            'feat_total': feat_tot,
            'feat_ent': feat_ent,
            'buckets': {'100': 0, '75': 0, '50': 1, '20': 1, '0': 0}
        }

    # 4. 348: SGDEA Acueducto - 10 Épicas en Azure (1 al 100%: Assesment de Madurez)
    if cod == '348':
        return {
            'tactico': 0.2529,
            'estrategico': 0.1000,
            'n': 10,
            'd': 1,
            'u': 'épicas',
            'isEpics': True,
            'feat_total': feat_tot,
            'feat_ent': feat_ent,
            'buckets': {'100': 1, '75': 0, '50': 2, '20': 4, '0': 3}
        }

    # 5. 416: Positiva Core 416 - 2 Épicas / Ramos (Vida Individual y Accidentes Personales)
    if cod == '416':
        return {
            'tactico': 0.2900,
            'estrategico': 0.0,
            'n': 2,
            'd': 0,
            'u': 'épicas',
            'isEpics': True,
            'feat_total': feat_tot,
            'feat_ent': feat_ent,
            'buckets': {'100': 0, '75': 0, '50': 0, '20': 0, '0': 2}
        }

    # 6. 456: Innovación Aeronáutica Civil - Supervisión contractual (6 hitos: 1 al 100%, 1 al 50% -> 24% táctico, 16,67% estratégico)
    # integrada con captura directa de Azure DevOps (1 Épica, 4 Funcionalidades, 16 HUs)
    if cod == '456':
        hu_tot = sum((f.get('n', 0) or 0) for f in feats)
        pct_az = round(sum((f.get('pct', 0) or 0) * (f.get('n', 0) or 0) for f in feats) / hu_tot, 4) if hu_tot else 0.0
        return {
            'tactico': 0.2400,
            'estrategico': round(1 / 6, 4),
            'n': 6,
            'd': 1,
            'u': 'entregables',
            'isEpics': False,
            'feat_total': feat_tot,
            'feat_ent': feat_ent,
            'epic_total': len(valid_epics),
            'hu_total': hu_tot,
            'pct_azure': pct_az,
            'buckets': {'100': 1, '75': 0, '50': 1, '20': 0, '0': 4}
        }

    # 6. Cálculo general sobre Épicas válidas en Azure DevOps (incluye 004, 355, 384, 419-DEP, 419-RAMA, 457, etc.)
    buckets = {1.0: 0, 0.75: 0, 0.5: 0, 0.2: 0, 0.0: 0}
    scores = []
    for e in valid_epics:
        pct = e.get('pct', 0.0)
        sc = escala_pmo(pct, e.get('e', ''))
        buckets[sc] += 1
        scores.append(sc)

    n = len(valid_epics)
    d = buckets[1.0]
    av = sum(scores) / n if n else 0.0
    ent = d / n if n else 0.0

    return {
        'tactico': round(av, 4),
        'estrategico': round(ent, 4),
        'n': n,
        'd': d,
        'u': 'épicas',
        'isEpics': True,
        'feat_total': feat_tot,
        'feat_ent': feat_ent,
        'buckets': {
            '100': buckets[1.0],
            '75': buckets[0.75],
            '50': buckets[0.5],
            '20': buckets[0.2],
            '0': buckets[0.0]
        }
    }


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_func_dir = os.path.join(base_dir, 'data_func')
    index_file = os.path.join(base_dir, 'data_func.json')
    cpe_file = os.path.join(base_dir, 'data_453_cpe.json')

    if not os.path.exists(index_file):
        print("No se encontró data_func.json en", base_dir)
        return

    with open(index_file, 'r', encoding='utf-8') as f:
        index_data = json.load(f)

    cmi_por_cod = {}

    # 1. Procesar cada archivo individual de detalle de funcionalidades
    json_files = glob.glob(os.path.join(data_func_dir, '*.json'))
    for path in sorted(json_files):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        cod = data.get('codigo') or os.path.splitext(os.path.basename(path))[0]

        cmi = calc_cmi_project(data.get('epics', []), data.get('features', []), cod)
        data['cmi'] = cmi
        cmi_por_cod[cod] = cmi

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"[{cod:8s}] Táctico: {cmi['tactico']*100:6.2f}% | Estratégico: {cmi['estrategico']*100:6.2f}% ({cmi['d']}/{cmi['n']} {cmi['u']}) | Feat: {cmi['feat_ent']}/{cmi['feat_total']}")

    # 2. Agregar CMI consolidado para POS (355 + 416)
    if '355' in cmi_por_cod and '416' in cmi_por_cod:
        c355 = cmi_por_cod['355']
        c416 = cmi_por_cod['416']
        n_pos = c355['n'] + c416['n']
        d_pos = c355['d'] + c416['d']
        av_pos = (c355['n'] * c355['tactico'] + c416['n'] * c416['tactico']) / n_pos if n_pos else 0.0
        ent_pos = d_pos / n_pos if n_pos else 0.0
        f_tot_pos = c355.get('feat_total', 82) + c416.get('feat_total', 7)
        f_ent_pos = c355.get('feat_ent', 6) + c416.get('feat_ent', 0)
        cmi_por_cod['POS'] = {
            'tactico': round(av_pos, 4),
            'estrategico': round(ent_pos, 4),
            'n': n_pos,
            'd': d_pos,
            'u': 'épicas',
            'isEpics': True,
            'feat_total': f_tot_pos,
            'feat_ent': f_ent_pos,
            'buckets': {
                '100': c355['buckets']['100'] + c416['buckets']['100'],
                '75': c355['buckets']['75'] + c416['buckets']['75'],
                '50': c355['buckets']['50'] + c416['buckets']['50'],
                '20': c355['buckets']['20'] + c416['buckets']['20'],
                '0': c355['buckets']['0'] + c416['buckets']['0']
            }
        }
        print(f"[POS cons] Táctico: {cmi_por_cod['POS']['tactico']*100:6.2f}% | Estratégico: {cmi_por_cod['POS']['estrategico']*100:6.2f}% ({d_pos}/{n_pos} épicas) | Feat: {f_ent_pos}/{f_tot_pos}")

    # 3. Guardar en data_func.json
    corte_pos = index_data.get('proyectos', {}).get('355', {}).get('corte', '2026-10-26')
    for cod, cmi in cmi_por_cod.items():
        if cod in index_data.get('proyectos', {}):
            index_data['proyectos'][cod]['cmi'] = cmi
        elif cod == 'POS':
            index_data['proyectos']['POS'] = {
                'corte': corte_pos,
                'archivo': 'Consolidado Positiva Core (355 + 416)',
                'cmi': cmi
            }

    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    # 4. Procesar y enriquecer 453 (Monitoreo CPE) con Casos de Uso y Fechas
    if os.path.exists(cpe_file):
        with open(cpe_file, 'r', encoding='utf-8') as f:
            cpe_data = json.load(f)

        # Aplicar homologación completa de estados_453 a cada Caso de Uso
        cus_list = cpe_data.get('cus', [])
        for cu in cus_list:
            ei_raw = (cu.get('ei') or '').strip().lower()
            if ei_raw in EI_453_MAP:
                cu['pct_cu'], cu['proc_cu'] = EI_453_MAP[ei_raw]

        # Recalcular pct_cu y term_cu por iteración
        for it in cpe_data.get('iteraciones', []):
            ik = it.get('k')
            cus_it = [c for c in cus_list if c.get('it') == ik]
            vs_cu = [c['pct_cu'] for c in cus_it if c.get('pct_cu') is not None]
            it['n_cu'] = len(cus_it)
            it['n_cu_pct'] = len(vs_cu)
            it['pct_cu'] = round(sum(vs_cu) / len(vs_cu), 4) if vs_cu else None
            it['term_cu'] = sum(1 for c in cus_it if c.get('ei') == '19. Entregado' or c.get('pct_cu') == 1.0)

        focos_fechas = {
            'A': {'inicio': '2026-02-25', 'fecha': '2026-10-24', 'fecha_plan': '2026-07-30', 'peso': '40%', 'nota': 'Hito reprogramado al 24/10/2026 (base: 30/07/2026)'},
            'B': {'inicio': '2026-07-01', 'fecha': '2026-12-25', 'fecha_plan': '2026-10-15', 'peso': '30%', 'nota': 'Hito reprogramado al 25/12/2026 (base: 15/10/2026)'},
            'C': {'inicio': '2026-09-16', 'fecha': '2026-10-30', 'fecha_plan': '2026-11-27', 'peso': '15%', 'nota': 'Hito reprogramado al 30/10/2026 (base: 27/11/2026)'},
            'D': {'inicio': '2026-10-30', 'fecha': '2026-12-30', 'fecha_plan': '2026-12-30', 'peso': '15%', 'nota': 'Hito al 30/12/2026'}
        }

        for foc in cpe_data.get('focos', []):
            fk = foc.get('k')
            if fk in focos_fechas:
                foc['hito'] = focos_fechas[fk]
                foc['sem'] = 'en_curso' if fk in ['A', 'B', 'C'] else 'sin_iniciar'
            cus_foco = [c for c in cus_list if fk in (c.get('fs') or []) or c.get('fp') == fk]
            vs_cu = [c['pct_cu'] for c in cus_foco if c.get('pct_cu') is not None]
            foc['n_cu'] = len(cus_foco)
            foc['n_cu_medibles'] = len(vs_cu)
            foc['pct_cu'] = round(sum(vs_cu) / len(vs_cu), 4) if vs_cu else None
            foc['term_cu'] = sum(1 for c in cus_foco if c.get('ei') == '19. Entregado' or c.get('pct_cu') == 1.0)

        # Asignar fecha de iteración en cada caso de uso para renderizado directo
        it_fechas = {}
        for it in cpe_data.get('iteraciones', []):
            if it.get('hito') and it['hito'].get('fecha'):
                it_fechas[it['k']] = {
                    'release': it['hito'].get('release'),
                    'fecha': it['hito'].get('fecha')
                }

        for cu in cus_list:
            it_k = cu.get('it')
            if it_k in it_fechas:
                cu['release'] = it_fechas[it_k]['release']
                cu['fecha_entrega'] = it_fechas[it_k]['fecha']

        medibles = [c for c in cus_list if c.get('pct_cu') is not None]
        n_cu = len(medibles)
        d_cu = sum(1 for c in medibles if c.get('ei') == '19. Entregado' or c.get('pct_cu') >= 0.999)
        av_cu = round(sum(c['pct_cu'] for c in medibles) / n_cu, 4) if n_cu else 0.0
        ent_cu = round(d_cu / n_cu, 4) if n_cu else 0.0

        k = cpe_data.setdefault('kpi', {})
        k['n_cu'] = len(cus_list)
        k['n_cu_medibles'] = n_cu
        k['cu_entregados'] = d_cu
        k['pct_cu_global'] = av_cu

        cpe_data['cmi'] = {
            'tactico': av_cu,
            'estrategico': ent_cu,
            'n': n_cu,
            'd': d_cu,
            'u': 'casos de uso',
            'buckets': {
                '100': d_cu,
                '75': sum(1 for c in medibles if 0.85 <= c['pct_cu'] < 0.999),
                '50': sum(1 for c in medibles if 0.80 <= c['pct_cu'] < 0.85),
                '20': sum(1 for c in medibles if 0.50 <= c['pct_cu'] < 0.80),
                '0': sum(1 for c in medibles if c['pct_cu'] < 0.50)
            }
        }

        with open(cpe_file, 'w', encoding='utf-8') as f:
            json.dump(cpe_data, f, ensure_ascii=False, indent=2)

        print(f"[453 (CU)] Táctico: {cpe_data['cmi']['tactico']*100:6.2f}% | Estratégico: {cpe_data['cmi']['estrategico']*100:6.2f}% ({d_cu}/{n_cu} Casos de Uso medibles de {len(cus_list)} totales)")

    # 5. Sincronizar espejos
    home = str(Path.home())
    mirror_dirs = [
        os.path.join(home, 'Indicadores estra y tac'),
        os.path.join(home, 'Documents', 'PMO INDICADORES', 'CMI'),
        os.path.join(home, 'Downloads')
    ]
    for md in mirror_dirs:
        if not os.path.exists(md) or os.path.normcase(os.path.abspath(md)) == os.path.normcase(base_dir):
            continue
        shutil.copy2(index_file, os.path.join(md, 'data_func.json'))
        if os.path.exists(cpe_file):
            shutil.copy2(cpe_file, os.path.join(md, 'data_453_cpe.json'))
        target_fnc = os.path.join(md, 'data_func')
        if os.path.exists(target_fnc):
            shutil.rmtree(target_fnc)
        shutil.copytree(data_func_dir, target_fnc)
        print(f"Sincronizado a espejo: {md}")

    print("Enriquecimiento CMI completado con éxito.")


if __name__ == '__main__':
    main()

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
    "16. ajustes": (0.40, "DESARROLLO"),
    "16. ajustes desarrollo": (0.40, "DESARROLLO"),
    "17. ejecución pruebas qa": (0.80, "QA"),
    "17. ejecución pruebas": (0.80, "QA"),
    "18. despliegue qa a uat": (0.90, "UAT"),
    "19. entregado": (1.0, "Terminado o Producción"),
}


def hu_escala_item(h):
    if not h or h.get('a') == 0:
        return None
    sg = str(h.get('p') or '').upper().strip()
    st = str(h.get('e') or '').lower().strip()
    v = h.get('v')

    if st.startswith('x') or st == 'removido' or sg in ['EXCLUIR', 'OMITIR']:
        return None

    # 1. 100% - Terminado / En Producción
    if (sg == "EN PRODUCCIÓN" or 
        st.startswith("4. cerrado") or 
        st.startswith("10. en producción") or 
        st.startswith("10. en produccion") or
        st.startswith("12 - en producción") or
        st.startswith("12 - en produccion") or
        st.startswith("20. aprobado") or
        (v is not None and v >= 0.999)):
        return 1.0

    # 2. 75% - UAT del Cliente (En Pruebas / Aprobación UAT)
    if (st.startswith("8.1") or 
        st.startswith("8.2") or 
        st.startswith("9. esperando") or 
        "uat" in st or 
        sg == "CLIENTE" or 
        "UAT" in sg or 
        "DESPLEGAR" in sg):
        return 0.75

    # 3. 50% - Pre-UAT / QA Concluido / Esperando QA-UAT / 3. Entregado
    if (st.startswith("8. esperando despliegue qa-uat") or 
        st.startswith("7.2") or 
        st.startswith("3. entregado") or 
        (v is not None and v >= 0.80)):
        return 0.50

    # 4. 20% - QA (Backlog QA y Pruebas QA en curso)
    if (st.startswith("7.") or 
        st.startswith("7 ") or 
        st.startswith("6. backlog qa") or 
        st.startswith("3. aseguramiento") or 
        sg == "QA" or 
        "qa" in st or 
        (v is not None and v >= 0.50)):
        return 0.20

    # 5. 0% - Requerimientos y Desarrollo (No superan el 50%)
    return 0.0

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


def calc_cmi_project(epics, features, cod, hus=None):
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

    # 1. 397: Medición oficial acordada sobre 57 Épicas globales (52 al 100%) con desglose de 233 Features
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

    # 2. 348 / 419: Excepciones
    if cod == '348':
        target_epics = ['539569', '539200']
        valid_epics = [e for e in (epics or []) if str(e.get('i') or '') in target_epics]
        feats = [
            f for f in (features or [])
            if str(f.get('ep') or '') in target_epics and (f.get('n', 0) or 0) > 0
        ]
        feat_tot = len(feats)
        feat_ent = sum(1 for f in feats if (f.get('pct') or 0) >= 0.999)

    if cod == '419':
        return {
            'tactico': 0.1195777351,
            'estrategico': 0.1716738197,
            'n': 466,
            'd': 80,
            'u': 'funcionalidades',
            'isEpics': False,
            'feat_total': feat_tot,
            'feat_ent': feat_ent,
            'buckets': {'100': 80, '75': 0, '50': 40, '20': 18, '0': 328}
        }

    # 3. 421: BALÚ - Filtrar frentes de producto (Afiliaciones y Recaudo; excluir Transversales y Automatización QA)
    if cod == '421':
        excluded_epics = ['funcionalidades transversales', 'automatización_qa balu', 'automatizacion_qa balu']
        feats = [
            f for f in feats
            if not any(ex in str(f.get('ept') or '').strip().lower() for ex in excluded_epics)
        ]
        feat_tot = len(feats)

    # 4. 416: Positiva Core 416 - Excepción oficial: Manejar por Épicas pero nombradas como RAMOS
    if cod == '416':
        return {
            'tactico': 0.2900,
            'estrategico': 0.0,
            'n': 2,
            'd': 0,
            'u': 'ramos',
            'isEpics': True,
            'isRamos': True,
            'feat_total': feat_tot,
            'feat_ent': feat_ent,
            'buckets': {'100': 0, '75': 0, '50': 0, '20': 0, '0': 2}
        }

    # 5. 456: Innovación Aeronáutica Civil - Supervisión contractual (6 hitos: 1 al 100%, 1 al 50% -> 24% táctico, 16,67% estratégico)
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

    # 6. Regla General PMO:
    #    - Distribución en Escala PMO (buckets): se mide sobre las HISTORIAS DE USUARIO (HU) activas.
    #    - % Táctico por Funcionalidad: promedio aritmético de las HU activas que la componen.
    #    - Indicador Táctico del Proyecto: promedio aritmético del % Táctico de las funcionalidades.
    #    - Indicador Estratégico: funcionalidades al 100% (en producción / táctico >= 0.999) / total funcionalidades.
    hu_by_feat = {}
    for h in (hus or []):
        fid = h.get('f')
        if fid:
            hu_by_feat.setdefault(fid, []).append(h)

    hu_buckets = {'100': 0, '75': 0, '50': 0, '20': 0, '0': 0}
    feat_buckets = {'100': 0, '75': 0, '50': 0, '20': 0, '0': 0}
    total_hus_eval = 0
    scores = []

    for f in feats:
        f_hus = hu_by_feat.get(f.get('i'), [])
        hu_scores = []
        for h in f_hus:
            sc = hu_escala_item(h)
            if sc is not None:
                total_hus_eval += 1
                hu_scores.append(sc)
                if sc == 1.0:
                    hu_buckets['100'] += 1
                elif sc == 0.75:
                    hu_buckets['75'] += 1
                elif sc == 0.50:
                    hu_buckets['50'] += 1
                elif sc == 0.20:
                    hu_buckets['20'] += 1
                else:
                    hu_buckets['0'] += 1

        if hu_scores:
            avg_f = sum(hu_scores) / len(hu_scores)
        else:
            avg_f = escala_pmo(f.get('pct', 0.0), f.get('e', ''))

        scores.append(avg_f)

        if avg_f >= 0.999:
            feat_buckets['100'] += 1
        elif avg_f >= 0.75:
            feat_buckets['75'] += 1
        elif avg_f >= 0.50:
            feat_buckets['50'] += 1
        elif avg_f >= 0.20:
            feat_buckets['20'] += 1
        else:
            feat_buckets['0'] += 1

    n = len(feats)
    d = sum(1 for s in scores if s >= 0.999)
    av = sum(scores) / n if n else 0.0
    ent = d / n if n else 0.0

    return {
        'tactico': round(av, 4),
        'estrategico': round(ent, 4),
        'n': n,
        'd': d,
        'u': 'funcionalidades',
        'isEpics': False,
        'feat_total': feat_tot,
        'feat_ent': d,
        'hu_total': total_hus_eval,
        'buckets': hu_buckets,
        'hu_buckets': hu_buckets,
        'feat_buckets': feat_buckets
    }

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_func_dir = os.path.join(base_dir, 'data_func')
    index_file = os.path.join(base_dir, 'data_func.json')
    cpe_file = os.path.join(base_dir, 'data_453_cpe.json')

    if not os.path.exists(index_file):
        print("No se encontró data_func.json en", base_dir)
        return

    with open(index_file, 'r', encoding='utf-8-sig') as f:
        index_data = json.load(f)

    cmi_por_cod = {}

    # 0. Cargar data_rqc.json si existe para Proyecto 421 (Balú)
    rqc_file = os.path.join(base_dir, 'data_rqc.json')
    rqc_421_block = None
    if os.path.exists(rqc_file):
        try:
            with open(rqc_file, 'r', encoding='utf-8') as rf:
                rqc_raw = json.load(rf)
            rqc_421_block = {
                'corte': rqc_raw.get('corte'),
                'total': rqc_raw.get('total', 913),
                'removidos': rqc_raw.get('removidos', 283),
                'activos': rqc_raw.get('activos', 630),
                'cumplidos': rqc_raw.get('cumplidos', 305),
                'cumplimiento': rqc_raw.get('cumplimiento', 0.4841),
                'resumen': rqc_raw.get('resumen', {}),
                'por_componente': rqc_raw.get('por_componente', {}),
            }
            print(f"[RQC 421] Cumplimiento: {rqc_421_block['cumplimiento']*100:.2f}% ({rqc_421_block['cumplidos']}/{rqc_421_block['activos']} activos, {rqc_421_block['removidos']} removidos)")
        except Exception as e:
            print(f"Aviso lectura data_rqc.json: {e}")

    # 1. Procesar cada archivo individual de detalle de funcionalidades
    json_files = glob.glob(os.path.join(data_func_dir, '*.json'))
    for path in sorted(json_files):
        with open(path, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
        cod = data.get('codigo') or os.path.splitext(os.path.basename(path))[0]

        if cod == '421':
            excluded_epics = ["funcionalidades transversales", "automatización_qa balu", "automatizacion_qa balu"]
            valid_epics = [
                e for e in (data.get("epics") or [])
                if not any(ex in str(e.get("t") or "").strip().lower() for ex in excluded_epics)
            ]
            valid_epic_ids = {str(e.get("i")) for e in valid_epics}
            valid_features = [
                f for f in (data.get("features") or [])
                if str(f.get("ep")) in valid_epic_ids
                and not any(ex in str(f.get("ept") or "").strip().lower() for ex in excluded_epics)
            ]
            valid_feat_ids = {str(f.get("i")) for f in valid_features}
            valid_hus = [
                h for h in (data.get("hus") or [])
                if str(h.get("f")) in valid_feat_ids
            ]

            n_hu = len(valid_hus)
            n_hu_act = len([h for h in valid_hus if h.get("a") != 0])
            term_global = sum(1 for h in valid_hus if (h.get("p") == "EN PRODUCCIÓN" or (h.get("v") is not None and h.get("v") >= 0.999)))

            data["epics"] = valid_epics
            data["features"] = valid_features
            data["hus"] = valid_hus
            data["kpi"] = {
                "n_hu": n_hu,
                "n_hu_activas": n_hu_act,
                "hu_sin_feature": 0,
                "n_feature": len(valid_features),
                "n_epic": len(valid_epics),
                "n_feature_con_hu": sum(1 for f in valid_features if (f.get("n", 0) or 0) > 0),
                "feature_sin_hu": sum(1 for f in valid_features if (f.get("n", 0) or 0) == 0),
                "hu_omitidas": sum(1 for h in valid_hus if h.get("a") == 0),
                "pct_global": round(sum((f.get("pct", 0) or 0) * (f.get("n", 0) or 0) for f in valid_features) / sum(f.get("n", 0) or 0 for f in valid_features), 4) if valid_features else 0.0,
                "term_global": term_global,
                "feature_sin_frente": 0,
                "hu_sin_frente": 0,
                "feature_100_sin_cerrar": sum(1 for f in valid_features if (f.get("pct") or 0) >= 0.999 and not str(f.get("e", "")).startswith("4")),
                "feature_estado_ajeno": 0,
                "feature_removido_con_hu": 0,
            }

        cmi = calc_cmi_project(data.get('epics', []), data.get('features', []), cod, data.get('hus', []))
        data['cmi'] = cmi
        if cod == '421' and rqc_421_block:
            data['rqc'] = rqc_421_block
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

    if rqc_421_block and '421' in index_data.get('proyectos', {}):
        index_data['proyectos']['421']['rqc'] = rqc_421_block

    # Actualizar KPI de 421 en el índice con el alcance de producto certificado (56 func en 2 frentes)
    if '421' in index_data.get('proyectos', {}):
        f421_p = os.path.join(data_func_dir, '421.json')
        if os.path.exists(f421_p):
            with open(f421_p, 'r', encoding='utf-8') as rf:
                d421 = json.load(rf)
            if 'kpi' in d421:
                index_data['proyectos']['421']['kpi'] = d421['kpi']
                index_data['proyectos']['421']['archivo'] = "Azure DevOps · 56 Funcionalidades de Producto (2 Frentes)"

    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    # 4. Procesar y enriquecer 453 (Monitoreo CPE) con Casos de Uso y Fechas
    if os.path.exists(cpe_file):
        with open(cpe_file, 'r', encoding='utf-8-sig') as f:
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

        # Medición oficial PMO para 453 sobre la totalidad de los CASOS DE USO (76 CUs)
        focos_list = cpe_data.get('focos', [])
        total_exito_cu = 0.0
        for f in focos_list:
            fk = f.get('k')
            peso_str = (f.get('hito') or {}).get('peso', '0%')
            peso_num = float(peso_str.replace('%', '')) / 100.0 if '%' in peso_str else float(f.get('peso') or 0.0)
            f['peso_num'] = peso_num
            pct_cu_val = f.get('pct_cu')
            aporte_cu = round(peso_num * pct_cu_val, 4) if (pct_cu_val is not None) else 0.0
            f['aporte_cu'] = aporte_cu
            total_exito_cu += aporte_cu

        cu_scores = []
        b_cus = {'100': 0, '75': 0, '50': 0, '20': 0, '0': 0}
        d_cus = 0
        n_cus = len(cus_list)
        for cu in cus_list:
            pct_val = cu.get('pct_cu')
            if pct_val is not None:
                sc = escala_pmo(pct_val, cu.get('ei', ''))
            else:
                sc = 0.0
            cu_scores.append(sc)
            if sc == 1.0:
                b_cus['100'] += 1
                d_cus += 1
            elif sc == 0.75:
                b_cus['75'] += 1
            elif sc == 0.50:
                b_cus['50'] += 1
            elif sc == 0.20:
                b_cus['20'] += 1
            else:
                b_cus['0'] += 1

        av_cus = round(sum(cu_scores) / n_cus, 4) if n_cus else 0.0
        ent_cus = round(d_cus / n_cus, 4) if n_cus else 0.0

        cpe_data['cmi'] = {
            'tactico': av_cus,
            'estrategico': ent_cus,
            'exito': round(total_exito_cu, 4),
            'n': n_cus,
            'd': d_cus,
            'u': 'casos de uso',
            'isFocos': False,
            'isCus': True,
            'feat_total': n_cus,
            'feat_ent': d_cus,
            'buckets': b_cus
        }

        # Mantener métricas complementarias de Casos de Uso en KPI
        medibles = [c for c in cus_list if c.get('pct_cu') is not None]
        n_cu = len(medibles)
        d_cu = sum(1 for c in medibles if c.get('ei') == '19. Entregado' or c.get('pct_cu') >= 0.999)
        av_cu = round(sum(c['pct_cu'] for c in medibles) / n_cu, 4) if n_cu else 0.0

        k = cpe_data.setdefault('kpi', {})
        k['n_cu'] = len(cus_list)
        k['n_cu_medibles'] = n_cu
        k['cu_entregados'] = d_cu
        k['pct_cu_global'] = av_cu

        with open(cpe_file, 'w', encoding='utf-8') as f:
            json.dump(cpe_data, f, ensure_ascii=False, indent=2)

        index_data.setdefault('proyectos', {})['453'] = {
            'corte': cpe_data.get('corte', '2026-11-06'),
            'archivo': '453 CPE (Focos y Casos de Uso)',
            'cmi': cpe_data['cmi']
        }
        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)

        print(f"[453 (CUs)]   Táctico: {cpe_data['cmi']['tactico']*100:6.2f}% | Estratégico: {cpe_data['cmi']['estrategico']*100:6.2f}% ({d_cus}/{n_cus} CUs entregados)")

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

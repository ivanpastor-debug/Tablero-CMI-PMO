"""
Enriquece data_func.json, cada data_func/*.json y data_453_cpe.json con el cálculo oficial del
Indicador Táctico y Estratégico de la PMO bajo la Escala CMI por entregable.

Gobernanza de Entregables:
  - Los ENTREGABLES principales de los proyectos se miden formalmente sobre las ÉPICAS (Epics / Frentes)
    en Azure DevOps (004, 348, 355, 384, 397, 416, 419, 421).
  - En el proyecto 453 (Monitoreo CPE), se mide frente a CASOS DE USO (CU) según Estado Interno estados_453.
  - En el proyecto 456 (Aeronáutica Civil), se mide frente a los 6 HITOS CONTRACTUALES en 3 fases.
  - Simultáneamente, se calcula el desglose técnico de FUNCIONALIDADES (Features en Azure) con
    feat_total, feat_ent y porcentaje de cierre para visualización en el contenedor Callout.
"""
import json
import glob
import os
import shutil

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
    valid_epics = [e for e in (epics or []) if e.get('i') != '_sin_frente' and e.get('t') != '(sin frente)']
    feats = [f for f in (features or []) if (f.get('n', 0) or 0) > 0]
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
    if cod == '419':
        return {
            'tactico': 0.1201,
            'estrategico': 0.2682,
            'n': 466,
            'd': 125,
            'u': 'funcionalidades',
            'isEpics': False,
            'feat_total': feat_tot,
            'feat_ent': feat_ent,
            'buckets': {'100': 125, '75': 0, '50': 40, '20': 23, '0': 278}
        }

    # 2. 421: BALÚ Frentes contractuales: Afiliaciones y Novedades (0.5), Recaudo y Cartera (0.2)
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

    # 3. 348: SGDEA Acueducto - 10 Épicas en Azure (1 al 100%: Assesment de Madurez)
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

    # 4. 416: Positiva Core 416 - 2 Épicas / Ramos (Vida Individual y Accidentes Personales)
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

    # 5. Cálculo general sobre Épicas válidas en Azure DevOps
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

        print(f"[{cod:8s}] Táctico: {cmi['tactico']*100:6.2f}% | Estratégico: {cmi['estrategico']*100:6.2f}% ({cmi['d']}/{cmi['n']} {cmi['u']})")

    # 2. Agregar CMI consolidado para POS (355 + 416)
    if '355' in cmi_por_cod and '416' in cmi_por_cod:
        c355 = cmi_por_cod['355']
        c416 = cmi_por_cod['416']
        n_pos = c355['n'] + c416['n']
        d_pos = c355['d'] + c416['d']
        av_pos = (c355['n'] * c355['tactico'] + c416['n'] * c416['tactico']) / n_pos if n_pos else 0.0
        ent_pos = d_pos / n_pos if n_pos else 0.0
        f_tot_pos = c355.get('feat_total', 80) + c416.get('feat_total', 7)
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
        print(f"[POS cons] Táctico: {cmi_por_cod['POS']['tactico']*100:6.2f}% | Estratégico: {cmi_por_cod['POS']['estrategico']*100:6.2f}% ({d_pos}/{n_pos} épicas)")

    # 3. Guardar en data_func.json
    for cod, cmi in cmi_por_cod.items():
        if cod in index_data.get('proyectos', {}):
            index_data['proyectos'][cod]['cmi'] = cmi
        elif cod == 'POS':
            index_data['proyectos']['POS'] = {
                'corte': '2026-09-25',
                'archivo': 'Consolidado Positiva Core (355 + 416)',
                'cmi': cmi
            }

    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    # 4. Procesar y enriquecer 453 (Monitoreo CPE) con Casos de Uso y Fechas
    if os.path.exists(cpe_file):
        with open(cpe_file, 'r', encoding='utf-8') as f:
            cpe_data = json.load(f)

        focos_fechas = {
            'A': {'inicio': '2026-02-25', 'fecha': '2026-10-24', 'fecha_plan': '2026-07-30', 'peso': '40%', 'nota': 'Hito reprogramado al 24/10/2026 (base: 30/07/2026)'},
            'B': {'inicio': '2026-07-01', 'fecha': '2026-12-25', 'fecha_plan': '2026-10-15', 'peso': '30%', 'nota': 'Hito reprogramado al 25/12/2026 (base: 15/10/2026)'},
            'C': {'inicio': '2026-09-16', 'fecha': '2026-10-30', 'fecha_plan': '2026-11-27', 'peso': '15%', 'nota': 'Hito reprogramado al 30/10/2026 (base: 27/11/2026)'},
            'D': {'inicio': '2026-10-30', 'fecha': '2026-12-30', 'fecha_plan': '2026-12-30', 'peso': '15%', 'nota': 'Hito al 30/12/2026'}
        }

        for foc in cpe_data.get('focos', []):
            k = foc.get('k')
            if k in focos_fechas:
                foc['hito'] = focos_fechas[k]
                foc['sem'] = 'en_curso' if k in ['A', 'B', 'C'] else 'sin_iniciar'

        # Asignar fecha de iteración en cada caso de uso para renderizado directo
        it_fechas = {}
        for it in cpe_data.get('iteraciones', []):
            if it.get('hito') and it['hito'].get('fecha'):
                it_fechas[it['k']] = {
                    'release': it['hito'].get('release'),
                    'fecha': it['hito'].get('fecha')
                }

        for cu in cpe_data.get('cus', []):
            it_k = cu.get('it')
            if it_k in it_fechas:
                cu['release'] = it_fechas[it_k]['release']
                cu['fecha_entrega'] = it_fechas[it_k]['fecha']

        k = cpe_data.get('kpi', {})
        n_cu = k.get('n_cu_medibles') or k.get('n_cu') or 45
        d_cu = k.get('cu_entregados') or 4
        av_cu = k.get('pct_cu_global') or 0.303
        ent_cu = d_cu / n_cu if n_cu else 0.0

        cpe_data['cmi'] = {
            'tactico': round(av_cu, 4),
            'estrategico': round(ent_cu, 4),
            'n': n_cu,
            'd': d_cu,
            'u': 'casos de uso',
            'buckets': {
                '100': d_cu,
                '75': 0,
                '50': sum(1 for c in cpe_data.get('cus', []) if c.get('pct_cu') is not None and c['pct_cu'] > 0.8 and c['pct_cu'] < 0.999),
                '20': sum(1 for c in cpe_data.get('cus', []) if c.get('pct_cu') is not None and c['pct_cu'] >= 0.5 and c['pct_cu'] <= 0.8),
                '0': sum(1 for c in cpe_data.get('cus', []) if c.get('pct_cu') is not None and c['pct_cu'] < 0.5)
            }
        }

        with open(cpe_file, 'w', encoding='utf-8') as f:
            json.dump(cpe_data, f, ensure_ascii=False, indent=2)

        print(f"[453 (CU)] Táctico: {cpe_data['cmi']['tactico']*100:6.2f}% | Estratégico: {cpe_data['cmi']['estrategico']*100:6.2f}% ({d_cu}/{n_cu} Casos de Uso)")

    # 5. Sincronizar espejos
    mirror_dirs = [
        r'C:\Users\Usuario1\Documents\PMO INDICADORES\CMI',
        r'C:\Users\Usuario1\Downloads'
    ]
    for md in mirror_dirs:
        if not os.path.exists(md):
            continue
        # copiar data_func.json
        shutil.copy2(index_file, os.path.join(md, 'data_func.json'))
        # copiar data_453_cpe.json
        if os.path.exists(cpe_file):
            shutil.copy2(cpe_file, os.path.join(md, 'data_453_cpe.json'))
        # copiar data_func/
        target_fnc = os.path.join(md, 'data_func')
        if os.path.exists(target_fnc):
            shutil.rmtree(target_fnc)
        shutil.copytree(data_func_dir, target_fnc)
        print(f"Sincronizado a espejo: {md}")

    print("Enriquecimiento CMI completado con éxito.")

if __name__ == '__main__':
    main()

"""
Enriquece data_func.json, cada data_func/*.json y data_453_cpe.json con el cálculo oficial del
Indicador Táctico y Estratégico de la PMO bajo la Escala CMI por entregable.

Para proyectos con funcionalidades (004, 348, 355, 384, 397, 416, 419, 421):
  - 100% (1.00): En producción (pct >= 0.999)
  - 75%  (0.75): En UAT del cliente
  - 50%  (0.50): En curso >80% (pct > 0.80)
  - 20%  (0.20): En curso 50-80% (pct >= 0.50)
  - 0%   (0.00): En curso <50% (pct < 0.50)

Para el proyecto 453 (Monitoreo CPE):
  - Conteo oficial frente a CASOS DE USO (CU) únicamente, no frente a HU.
  - Indicador Táctico = % Avance Casos de Uso según Estado Interno estados_453 (30,30%).
  - Indicador Estratégico = CUs entregados al 100% (19. Entregado) sobre CUs medibles (4 / 45 = 8,89%).
  - Fechas comprometidas por Foco e Iteración normalizadas con semáforos.
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

def calc_cmi_project(features):
    fs = [f for f in (features or []) if (f.get('n', 0) or 0) > 0]
    buckets = {1.0: 0, 0.75: 0, 0.5: 0, 0.2: 0, 0.0: 0}
    for f in fs:
        sc = escala_pmo(f.get('pct'), f.get('e'))
        buckets[sc] += 1
    n = len(fs)
    d = buckets[1.0]
    av = sum(k * v for k, v in buckets.items()) / n if n else 0.0
    ent = d / n if n else 0.0
    return {
        'tactico': round(av, 4),
        'estrategico': round(ent, 4),
        'n': n,
        'd': d,
        'u': 'funcionalidades',
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
        if cod == '397':
            # Medición oficial PMO sobre las 57 Épicas de Azure DevOps con desglose de 233 Funcionalidades
            cmi = {
                'tactico': 0.9706,
                'estrategico': 0.9118,
                'n': 57,
                'd': 52,
                'u': 'épicas',
                'isEpics': True,
                'feat_total': 233,
                'feat_ent': 228,
                'buckets': {
                    '100': 52,
                    '75': 2,
                    '50': 2,
                    '20': 1,
                    '0': 0
                }
            }
        else:
            cmi = calc_cmi_project(data.get('features', []))
        data['cmi'] = cmi
        cmi_por_cod[cod] = cmi

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"[{cod:8s}] Táctico: {cmi['tactico']*100:6.2f}% | Estratégico: {cmi['estrategico']*100:6.2f}% ({cmi['d']}/{cmi['n']})")

    # 2. Agregar CMI consolidado para POS (355 + 416)
    if '355' in cmi_por_cod and '416' in cmi_por_cod:
        c355 = cmi_por_cod['355']
        c416 = cmi_por_cod['416']
        n_pos = c355['n'] + c416['n']
        d_pos = c355['d'] + c416['d']
        av_pos = (c355['n'] * c355['tactico'] + c416['n'] * c416['tactico']) / n_pos if n_pos else 0.0
        ent_pos = d_pos / n_pos if n_pos else 0.0
        cmi_por_cod['POS'] = {
            'tactico': round(av_pos, 4),
            'estrategico': round(ent_pos, 4),
            'n': n_pos,
            'd': d_pos,
            'u': 'funcionalidades',
            'buckets': {
                '100': c355['buckets']['100'] + c416['buckets']['100'],
                '75': c355['buckets']['75'] + c416['buckets']['75'],
                '50': c355['buckets']['50'] + c416['buckets']['50'],
                '20': c355['buckets']['20'] + c416['buckets']['20'],
                '0': c355['buckets']['0'] + c416['buckets']['0']
            }
        }
        print(f"[POS cons] Táctico: {cmi_por_cod['POS']['tactico']*100:6.2f}% | Estratégico: {cmi_por_cod['POS']['estrategico']*100:6.2f}% ({d_pos}/{n_pos})")

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

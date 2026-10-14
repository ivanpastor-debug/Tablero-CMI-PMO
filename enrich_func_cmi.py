"""
Enriquece data_func.json y cada data_func/*.json con el cálculo oficial del
Indicador Táctico y Estratégico de la PMO bajo la Escala CMI por entregable:
  - 100% (1.00): En producción (pct >= 0.999)
  - 75%  (0.75): En UAT del cliente
  - 50%  (0.50): En curso >80% (pct > 0.80)
  - 20%  (0.20): En curso 50-80% (pct >= 0.50)
  - 0%   (0.00): En curso <50% (pct < 0.50)

Indicador Táctico = Promedio del avance de cada funcionalidad bajo la escala
Indicador Estratégico = Funcionalidades al 100% sobre el total (d / n)
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

    if not os.path.exists(index_file):
        print("No se encontró data_func.json en", base_dir)
        return

    with open(index_file, 'r', encoding='utf-8') as f:
        index_data = json.load(f)

    cmi_por_cod = {}

    # 1. Procesar cada archivo individual de detalle
    json_files = glob.glob(os.path.join(data_func_dir, '*.json'))
    for path in sorted(json_files):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        cod = data.get('codigo') or os.path.splitext(os.path.basename(path))[0]
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

    # 4. Sincronizar espejos
    mirror_dirs = [
        r'C:\Users\Usuario1\Documents\PMO INDICADORES\CMI',
        r'C:\Users\Usuario1\Downloads'
    ]
    for md in mirror_dirs:
        if not os.path.exists(md):
            continue
        # copiar data_func.json
        shutil.copy2(index_file, os.path.join(md, 'data_func.json'))
        # copiar data_func/
        target_fnc = os.path.join(md, 'data_func')
        if os.path.exists(target_fnc):
            shutil.rmtree(target_fnc)
        shutil.copytree(data_func_dir, target_fnc)
        print(f"Sincronizado a espejo: {md}")

    print("Enriquecimiento CMI completado con éxito.")

if __name__ == '__main__':
    main()

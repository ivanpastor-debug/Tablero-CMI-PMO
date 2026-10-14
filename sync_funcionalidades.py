"""
Script de sincronización de datos de funcionalidades desde el repositorio Tableros
hacia el Tablero CMI PMO.
"""
import glob
import os
import shutil

def main():
    src_patterns = [
        r'C:\Users\Usuario1\Documents\Optimizaci*n y Control\tableros de proyectos\web',
        r'C:\Users\Usuario1\Documents\Optimizaci*n y Control\tableros-front\web'
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

    dest_dirs = [
        r'c:\Users\Usuario1\Indicadores estra y tac',
        r'C:\Users\Usuario1\Documents\PMO INDICADORES\CMI',
        r'C:\Users\Usuario1\Downloads'
    ]

    files_to_copy = ['data_func.json', 'data_453_cpe.json']
    dirs_to_copy = ['data_func']

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

    print("Sincronización completada con éxito.")
    try:
        import enrich_func_cmi
        print("Ejecutando enriquecimiento CMI de indicadores...")
        enrich_func_cmi.main()
    except Exception as e:
        print(f"Aviso: No se pudo ejecutar el enriquecimiento CMI: {e}")

if __name__ == "__main__":
    main()


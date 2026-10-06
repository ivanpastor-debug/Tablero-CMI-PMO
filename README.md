# Tablero CMI PMO · Indicadores Estratégicos y Tácticos

Tablero de control gerencial y operativo de indicadores para la PMO.

## Publicación en Vercel

Este proyecto está optimizado para publicarse directamente en **Vercel**:
- `index.html`: Punto de entrada principal servido automáticamente por Vercel.
- `vercel.json`: Configuración de URLs limpias para despliegue estático.

### Despliegue con GitHub (Recomendado)
1. Crear un repositorio en GitHub (público o privado).
2. Vincular el repositorio local:
   ```bash
   git remote add origin https://github.com/<tu-usuario>/<tu-repositorio>.git
   git branch -M main
   git push -u origin main
   ```
3. En [Vercel](https://vercel.com):
   - Iniciar sesión con GitHub.
   - Clic en **Add New...** > **Project**.
   - Seleccionar el repositorio y hacer clic en **Deploy**.

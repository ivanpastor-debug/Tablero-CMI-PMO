@echo off
chcp 65001 > nul
echo ======================================================================
echo          TABLERO CMI PMO - ACTUALIZACIÓN INTEGRAL ALINEADA
echo ======================================================================
echo.
echo Este proceso ejecutará en un solo flujo:
echo   1. Actualización operativa y financiera desde los Excel locales (PMO)
echo   2. Sincronización de Épicas y Funcionalidades desde Azure DevOps
echo   3. Enriquecimiento y cálculo oficial de la Escala CMI por funcionalidad
echo   4. Sincronización en las 4 rutas espejo del tablero
echo.
pause

python "c:\Users\Usuario1\Indicadores estra y tac\actualizar_todo.py"

echo.
set /p PUSH="¿Deseas publicar los cambios en GitHub Pages en vivo (s/n)? [s]: "
if /i "%PUSH%"=="n" goto FIN
if /i "%PUSH%"=="no" goto FIN

python "c:\Users\Usuario1\Indicadores estra y tac\actualizar_todo.py" --skip-cmi --skip-azure --push

:FIN
echo.
echo ======================================================================
echo   Proceso finalizado. Puedes cerrar esta ventana.
echo ======================================================================
pause


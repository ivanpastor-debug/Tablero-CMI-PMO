@echo off
chcp 65001 > nul
title PMO - Validador de Ajustes Otra Terminal
cls
echo =====================================================================
echo   AUDITORIA Y MONITOREO DE AJUSTES CONCURRENTES PMO
echo =====================================================================
python "%~dp0validar_ajustes_otra_terminal.py" %*
pause

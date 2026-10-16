---
title: Hub · Tablero de Control Estratégico y Táctico PMO (CMI)
description: Centro de navegación y memoria técnica del Tablero CMI de la PMO para proyectos estratégicos.
tags:
  - pmo
  - cmi
  - control-estrategico
  - control-tactico
  - cuadro-de-mando-integral
  - portafolio
fecha_corte: 2026-10-01
ultima_actualizacion: 2026-10-16
version: "2.5"
url_produccion: https://ivanpastor-debug.github.io/Tablero-CMI-PMO/
repositorio: https://github.com/ivanpastor-debug/Tablero-CMI-PMO.git
---

# 📊 Hub · Tablero de Control Estratégico y Táctico PMO (CMI)

> [!INFO] Resumen Ejecutivo
> Sistema central de supervisión ejecutiva y operativa de la **PMO** para el portafolio de proyectos estratégicos. Integra el seguimiento en vivo de entregables en **Azure DevOps**, la gobernanza contractual bajo la **Escala CMI oficial**, y la supervisión financiera (**EVM**, facturación, costos, márgenes, CPI e ICFF).

---

## 📌 Mapa de Navegación del Módulo CMI

```mermaid
flowchart TD
    Hub["[[00 Hub - Tablero CMI PMO|Hub Central CMI]]"]
    Hub --> M1["[[01 Marco Metodológico Escala CMI y Entregables|01. Marco Metodológico y Escala CMI]]"]
    Hub --> M2["[[02 Matriz Maestra y Portafolio de Proyectos|02. Matriz Maestra de Proyectos]]"]
    Hub --> M3["[[03 Arquitectura y Pipeline Unificado de Datos|03. Arquitectura y Pipeline de Datos]]"]
    Hub --> M4["[[04 Bitácora de Decisiones y Versiones|04. Bitácora de Decisiones (Changelog)]]"]
    
    M2 --> P005["005 - POSITIVA SGDEA"]
    M2 --> P416["416 - CORE POSITIVA"]
    M2 --> P384["384 - CORE FIDUPREVISORA"]
    M2 --> P419["419 - DEPOSITOS JUDICIALES"]
    M2 --> P421["421 - BALÚ"]
    M2 --> P453["453 - MONITOREO CPE"]
    M2 --> P456["456 - INNOVACION AERONAUTICA"]
    M2 --> P348["348 - SGDEA ACUEDUCTO"]
    M2 --> P397["397 - CORE ANDINA"]
```

---

## 🌐 Enlaces Oficiales del Sistema

- **Producción en Vivo (GitHub Pages):** [https://ivanpastor-debug.github.io/Tablero-CMI-PMO/](https://ivanpastor-debug.github.io/Tablero-CMI-PMO/)
- **Repositorio de Código Fuente:** `https://github.com/ivanpastor-debug/Tablero-CMI-PMO.git` (rama `main`)
- **Fecha de Corte Oficial:** `01-Oct-2026`

---

## 📂 Contenido de esta Carpeta

1. [[01 Marco Metodológico Escala CMI y Entregables]]: Reglas de medición por entregable, fórmula del Indicador Táctico y Estratégico, y excepciones metodológicas (453 Casos de Uso, 419 Archivo Local).
2. [[02 Matriz Maestra y Portafolio de Proyectos]]: Fichas de los 9 proyectos oficiales con volumetrías de Azure DevOps, frentes contractuales y datos financieros consolidados.
3. [[03 Arquitectura y Pipeline Unificado de Datos]]: Flujo de sincronización automatizado con `ACTUALIZAR_TODO.bat`, `ACTUALIZAR.py`, enriquecimiento CMI y carga local CORS.
4. [[04 Bitácora de Decisiones y Versiones]]: Registro cronológico de las 16 sesiones de evolución del tablero (Changelog completo).

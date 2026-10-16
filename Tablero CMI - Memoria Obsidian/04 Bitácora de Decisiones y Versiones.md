---
title: Bitácora Histórica de Decisiones y Versiones (Changelog CMI)
tags:
  - pmo
  - cmi
  - changelog
  - bitacora
  - versiones
---

# 📜 Bitácora Histórica de Decisiones y Versiones (Changelog CMI)

> [!NOTE] Registro de Evolución Continua
> Detalle cronológico de las 16 sesiones de trabajo y decisiones arquitectónicas del Tablero CMI PMO.

---

### Sección 16 · Alineación y Automatización Integral (16-oct-2026)
- **Unificación de la Tubería Operativa, Financiera y de Azure DevOps:** Creación del orquestador `actualizar_todo.py` y `ACTUALIZAR_TODO.bat`.
- **Integración en `ACTUALIZAR.py`:** En ejecuciones reales propaga a los 4 espejos y corre `sync_funcionalidades.py`.
- **Carga CORS Inteligente para `file://`:** Función `getJsonUrl` con fallback a GitHub Pages para lectura de datos de Azure DevOps sin bloqueos locales.

### Sección 15 · Estandarización de Nombres Oficiales de Todo el Portafolio (16-oct-2026)
- **Homologación Global:** 005 (`005 - PROYECTO POSITIVA SGDEA 2026 - 3T`), 416 (`416 - PROYECTO DE DESARROLLO Y SOPORTE CORE POSITIVA`), 384 (`384 - PROYECTO CORE FIDUPREVISORA`), 419 (`419- DEPOSITOS JUDICIALES`), 421 (`421 - PROYECTO BALÚ`), 453 (`453 - PROYECTO MONITOREO DE EQUIPOS CPE 2026`), 456 (`456 - PROYECTO INNOVACION AEREONAUTICA CIVIL`), 348 (`348 - PROYECTO SGDEA ACUEDUCTO`), 397 (`397 - PROYECTO CORE ANDINA`).
- **Campos Actualizados:** Chips superiores, tarjetas de portafolio, filas de resumen, flujo financiero, gráfico de costos y callouts.
- **Control Anti-duplicación:** Evaluación `p.name.startsWith(code(p)) || p.id === "POS"` para evitar prefijos numéricos repetidos.

### Sección 14 · Ajustes Oficiales en 453 y 419 (16-oct-2026)
- **453 (Monitoreo CPE):** Retiro de tabla estática redundante `#cpe-cu` y depuración de filtros por foco, dejando exclusivamente el selector metodológico (*Por ejecución* vs *Por compromiso*).
- **419 (Depósitos Judiciales):** Reubicación de la gráfica de certificaciones `#c-419` inmediatamente después de la jerarquía de funcionalidades de Azure DevOps.

### Sección 13 · Medición por Épicas del Portafolio y Limpieza Operativa (16-oct-2026)
- **Gobernanza sobre Épicas:** Definición formal de entregables CMI sobre Épicas en 005 (18), POS (20), 384 (32), 421 (2), 348 (10) y 397 (57).
- **Excepción 419:** Mantiene los 125 entregados sobre 466 del archivo local maestro PMO.
- **Limpieza Ficha Operativa:** Retiro del panel estático *"Escala CMI por frente"* (`#fr-list`), preservando de forma estricta las dos columnas contractuales en 456 (Aeronáutica Civil).
- **Sintaxis:** Eliminación del caracter `}` stray tras el banner resumen CMI.

### Sección 12 · Estandarización Visual Ejecutiva (15-oct-2026)
- Generalización del callout aeroespacial (`PROJ_CALLOUT_META`), badge dinámico (`getBadgeTag`) y bloque financiero enriquecido (`finMini`) a todo el portafolio.

### Sección 11 · Homologación de 397 (Colfondos Core · Andina Seguros) (15-oct-2026)
- Corrección de nombre de cliente: Andina Seguros.
- Medición CMI oficial sobre 57 Épicas (52 en prod · 91,18% est, 97,06% tác) con callout a sus 233 Features de Azure DevOps.
- Integración de libro financiero ($1.450 M contrato, CPI fcst 1,02).

### Sección 10 · Homologación de Casos de Uso (CU) e Hitos en 453 (14-oct-2026)
- Medición oficial exclusiva sobre 45 Casos de Uso (4 entregados · 8,89% est, 30,30% tác).
- Integración de fechas contractuales de focos e iteraciones (`focos_fechas` y `HITOS_453`).

### Sección 9 · Alimentación Dinámica CMI desde Azure DevOps (14-oct-2026)
- Creación de `enrich_func_cmi.py` y cálculo de los 5 buckets PMO (100%, 75%, 50%, 20%, 0%).
- Conmutación dinámica de indicadores tácticos y estratégicos al filtrar subproyectos o variantes.

### Sección 8 · Desglose Jerárquico de Azure DevOps (14-oct-2026)
- Ingesta de árboles jerárquicos: Frente (Epic) → Funcionalidad (Feature) → Historias de Usuario (HU).
- Lazy loading asíncrono de JSON por proyecto (`data_func/{cod}.json`).

### Sección 7 · Integración Financiera 348 y 456 y GitHub Pages (07-oct-2026)
- Incorporación de libros oficiales `Indicadores 348.xlsx` e `Indicadores456.xlsx`.
- Migración permanente de hosting desde Vercel (agotamiento de cuota Hobby) hacia **GitHub Pages**.

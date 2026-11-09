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
> Detalle cronológico de las 32 sesiones de trabajo y decisiones de diseño, metodológicas y operativas del Tablero CMI PMO.

---

### Sección 33 · Ajuste de Indicadores de 421 a 56 Funcionalidades de Producto (06-nov-2026)
- **Alcance Exclusivo de Producto en 421:** Se excluyen las funcionalidades atadas a *Funcionalidades Transversales* (10) y *Automatización_QA Balu* (2) por no corresponder a producto.
- **Universo de Producto:** 56 Funcionalidades en 2 frentes (*Afiliaciones y Novedades*: 29, *Sistema de Recaudo y Cartera*: 27).
- **Indicador Táctico:** **`48,75%`** (12 al 100%, 27 al 50%, 9 al 20%, 8 al 0%).
- **Indicador Estratégico:** **`21,43%`** (12 de 56 al 100% formal en producción).
- **Recálculo del Indicador de Éxito:** **`39,62%`** = 30% Táctico (14,63%) + 40% RQC (19,75%) + 30% Cronograma (5,25%). Hero Card 02 sube a 39,62%.

### Sección 32 · Indicador de Éxito Escenario B.3 y Cronograma Dual 16 Sprints en 419 (06-nov-2026)
- **Fórmula Oficial del Indicador de Éxito 419:** Consolida 40% Funcionalidades 100% en Producción (**28,77%** · 63/219 Azure) + 60% Cronograma Dual B.3 (**36,15%**) = **`33,20%`**.
- **Doble Momento Metodológico:** Momento 1 Linktic (37,91% · HUs en State 8.2 / 08) vs Momento 2 Cliente (34,38% · HUs en State 4 / 20).
- **Pestaña Desplegable de Cronograma (16 Sprints):** Visualización en paralelo de ambos momentos, con meta al corte de 40,63%, brecha de -4,48 pp y cierre final inamovible al 10-Sep-2027 (Sprint 16 UAT con 0d de desviación).
- **Tarjetas en Acordeón:** Tarjeta táctica preservada en 11,96% (sin sumar al éxito y sin nota de archivo local), tarjeta de funcionalidades completa y caja de cronograma con métricas real, meta y brecha.

### Sección 31 · Retiro de Avance Ponderado y Estados Ruidosos en Azure (06-nov-2026)
- Retiro del bloque `Avance ponderado` del encabezado funcional de todos los proyectos para evitar discrepancias con la escala CMI.
- Eliminación de estados de Features (`Active`, `Closed`); la columna se reserva exclusivamente como `Estado / Etapa` para la etapa viva de las HUs.

### Sección 30 · Protocolo de Disparo: Ajuste de Indicadores de 421 a Funcionalidades Azure (06-nov-2026)
- Definición de frase clave de activación: `"Ajusta el indicador tactico y estratégico a funcionalidades del proyecto 421"`.
- Script preparado para conmutar: Estratégico a 26,87% (18/67), Táctico a 53,43% y Éxito a 41,03%.

### Sección 29 · Triada de Control CMI, RQC y Cronograma 10 Releases en 421 (06-nov-2026)
- **Fórmula Indicador de Éxito 421:** **`35,50%`** = 30% Táctico (35,00%) + 40% RQC Contrato (49,37% · 311/630) + 30% Cronograma 10 Releases (17,49% vs Meta 20,00% · Brecha -2,51 pp).
- **Pestaña Desplegable de Cronograma:** 10 Releases contractuales (10% c/u) con avance Azure, desviación en días y semáforos.

### Sección 28 · Generalización de Arquitectura CMI de 2 Tarjetas y Desplegable (05-nov-2026)
- Unificación en todo el portafolio: Hero Grid superior con `01 · Estratégico` y `02 · Éxito`, y acordeón interactivo para `03 · Táctico` y cajas de conciliación.

### Sección 27 · Reestructuración Operativa en 456 (05-nov-2026)
- Dos paneles verticales continuos: *Estatus por fase* (6 entregables con avance y escala) y *Desviación del cronograma* (comparativa línea base vs reprogramado con alerta fiscal 2027).

### Sección 26 · Indicador de Éxito y Pestaña Desplegable CMI en 456 (05-nov-2026)
- Indicador de éxito contractual en **18,00%** frente a meta proyectada de **30,00%** (Brecha de -12,00 pp por Entregable II en Gate 1).

### Sección 25 · Restauración de Carga Asíncrona Azure DevOps y Despliegue Operativo (05-nov-2026)
- Corrección de `ensureFuncIndex()` y `getJsonUrl()` con fallback CORS para `file://`. Despliegue operativo inmediato al abrir cualquier ficha (`mode = "op"`).

### Sección 24 · Corrección en Vistas Operativa y Financiera y Centrado Responsive (05-nov-2026)
- Restauración de `updateTopOpTiles()`. Centrado estructural con `max-width: 1600px; margin: 0 auto;`.

### Sección 23 · Rediseño Visual UX/UI v2 con 3 Indicadores CMI (05-nov-2026)
- Selector numérico estilizado con sangría para `↳ 355 · Positiva Core` y `↳ 416 · Evolutivos`. Hero Grid de 3 indicadores CMI y eliminación de notas interpretativas no ejecutivas.

### Sección 22 · Actualización del Indicador Estratégico en 419 a 80/466 (05-nov-2026)
- Ajuste del CMI oficial según celda `K34` de Excel PMO: 80 certificadas de 466 (**17,17%** estratégico, **11,96%** táctico).

### Sección 21 · Módulo de Bugs y Conciliación Financiera en 419 (04-nov-2026)
- Tablero de 1.627 bugs con tiempos medios de resolución vs ANS y tabla de conciliación comercial ($130M facturados en Sp1-Sp3, Sp4 en mesa técnica).

### Sección 20 · Incorporación de 4 Frentes Contractuales en 348 (04-nov-2026)
- Adición de 4 frentes contractuales de Acueducto a la estructura de entregables.

### Sección 19 · Incorporación de Proyectos Azure DevOps 457, 020 y 461 (04-nov-2026)
- Integración de árboles jerárquicos vivos de Colfondos Arquitectura (457), CNE (020) y Positiva Enlace (461).

### Sección 18 · Corrección Crítica de Indicador Estratégico en 384 y 005 (17-oct-2026)
- 384 ajustado a 1 de 32 épicas al 100% (3,12%). 005 confirmado en 7 de 18 épicas (38,89%).

### Sección 17 · Soporte Nativo para Ejecución Local de Doble Clic (16-oct-2026)
- Fallback automático hacia GitHub Pages en peticiones fetch locales bajo protocolo `file:///`.

---

### Secciones Anteriores (1 a 16)
- **Sección 16:** Unificación de la tubería operativa, financiera y Azure DevOps (`actualizar_todo.py`).
- **Sección 15:** Estandarización de nombres oficiales de todo el portafolio.
- **Sección 14:** Ajuste de nombres oficiales y retiro de tablas redundantes en 453 y 419.
- **Sección 13:** Medición oficial por Épicas del portafolio y excepción 419 (archivo local).
- **Sección 12:** Estandarización visual ejecutiva con callouts y badges de alcance.
- **Sección 11:** Homologación de épicas y alcance funcional en 397 (Colfondos Core / Andina Seguros).
- **Sección 10:** Medición oficial exclusiva sobre 45 Casos de Uso en 453 (Monitoreo CPE).
- **Sección 9:** Alimentación dinámica de indicadores CMI desde Azure DevOps (`enrich_func_cmi.py`).
- **Sección 8:** Desglose jerárquico Frente → Funcionalidad → HU.
- **Sección 7:** Integración financiera 348 y 456 y migración permanente a GitHub Pages.
- **Secciones 1 a 6:** Creación inicial del Tablero CMI PMO, macrofinanciero EVM, escalas y scripts de automatización (`ACTUALIZAR.py`).

---

## 33. Registro de Pestaña Desplegable de Cronograma y Depuración Visual Ejecutiva en 453 (06-nov-2026)
* **Redimensionamiento y Limpieza del Acordeón CMI (`cmiOverviewHTML`):**
  - **Remoción de tabla interna:** Se eliminó la tabla estática incrustada dentro del acordeón `📊 Ver Indicador Táctico y Discriminado del Indicador de Éxito` para 453.
  - **Alineación y Simetría:** Se removió la regla `grid-column: 1/-1` del contenedor `.cmi-exito-box`, permitiendo que la tarjeta de *⏱️ Cumplimiento Cronograma (Peso: 100%)* quede perfectamente redimensionada lado a lado con el *03 · Indicador táctico*, en cuadrícula armónica igual que en 421 y 419.
  - **Métricas Visibles:** Muestra limpiamente los 3 KPIs de alto impacto: Real Entregado (**39,81%**), Meta a la fecha (**55,00%**) y Brecha de Cumplimiento (**-15,19 pp**), complementada con la franja inferior de aportes (Foco A: 32,95%, Foco B: 5,25%, Foco C: 1,61%, Foco D: 0,00%).
* **Depuración del Encabezado en la Ficha de Casos de Uso (`cpe453Card`):**
  - **Eliminación de narrativa repetitiva:** Se retiró el bloque de título y texto redundante (`🗂 453 - PROYECTO MONITOREO DE EQUIPOS CPE 2026 · Casos de Uso y HUs...`).
  - **Remoción de tabla duplicada:** Se quitó la tabla estática que se encontraba insertada dentro de la ficha de CUs, dejando la ficha directamente con el banner CMI oficial, las tarjetas estadísticas y el árbol interactivo de trabajo.
* **Pestaña Desplegable de Cronograma Dedicada (`renderCrono453Collapsible`):**
  - **Estructura Estándar:** Implementada la función `renderCrono453Collapsible()` con `<details class="cmi-accordion" open>`, encabezado con badge de Éxito Ponderado (39,81%), etiqueta de pestaña desplegable y tabla ejecutiva estilizada con clase `tbl-estatus-456`.
  - **Posición Operativa Estratégica:** Se invoca en `renderOpBody` inmediatamente antes de la sección funcional de Azure (`renderFncSection`), brindando una jerarquía visual impecable: primero los Tiles superiores, segundo la Pestaña Desplegable de Cronograma de los 4 Focos, y tercero el árbol interactivo de Casos de Uso y HUs.
* **Sincronización y Validación:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (0 errores de regex, estricto cumplimiento de Regla 4).
  - Sincronización completa en las 4 rutas espejo (`index.html`, `Tablero_CMI_PMO.html`, copia de usuario y copia de descargas).
  - Publicación y despliegue en producción completado en GitHub Pages (`commit 0336fda`).

---

## 34. Registro de Corrección de Aislamiento de Desglose de Cronograma CPE 453 (06-nov-2026)
* **Diagnóstico de Incidencia:**
  - La tabla de cronograma contractual de los 4 Focos de CPE 453 se encontraba incrustada por duplicidad dentro de la función general `funcCard(cod)` bajo el encabezado *"🗂 Funcionalidades por frente · qué HU componen cada una"*, provocando que se renderizara indebidamente en todos los proyectos de Azure DevOps (005, POS, 355, 416, 384, 419, 421, 348, 397).
* **Solución Implementada:**
  - Se eliminó completamente el bloque de tabla de Focos de 453 de la función genérica `funcCard(cod)`.
  - Dicha información quedó aislada y circunscrita **exclusivamente al proyecto CPE 453**, donde se visualiza mediante su pestaña colapsable dedicada `renderCrono453Collapsible()`.
  - La sección *"🗂 Funcionalidades por frente · qué HU componen cada una"* de los demás proyectos recuperó su estructura limpia y nativa: selector de frentes, banner CMI con escala y árbol interactivo de Épicas, Funcionalidades y HUs.
* **Sincronización y Validación:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (0 errores de regex, apego a Regla 4).
  - Sincronización en las 4 rutas espejo y publicación automática en GitHub Pages (`commit 4ac2e77`).

---

## 35. Registro de Transición Global de Indicadores Táctico y Estratégico a Funcionalidades (Features) con Excepción Oficial de Ramos en 416 (06-nov-2026)
* **Gobernanza Operativa sobre Funcionalidades (Features):**
  - Conforme a la directriz PMO, los **Indicadores Tácticos y Estratégicos** de los proyectos pasan a medirse oficialmente sobre las **Funcionalidades (Features)** activas de Azure DevOps (no sobre Épicas), evaluadas bajo la **Escala CMI por entregable**:
    - `100,00%`: En producción o entregado formalmente (`pct >= 0.999`).
    - `75,00%`: En UAT o aprobación del cliente.
    - `50,00%`: En curso >80% (`pct > 0.80`).
    - `20,00%`: En curso 50–80% (`pct >= 0.50`).
    - `0,00%`: En curso <50% (`pct < 0.50`).
  - **Indicador Táctico:** Promedio aritmético de los valores resultantes de la Escala CMI sobre las funcionalidades activas.
  - **Indicador Estratégico:** Proporción de funcionalidades al 100% sobre el total de funcionalidades activas del proyecto ($rac{D}{N}$).
* **Excepción Oficial Exclusiva para Proyecto 416 (Positiva Core Evolutivos):**
  - Se mantiene la medición formal sobre sus **2 Épicas contractuales**, pero expresadas e identificadas en todos los componentes con la unidad oficial **Ramos**:
    - **Total:** `2 Ramos` (*Vida Individual* y *Accidentes Personales*).
    - **Indicador Táctico:** **29,00%**.
    - **Indicador Estratégico:** **0,00%** (0 de 2 Ramos formalizados al 100%).
    - Badge e identificación: `Azure · 2 Ramos` y etiquetas correspondientes (*% avance ramos*, *% cumplimiento ramos*).
* **Consolidación del Portafolio de Proyectos Actualizado:**
  - **005 (POSITIVA SGDEA 2026 - 3T):** 22 Funcionalidades (5 al 100%) $
ightarrow$ Táctico: **28,64%** · Estratégico: **22,73%** (Badge: `Azure · 22 Func.`).
  - **355 (Positiva Core 355):** 83 Funcionalidades activas (6 al 100%) $
ightarrow$ Táctico: **27,35%** · Estratégico: **7,23%** (Badge: `Azure · 83 Func.`).
  - **POS (Consolidado 355 + 416):** 85 Entregables (83 Func. + 2 Ramos, 6 entregados) $
ightarrow$ Táctico: **27,39%** · Estratégico: **7,06%** (Badge: `Azure · 85 Entregables`).
  - **384 (Core Fiduprevisora):** 496 Funcionalidades activas (101 al 100%) $
ightarrow$ Táctico: **48,51%** · Estratégico: **20,36%** (Badge: `Azure · 496 Func.`).
  - **348 (SGDEA Acueducto):** 115 Funcionalidades activas (27 al 100%) $
ightarrow$ Táctico: **28,35%** · Estratégico: **23,48%** (Badge: `Azure · 115 Func.`).
  - **420 (Pólizas de Salud):** 57 Funcionalidades activas (35 al 100%) $
ightarrow$ Táctico: **74,39%** · Estratégico: **61,40%** (Badge: `Azure · 57 Func.`).
  - **421 (Balú):** 56 Funcionalidades de Producto (12 al 100%) $
ightarrow$ Táctico: **48,21%** · Estratégico: **21,43%** (Badge: `Azure · 56 Func.`).
  - **457 (La Equidad):** 49 Funcionalidades (45 al 100%) $
ightarrow$ Táctico: **94,08%** · Estratégico: **91,84%** (Badge: `Azure · 49 Func.`).
  - **020 (Servicios de Analítica):** 7 Funcionalidades (0 al 100%) $
ightarrow$ Táctico: **32,86%** · Estratégico: **0,00%** (Badge: `Azure · 7 Func.`).
  - **461 (Cuentas Claras):** 32 Funcionalidades (0 al 100%) $
ightarrow$ Táctico: **7,19%** · Estratégico: **0,00%** (Badge: `Azure · 32 Func.`).
  - **Proyectos Especiales Preservados:**
    - **419 (Depósitos Judiciales):** Archivo local 466 funcionalidades (80 entregadas $
ightarrow$ 11,96% táctico, 17,17% estratégico).
    - **453 (Monitoreo CPE):** 4 Focos en cronograma (12,50% táctico, 0,00% estratégico, 39,81% éxito ponderado).
    - **456 (Aeronáutica Civil):** 6 Hitos contractuales en 3 fases (24,00% táctico, 16,67% estratégico).
    - **397 (Core Andina):** 57 Épicas contractuales revisadas (97,06% táctico, 91,18% estratégico con 233 Features).
* **Sincronización y Validación:**
  - Script `enrich_func_cmi.py` actualizado para recalcular en base a Features y Ramos en 416.
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (**0 errores de regex**).
  - Sincronización en las 4 rutas espejo y publicación automática en GitHub Pages (`commit 434d56a`).


### Versión 3.20.0 · 09-Nov-2026: Indicador Estratégico Vivo Redimensionable en Aeronáutica (456) y Limpieza de Duplicidades Visuales Operativas
- **Supervisión Contractual Dinámica y Redimensionable en Aeronáutica Civil (456):**
  - El Indicador Estratégico redimensiona dinámicamente su denominador con los hitos vencidos o debidos a la fecha ($N_{fecha} = 2$ de 6 contrato) y su numerador con los hitos entregados formalmente ($D_{real} = 1$).
  - **Indicador Estratégico Real a la fecha:** 50,00% (1 de 2 debidos formalizados).
  - **Meta proyectada a la fecha:** 100,00% (2 de 2 debidos formalizados).
  - **Brecha de cumplimiento:** -50,00 pp (1 hito con desfase en Gate 1).
  - **Etiqueta CMI Hero:** Muestra meta proyectada a la fecha y brecha de cumplimiento.
  - **Doble Conciliación en Acordeón CMI:** Cajas lado a lado para la Conciliación del Indicador Estratégico (Real 50,00%, Meta 100,00%, Brecha -50,00 pp) y la Conciliación del Indicador de Éxito Ponderado (Real 18,00%, Meta 30,00%, Brecha -12,00 pp).
- **Eliminación de Métricas Duplicadas en el Cuerpo Operativo:**
  - Retiro completo de `#op-tiles-top` en `renderOpBody` para todos los proyectos del portafolio (evitando repetición con el CMI Hero superior).
  - Retiro del bloque derecho de métricas numéricas duplicadas en los banners de `funcCard` y `cpe453Card`, preservando el encabezado de trazabilidad y los chips de Distribución en Escala CMI.
- **Validación y Despliegue:**
  - `ACTUALIZAR.py --dry-run` exitoso sin errores de regex.
  - 4 rutas espejo sincronizadas y desplegadas en GitHub Pages (`commit 7cac637`).

- **Ajuste de Medición del Indicador Estratégico en Aeronáutica (456):**
  - Denominador fijado sobre los 6 entregables contractuales.
  - Avance Real a la fecha: 1/6 = 16,67%.
  - Meta Proyectada a la fecha (comprometida / reprogramada): 2/6 = 33,33%.
  - Brecha de Cumplimiento: -16,67 pp (Entregable II pendiente en Gate 1).
  - Desplegado en GitHub Pages (`commit 486cc19`).

- **Retiro de Aclaración Metodológica PMO en Proyecto 456:**
  - Cuadro aclaratorio removido de la sección de funcionalidades para evitar duplicidad de información.
  - Publicado en GitHub Pages (`commit 6ebece2`).

- **Meta Proyectada (30%) y Brecha (-6 pp) en Indicador Táctico de Aeronáutica (456):**
  - Métrica de primer nivel preservada en 24,00%.
  - Debajo del indicador táctico se incluyó la meta proyectada a la fecha (30,00%) y la brecha de cumplimiento (-6,00 pp) con píldora semafórica.
  - Añadida caja de Conciliación del Indicador Táctico en el acordeón junto a las conciliaciones estratégica y de éxito.
  - Publicado en GitHub Pages (`commit b6dfecd`).

- **Ajuste Visual de Ficha Táctica en Aeronáutica (456):**
  - Línea compacta de meta (30,00%) y brecha (-6,00 pp) ubicada debajo de "6 entregables en universo" y "Requiere atención", visible en una sola línea.
  - Publicado en GitHub Pages (`commit cd3fc56`).

- **Conciliación Táctica Desplegable (+) y Limpieza de Fechas de Corte (456):**
  - Conciliación táctica integrada como subpestaña desplegable (`+`/`−`) dentro de la tarjeta `03 · Indicador táctico`.
  - Restaurada la cuadrícula inicial de 3 elementos: Táctico + Conciliación Estratégica + Conciliación de Éxito.
  - Retiradas las etiquetas de "Corte al..." en los encabezados de conciliación.
  - Publicado en GitHub Pages (`commit ad42717`).

- **Ajustes en Cronograma y Sección de Éxito de Balú (421):**
  - Renombrada sección a `🗓️ Desviación del Cronograma`.
  - Oculto % texto numérico de avance, conservando barra visual.
  - Columna Estado homologada a `Entregado` (100%) / `No entregado` (<100%).
  - Nota aclaratoria incluida en la caja de Cumplimiento Cronograma (30%) sobre las 37 funcionalidades de Excel pendientes de correlacionar en Azure.
  - Publicado en GitHub Pages (`commit 8d32dd4`).

- **Actualización Operativa General desde Azure DevOps (09-Nov-2026):**
  - Repositorio fuente `tableros de proyectos` puesto al día mediante `git pull` con los snapshots al **09-nov-2026** generados por GitHub Actions.
  - Sincronizados y recalculados los archivos `data_func.json`, carpeta `data_func/*.json` (16 proyectos) y `data_453_cpe.json` con `enrich_func_cmi.py`.
  - Actualizaciones en indicadores y volumetría viva:
    - **005 (Positiva SGDEA):** Táctico sube a **30,42%**, Estratégico a **25,00%** (6 de 24 funcionalidades en producción al 100%, +1 cerrada vs 5/22).
    - **020 (Servicios de Analítica):** Táctico sube a **58,75%**, Estratégico a **25,00%** (2 de 8 funcionalidades en producción al 100%, +2 cerradas vs 0/7).
    - **355 (Positiva Core 355):** Táctico en **27,02%**, Estratégico en **7,14%** (6 de 84 funcionalidades en producción al 100%).
    - **POS (Consolidado Positiva Core):** Táctico en **27,07%**, Estratégico en **6,98%** (6 de 86 entregables en producción al 100%).
    - **384 (Core Fiduprevisora):** Táctico en **47,97%**, Estratégico en **19,68%** (98 de 498 funcionalidades en producción al 100%).
    - **457 (Portales Digitales La Equidad):** Táctico en **94,31%**, Estratégico en **92,16%** (47 de 51 funcionalidades en producción al 100%, +2 cerradas vs 45/49).
    - **419 (Depósitos Judiciales):** Se mantiene la regla del maestro local (80 de 466 entregables · 17,17% est. / 11,96% tác.), con trazabilidad en Azure actualizada a **195 funcionalidades** (63 en producción · 32,3% cerrado).
    - **348 (Acueducto), 397 (Andina), 416 (Ramos), 420 (Salud), 421 (Balú), 453 (CPE), 456 (Aeronáutica), 461 (CNE):** Mantienen sus valores estables al corte del 09-nov-2026 con HUs y Features sincronizadas.
  - Actualizadas las fechas en el encabezado general (`Act. Operativa: 09-Nov-2026`) y en los metadatos de fuentes de cada proyecto (`PROJ_DATES_META` y `PROJ_CALLOUT_META`).
  - Validación con `ACTUALIZAR.py --dry-run` exitosa (0 errores de regex).
  - Sincronización en las 4 rutas espejo y publicación automática en producción vía GitHub Pages (`commit 85cdd4b`).

- **Ajuste de Release 3 Vencido (07-Nov-2026) en Cronograma Balú (421):**
  - **Causa identificada:** La variable `cutoff421` estaba fijada en `2026-11-06`, por lo que el Release 3 (cierre planeado `2026-11-07`) quedaba fuera del filtro de releases debidos a la fecha (`passed421`).
  - **Corrección dinámica:** Se actualizó `cutoff421` al corte operativo actual (`2026-11-09`), enlazado dinámicamente con `FUNC.proyectos["421"].corte` para que los futuros cortes absorban automáticamente los hitos cumplidos o vencidos.
  - **Redimensión del denominador (Meta Proyectada):** Pasa de **20,00%** (Releases 1 y 2) a **30,00%** (Releases 1, 2 y 3 debidos a la fecha, 10% c/u).
  - **Recálculo de avance real y brecha:**
    - Real Entregado en cronograma: sube a **25,13%** (R1 8,85% + R2 8,64% + R3 7,64%).
    - Brecha de cumplimiento de cronograma: pasa de -2,51 pp a **-4,87 pp** (25,13% - 30,00%).
    - Indicador de éxito 421: sube a **41,75%** (Táctico 30% [14,46%] + RQC 40% [19,75%] + Cronograma 30% [7,54%]).
  - **Marcado semafórico en tabla de Desviación del Cronograma (`tbl-crono-421`):**
    - Release 3 marcado como vencido/incumplido con semáforo crítico `st crit` (fondo rojo `rgba(239,68,68,0.05)`, fecha en rojo `#dc2626`, desviación `+1 d hábil` y `+2 d cal`, estado `No entregado` en rojo crítico).
    - Release 4 ajustado a `Plazo a favor (4 d hábiles)` / `Faltan 5 d`.
    - Fila total y resumen inferior sincronizados a Meta 30,00%, Real 25,13% y Brecha -4,87 pp.
  - Publicado en producción en GitHub Pages (`commit de15219`).

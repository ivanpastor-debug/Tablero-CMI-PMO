# Memoria y Reglas de Trabajo · Tablero de Control Estratégico PMO

## 1. Propósito y Alcance
Este espacio de trabajo contiene el **Tablero de Control Estratégico y Táctico (CMI) de la PMO** para la supervisión ejecutiva y operativa de proyectos estratégicos (005 SGDEA DOCUM, POS 355/416 Positiva Core, 384 Core Fiduprevisora, 419 Depósitos Judiciales, 421, 453, 456 Aeronáutica, 397, 348).

* **Indicador Táctico:** % de avance por funcionalidad/entregable de cada proyecto.
* **Indicador Estratégico:** Entregables al 100% en Azure DevOps (entregados formalmente al cliente).
* **Indicadores Financieros:** Valor contractual, facturación con/sin IVA, recaudo, CPI (FCST y PPTO), ICFF y cronogramas.

---

## 2. Publicación y Despliegue en Vivo
* **Hosting Oficial:** **GitHub Pages** (100% gratuito, sin límites de despliegue ni consumo de cuota mensual).
* **URL Pública en Producción:**  
  👉 **https://ivanpastor-debug.github.io/Tablero-CMI-PMO/**
* **Repositorio Remoto:**  
  `https://github.com/ivanpastor-debug/Tablero-CMI-PMO.git` (rama `main`, visibilidad pública).
* **Archivo raíz:** `index.html` (servido directamente; cuenta con `.nojekyll` para evitar procesamiento innecesario de Jekyll).
* **Nota sobre Vercel:** La cuenta gratuita de Vercel agotó el 100% de su capacidad (Hobby plan quota), por lo que se migró permanentemente a **GitHub Pages** para garantizar disponibilidad continua.

---

## 3. Archivos y Rutas Espejo
Toda modificación debe sincronizarse entre el archivo raíz de despliegue y las copias locales de respaldo:
1. `c:\Users\IvanDarioPastorParra\Indicadores estra y tac\index.html` (Punto de entrada web para GitHub Pages).
2. `c:\Users\IvanDarioPastorParra\Indicadores estra y tac\Tablero_CMI_PMO.html` (Copia local de trabajo).
3. `C:\Users\IvanDarioPastorParra\Documents\PMO INDICADORES\CMI\Tablero_CMI_PMO.html` (Copia maestra del usuario).
4. `C:\Users\IvanDarioPastorParra\Downloads\Tablero_CMI_PMO.html` (Copia de consulta rápida).

---

## 4. Restricciones Críticas y Compatibilidad de Automatización
1. **Script de Automatización `ACTUALIZAR.py`:**
   * Ubicación: `C:\Users\IvanDarioPastorParra\Documents\PMO INDICADORES\CMI\ACTUALIZAR.py`.
   * **REGLA ESTRICTA:** El script busca la declaración de datos mediante la expresión regular:
     `FR_PATTERN = re.compile(r"const FR=(\{[\s\S]*?\});\s*const BOOK416=")`
     Bajo ninguna circunstancia se debe romper la línea de código `const FR=...; const BOOK416=`.
   * Antes de hacer push, siempre verificar con:
     `python "C:\Users\IvanDarioPastorParra\Documents\PMO INDICADORES\CMI\ACTUALIZAR.py" --dry-run`

2. **Integridad Estructural del Tablero:**
   * **Sin cambios en la estructura establecida:**
     * En el proyecto **456 - Aeronáutica**, la sección operativa debe permanecer en **dos columnas lado a lado (`g-2`)**:
       - Columna 1: *Escala CMI por fase* (`#fr-list`).
       - Columna 2: *Desviación del Cronograma* (`table.xl.tbl-crono-456`), ajustada con anchos específicos para evitar barras de desplazamiento horizontal.

---

## 5. Diseño y Funcionalidades de la Interfaz Ejecutiva
* **Header:**
  * Isotipo corporativo PMO con degradado azul tecnológico.
  * Indicador de fecha de corte oficial (`01-Oct-2026`) con punto animado pulsante (`pulse-dot`).
  * Botón interactivo de cambio de tema **Claro ☀️ / Oscuro 🌙** con persistencia en `localStorage` (`cmi-theme`).
* **Buscador en Tiempo Real:**
  * Entrada `#pmo-search` que filtra en vivo las tarjetas de `#sem-op` por código, nombre o cliente.
  * Contador dinámico de resultados (`#search-feedback`).
* **Tipografía:**
  * `Plus Jakarta Sans` para textos, etiquetas y titulares.
  * `JetBrains Mono` para datos tabulares y cifras numéricas.
* **Micro-interacciones:**
  * Elevación suave (`hover lift`) en tarjetas de proyecto (`.op-card`) y chips (`.chip`).
  * Indicadores de estado crítico con latido semafórico suave.

---

## 6. Procedimiento para Nuevos Cambios y Publicación
Para aplicar y publicar cualquier cambio futuro:
```powershell
# 1. Copiar index.html a las rutas espejo
Copy-Item "c:\Users\IvanDarioPastorParra\Indicadores estra y tac\index.html" "c:\Users\IvanDarioPastorParra\Indicadores estra y tac\Tablero_CMI_PMO.html" -Force
Copy-Item "c:\Users\IvanDarioPastorParra\Indicadores estra y tac\index.html" "C:\Users\IvanDarioPastorParra\Documents\PMO INDICADORES\CMI\Tablero_CMI_PMO.html" -Force
Copy-Item "c:\Users\IvanDarioPastorParra\Indicadores estra y tac\index.html" "C:\Users\IvanDarioPastorParra\Downloads\Tablero_CMI_PMO.html" -Force

# 2. Validar con el script de actualización
python "C:\Users\IvanDarioPastorParra\Documents\PMO INDICADORES\CMI\ACTUALIZAR.py" --dry-run

# 3. Guardar y publicar automáticamente en GitHub Pages
git add .
git commit -m "descripcion del cambio"
git push origin main
```
GitHub Pages detectará el commit y actualizará la web pública automáticamente en ~30 segundos.

---

## 7. Registro de Integración Financiera y Vercel (07-oct-2026)
* **Proyecto 348 (SGDEA Acueducto):**
  - Incorporación del libro oficial `Indicadores 348.xlsx` (`Información Financiera/348 - Acueducto/`).
  - Habilitadas las 4 dimensiones financieras: Facturación/Recaudo ($11.031 M Sin IVA / $13.127 M Con IVA, facturado $3.517 M / $4.185 M, recaudo $3.853 M), Costos (PPTO $527 M vs FCST $2.874 M vs Real $1.641 M, CPI fcst 0,61, ICFF 1,51), Costo Personal (49 HC, costo $1.235 M liderado por Desarrollo con 42,13%) y Márgenes (directo real -203,5%, neto real -243,9%).
  - 348 entra plenamente a la lista `FIN` y suma a los totales del portafolio.
* **Proyecto 456 (Aeronáutica Civil):**
  - Reemplazo de preliminares por el libro oficial completo `Indicadores456.xlsx` (`Información Financiera/456- Aeronautica/`).
  - Costos reales actualizados ($346,8 M total, acumulado $273,3 M), curva mensual 2026 ajustada a los datos reales/forecast (Marzo $9,8 M, Abril $25 M, etc.), CPI fcst 0,79, ICFF 1,17, Equipo de 9 HC ($326,6 M), Márgenes completos (directo real -21,8%, neto real -44,0%) y recaudo neto al día ($296,9 M).
* **Ajuste de Vercel (`vercel.json`):**
  - Configuración optimizada con `$schema`, `cleanUrls`, reglas SPA de reescritura hacia `/index.html` y encabezados `Cache-Control: public, max-age=0, must-revalidate` para despliegues instantáneos.

---

## 8. Registro de Integración Desglose Funcional & HUs de Azure DevOps (14-oct-2026)
* **Desglose Jerárquico en la Vista Operativa:**
  - Incorporada la sección interactiva desplegable `🗂 Funcionalidades por frente · qué HU componen cada una` para todos los proyectos con work items en Azure (005/004, 348, 355, 384, 397, 416, 419, 421):
    - Árbol jerárquico: **Frente (Epic) → Funcionalidad (Feature) → Historias de Usuario (HU)**.
    - Columnas detalladas: Estado en Azure / Etapa, Responsable, Funcionalidades con HU, HU activas, HU en producción, Barra de avance ponderado y % exacto.
    - Truncado a 60 HU con botón "Ver todas", alertas de funcionalidades al 100% sin cerrar en Azure y botón para **Descargar CSV completo**.
    - Conmutadores específicos integrados: selector de subproyectos en POS (355 vs 416) y filtros de variantes en 419 (Consolidado vs DEP vs RAMA).
* **Componente Especializado 453 (Monitoreo CPE):**
  - Incorporado el árbol interactivo `🗂 Foco → Iteración → Caso de Uso → HU`:
    - Conmutador metodológico: **⚡ Por ejecución** (HU en su propia iteración real) vs **🎯 Por compromiso** (HU en la iteración de su Caso de Uso).
    - Chips interactivos de filtro por Foco (Todos, Foco A, B, C, D) con hitos comprometidos y semáforos.
    - Doble métrica de avance: por Estado Interno de Casos de Uso (`estados_453`) y por HU atadas en Azure.
* **456 (Aeronáutica):**
  - Conserva su supervisión contractual de 2 columnas (Escala CMI por fase + Desviación del Cronograma) sin alteraciones.
* **Tubería de Datos y Rendimiento:**
  - Datos estáticos servidos en GitHub Pages: `data_func.json`, carpeta `data_func/*.json` y `data_453_cpe.json`.
  - Carga diferida asíncrona (Lazy loading): el `index.html` descarga únicamente el JSON del proyecto seleccionado (~50ms).
  - Manejo amigable para aperturas locales bajo `file://` con aviso informativo que redirige a GitHub Pages.
  - Script auxiliar `sync_funcionalidades.py` para refrescar los datos desde el repositorio local `Tableros` en cualquier momento.

---

## 9. Registro de Alimentación Dinámica de Indicadores CMI desde Azure DevOps (14-oct-2026)
* **Cálculo Oficial PMO por Funcionalidad:**
  - Los indicadores operativos se calculan dinámicamente usando las funcionalidades (`features`) con HU activas de Azure DevOps, evaluadas bajo la **Escala por entregable PMO**:
    - `100,00% ✓`: En producción (`pct >= 0.999`)
    - `75,00%`: En UAT del cliente
    - `50,00%`: En curso >80% (`pct > 0.80`)
    - `20,00%`: En curso 50–80% (`pct >= 0.50`)
    - `0,00%`: En curso <50% (`pct < 0.50`)
  - **Indicador Táctico:** Promedio aritmético del valor asignado a cada funcionalidad bajo la escala.
  - **Indicador Estratégico:** Cantidad de funcionalidades al 100% (en producción) sobre la cantidad total de funcionalidades (`d / n`).
* **Visualización y Reactividad en la Interfaz:**
  - **Tarjetas del Portafolio (`#sem-op`):** Muestran los indicadores calculados con el distintivo verde `Azure` en el encabezado.
  - **Tiles Superiores de la Ficha Operativa (`#op-tiles-top`):** Presentan los indicadores táctico y estratégico con el conteo exacto de funcionalidades y el desglose de entregadas al 100%.
  - **Banner Ejecutivo CMI en el Desglose Funcional:** Incorpora el resumen oficial con doble indicador y la distribución visual de funcionalidades en los 5 cubos de la escala (100%, 75%, 50%, 20%, 0%).
  - **Conmutación Dinámica:** Al cambiar de variante o subproyecto (ej. 355 vs 416 en Positiva, o Consolidado vs DEP vs RAMA en 419), los tiles superiores y el panel CMI recalculan y actualizan los valores en tiempo real.
* **Módulos de Automatización:**
  - Script `enrich_func_cmi.py`: enriquece `data_func.json` y los JSON de `data_func/` con el bloque precalculado `cmi`.
  - Integrado en `sync_funcionalidades.py` para recalcular y sincronizar automáticamente con las carpetas espejo en cada actualización.

---

## 10. Registro de Homologación de Casos de Uso (CU) e Hitos Temporales en 453 (14-oct-2026)
* **Medición Oficial Exclusiva por Casos de Uso (CU) para Proyecto 453:**
  - El proyecto 453 (Monitoreo CPE) no mide sus indicadores frente a Historias de Usuario (HU), sino exclusivamente frente a **Casos de Uso (CU)**:
    - **Total CUs medibles:** 45 CUs (de 49 totales; 4 CU están en levantamiento o excluidos de la medición activa).
    - **CUs entregados formalmente:** 4 CUs en estado interno `19. Entregado` (100% de avance).
    - **Indicador Táctico:** **30,30%** (calculado a partir del promedio del Estado Interno `estados_453` de los 45 CUs medibles).
    - **Indicador Estratégico:** **8,89%** (4 / 45 Casos de Uso entregados al cliente al 100%).
  - **Identidad visual en la interfaz:**
    - Tarjeta del portafolio con badge `Azure · CU` y subtítulos específicos: `% Avance casos de uso` y `% Cumplimiento casos de uso`, con unidad `* Casos de uso`.
    - Tiles superiores con desglose: `Medición por Estado Interno (45 CUs medibles)` y `4 de 45 Casos de Uso entregados (100%)`.
    - Banner Ejecutivo CMI PMO especializado dentro de la ficha de 453 con la distribución de CUs en la escala de entregables.
* **Integración Completa de Fechas Contractuales:**
  - **Nivel Focos:** Incorporación de fechas de Línea Base vs Reprogramadas (`focos_fechas` según `FOCOS_453_20260909.csv`):
    - Foco A: Inicio `2026-02-25` → Reprog `2026-10-24` (Base `2026-07-30`, +87d).
    - Foco B: Inicio `2026-07-01` → Reprog `2026-12-25` (Base `2026-10-15`, +77d).
    - Foco C: Inicio `2026-09-16` → Reprog `2026-10-30` (Base `2026-11-27`, -9d).
    - Foco D: Inicio `2026-10-30` → Fecha `2026-12-30` (Base `2026-12-30`, 0d).
    - Visualización en chips y en la tabla jerárquica con semáforos de cumplimiento.
  - **Nivel Iteraciones:** Integración de fechas de hito por release según `HITOS_453_20260909.csv` (Iteraciones 1 a 7 con releases 1, 2 y 3).
  - **Nivel Casos de Uso:** Nueva columna `Iteración / Fecha` en la tabla de detalle con insignias visuales (ej. `📅 2026-06-02 (Rel. 3)`), vinculando cada CU a la fecha de entrega de su release.
  - **Panel de Supervisión Superior (`#cpe-cu`):** Actualización a hitos de releases por iteración con sus fechas contractuales, CU/HU componentes y semáforos en tiempo real.

---

## 11. Registro de Homologación de Épicas y Alcance Funcional en 397 (Colfondos Core · Andina Seguros) (15-oct-2026)
* **Identidad y Cliente:**
  - Cliente oficial: **Andina Seguros**.
  - Nombre del proyecto en Azure DevOps: **Colfondos Core** (Código PMO: `397`).
  - Se corrigió el cruce de nombres con Previsora en matrices y reportes.
* **Gobernanza de Entregables CMI sobre 57 Épicas:**
  - En Azure DevOps el proyecto cuenta globalmente con **57 Épicas (Epics / Frentes)** y **233 Funcionalidades (Features)**.
  - La unidad oficial de entregable contractual CMI para 397 se mide sobre las **57 Épicas**:
    - **Indicador Táctico:** **97,06%** (promedio ponderado en la escala CMI PMO).
    - **Indicador Estratégico:** **91,18%** (52 de 57 Épicas entregadas formalmente al 100%).
  - **Aclaración destacada permanente:** En la tarjeta `#sem-op`, en los tiles `#op-tiles-top` y en el banner `#func-cmi-summary` se resalta el desglose técnico de **233 Funcionalidades** de Azure DevOps (228 en producción · 97,8% cerrado).
* **Dimensión Financiera Corporativa:**
  - Integración en la tarjeta de portafolio y ficha de proyecto:
    - Valor contrato: $1.450 M (Sin IVA) / $1.725 M (Con IVA) con reactividad ante el conmutador de IVA.
    - Facturación acumulada: $1.392 M (Sin IVA) / $1.656 M (Con IVA) (96,0% de avance).
    - Indicadores EVM: CPI Forecast de 1,02 y CPI Presupuesto de 0,98 con 100% de recaudo esperado neto.
* **Sincronización y Validación:**
  - Matrices regeneradas: `Entregables_y_Entregados_Proyectos_PMO.xlsx` y `.csv`.
  - Archivos espejo sincronizados y verificación exitosa con `ACTUALIZAR.py --dry-run`.
  - Despliegue en producción completado en GitHub Pages.

---

## 12. Registro de Estandarización Visual Ejecutiva para todo el Portafolio (15-oct-2026)
* **Generalización del Diseño Visual Aprobado en 397:**
  - Se extendió a todas las tarjetas de proyecto en `#sem-op` (005, POS, 355, 416, 384, 419, 453, 421, 456, 348, 397) la misma arquitectura visual uniforme:
    1. **Encabezado con Código, Nombre y Subtítulo de Cliente:** subtítulo visible en todos los proyectos (`p.sub`), incluyendo subproyectos 355 y 416.
    2. **Insignia Dinámica de Origen (`getBadgeTag`):** Muestra el alcance exacto de medición de cada proyecto (`Azure · 77 Func.`, `Azure · 87 Func.`, `Azure · 543 Func.`, `Azure · 168 Func.`, `Azure · 66 Func.`, `Azure · 95 Func.`, `Azure · 57 Épicas`, `Azure · 45 CUs`, `Contractual · 6 Hitos`).
    3. **Contenedor Callout Estilizado (`getProjCallout`):** Bloque con degradado aeroespacial y borde celeste sutil que resalta para cada proyecto su alcance, entregables en producción y % cerrado en Azure / contrato.
    4. **Bloque Financiero Enriquecido (`finMini`):** Integra el porcentaje de avance de facturación contractual (`Sin/Con IVA · % av.`) directamente en el subtítulo de "Valor facturado", permitiendo lectura ejecutiva inmediata.
* **Sincronización y Despliegue:**
  - Verificación exitosa de compatibilidad con `ACTUALIZAR.py --dry-run`.
  - Sincronización en las 4 rutas espejo y despliegue automático en GitHub Pages.

---

## 13. Registro de Medición por Épicas del Portafolio, Excepción 419 y Limpieza Operativa (16-oct-2026)
* **Gobernanza de Entregables CMI sobre Épicas / Frentes:**
  - Los entregables principales para los proyectos con trabajo en Azure DevOps se miden contractualmente frente a las **Épicas (Epics / Frentes)**:
    - 005 SGDEA DOCUM: 18 Épicas (7 entregadas · 38,89% estratégico, 50,56% táctico).
    - POS Positiva Core: 20 Épicas (0 entregadas · 0,00% estratégico, 21,85% táctico) con subproyectos 355 (18 Épicas) y 416 (2 Épicas).
    - 384 Core Fiduprevisora: 32 Épicas (1 entregada al 100%: *15 PDI PORTAFOLIO DE INVERSIONES* · 3,12% estratégico, 42,19% táctico).
    - 421 BALÚ: 2 Frentes contractuales (0 entregados · 0,00% estratégico, 35,00% táctico).
    - 348 SGDEA Acueducto: 10 Épicas (1 entregada al 100%: *Assesment de Madurez* · 10,00% estratégico, 25,29% táctico).
    - 397 Colfondos Core: 57 Épicas (52 entregadas · 91,18% estratégico, 97,06% táctico).
  - Todas las tarjetas operativas (`#sem-op`), tiles (`#op-tiles-top`) y banners CMI reflejan esta unidad de gobierno con desglose complementario de Features en el callout.
* **Excepción Oficial Proyecto 419 (Depósitos Judiciales):**
  - Mantiene los indicadores y volumetría oficial del **archivo maestro local PMO**:
    - Entregables: **466 funcionalidades** (125 certificadas por el cliente).
    - **Indicador Estratégico:** **26,82%** (125 / 466).
    - **Indicador Táctico:** **12,01%**.
    - Badge: `Local · 466 Func.`
  - Callout conmutado a la trazabilidad en Azure DevOps: `168 Funcionalidades en Azure` · `60 en prod. · 35,7% cerrado`.
* **Optimización de la Ficha Operativa (`renderOpBody`):**
  - Se retiró el panel y gráfica estática redundante *"Escala CMI por frente"* (`#fr-list`) en todos los proyectos que cuentan con el desglose interactivo de Azure DevOps (`renderFncSection`), dando paso directo a la jerarquía funcional viva.
  - **Preservación estricta de 456 (Aeronáutica Civil):** Mantiene sin cambios su visualización contractual de 2 columnas (`#fr-list` Escala CMI por fase + `table.xl.tbl-crono-456` Desviación del Cronograma) conforme a la Regla 4.
  - Se conservaron los paneles complementarios de 419 (`#c-419` Entregas y certificaciones) y 453 (`#cpe-cu` Casos de uso / releases).
* **Corrección de Sintaxis Visual:**
  - Se eliminó el caracter literal stray `}` que se renderizaba indebidamente tras el banner resumen de la Escala CMI.
* **Validación y Despliegue:**
  - Verificación exitosa sin errores de regex con `python ACTUALIZAR.py --dry-run`.
  - Sincronización en las 4 rutas espejo y despliegue a producción vía GitHub Pages.

---

## 14. Registro de Ajuste de Nombres Oficiales y Optimización Visual en 453 y 419 (16-oct-2026)
* **Proyecto 453 (PROYECTO MONITOREO DE EQUIPOS CPE 2026):**
  - **Nombre oficial actualizado:** Se renombró a `453 - PROYECTO MONITOREO DE EQUIPOS CPE 2026` en todo el tablero (chips, encabezados de tarjeta, fichas operativas y financieras, callout y búsquedas).
  - **Eliminación de tabla redundante de Casos de Uso:** Se retiró el panel estático `#cpe-cu` y su llamada `renderCU(g)`, dado que la información completa y viva se visualiza directamente a través de la conexión con Azure DevOps en el árbol interactivo.
  - **Depuración de filtros dinámicos:** Se removieron los chips de filtro por foco (`Todos los focos`, `Foco A`, `Foco B`, `Foco C`, `Foco D`), manteniendo exclusivamente el conmutador metodológico: **▶ Por ejecución** vs **◆ Por compromiso**.
* **Proyecto 419 (419- DEPOSITOS JUDICIALES):**
  - **Nombre oficial actualizado:** Se renombró a `419- DEPOSITOS JUDICIALES` en todo el tablero.
  - **Reubicación de gráfica de certificaciones:** La gráfica *"Entregas y certificaciones"* (`#c-419`) se ubicó inmediatamente **después** de la tabla jerárquica de *"Funcionalidades por frente · qué HU componen cada una"*, garantizando lectura visual continua de lo general a lo específico.
* **Sincronización y Validación:**
  - Verificación exitosa con `python ACTUALIZAR.py --dry-run`.
  - Sincronización completa en las 4 rutas espejo y publicación automática en GitHub Pages.

---

## 15. Registro de Estandarización de Nombres Oficiales de Todo el Portafolio (16-oct-2026)
* **Homologación Global de Nombres Oficiales de Proyectos:**
  - **005:** `005 - PROYECTO POSITIVA SGDEA 2026 - 3T`
  - **416 / POS:** `416 - PROYECTO DE DESARROLLO Y SOPORTE CORE POSITIVA` (incluyendo su subproyecto 416 y el consolidado POS)
  - **384:** `384 - PROYECTO CORE FIDUPREVISORA`
  - **419:** `419- DEPOSITOS JUDICIALES`
  - **421:** `421 - PROYECTO BALÚ`
  - **453:** `453 - PROYECTO MONITOREO DE EQUIPOS CPE 2026`
  - **456:** `456 - PROYECTO INNOVACION AEREONAUTICA CIVIL`
  - **348:** `348 - PROYECTO SGDEA ACUEDUCTO`
  - **397:** `397 - PROYECTO CORE ANDINA`
* **Campos y Componentes Actualizados:**
  - Chips superiores de navegación (`#pchips`).
  - Tarjetas de portafolio operativo (`.op-card` en `#sem-op`).
  - Filas de la tabla resumen de proyectos (`semName`).
  - Gráfico de flujo contractual *"Del contrato a la caja"* (`#flow` en `renderFlow`).
  - Gráfico comparativo de costos *"Costo real 2026 vs forecast"* (`#c-costport` en `renderCostPort`).
  - Contenedores callout de cada tarjeta (`PROJ_CALLOUT_META`).
  - Aclaración metodológica PMO en la vista funcional de 397 y título de supervisión contractual en 456.
  - Lógica anti-duplicación de código: evaluación de `(p.name.startsWith(code(p)) || p.id === "POS")` para evitar prefijos redundantes (evita `005 · 005 - ...` o `355 / 416 · 416 - ...`).
* **Sincronización y Validación:**
  - Verificación exitosa de compatibilidad con `ACTUALIZAR.py --dry-run` (0 errores de regex).
  - Sincronización en las 4 rutas espejo y despliegue a producción vía GitHub Pages.

---

## 16. Registro de Alineación y Automatización Integral (16-oct-2026)
* **Unificación de la Tubería Operativa, Financiera y de Azure DevOps:**
  - Se unificó el flujo de actualización local mediante el orquestador `actualizar_todo.py` y el ejecutable por lotes `ACTUALIZAR_TODO.bat`:
    1. **Paso 1 (Excel PMO):** Ejecuta `ACTUALIZAR.py` para leer `Consolidado Indicadores PMO*.xlsx`, refrescar la variable `FR` e inyectar indicadores operativos y financieros.
    2. **Paso 2 (Azure DevOps):** Ejecuta `sync_funcionalidades.py` para copiar los árboles jerárquicos (`data_func.json`, carpeta `data_func/*.json`, `data_453_cpe.json`) desde `tableros de proyectos\web`.
    3. **Paso 3 (Enriquecimiento CMI):** Ejecuta `enrich_func_cmi.py` recalculando dinámicamente los indicadores tácticos, estratégicos y buckets CMI para todo el portafolio.
    4. **Paso 4 (Sincronización Espejo):** Propaga automáticamente `index.html` a las 4 rutas espejo del sistema.
    5. **Paso 5 (Publicación Opcional en Producción):** Permite publicar a GitHub Pages con `git add .`, `commit` y `push` automático mediante `--push` o confirmación en consola.
* **Integración Directa en `ACTUALIZAR.py`:**
  - Se modificó `ACTUALIZAR.py` en `C:\Users\IvanDarioPastorParra\Documents\PMO INDICADORES\CMI\ACTUALIZAR.py` para que, en ejecuciones reales (no `--dry-run`), sincronice automáticamente las 4 rutas espejo y llame a `sync_funcionalidades.py`.
* **Carga en Línea Amigable para Visualización Local (`file://`):**
  - Se incorporó en `index.html` la función `getJsonUrl(relPath)` con fallback hacia `https://ivanpastor-debug.github.io/Tablero-CMI-PMO/` gracias al soporte CORS de GitHub Pages (`Access-Control-Allow-Origin: *`).
  - Al abrir el HTML local con doble clic (`file:///...`), el navegador ahora puede cargar e interactuar con el árbol vivo de Épicas, Funcionalidades y HUs sin bloqueos.
* **Sincronización y Validación:**
  - `ACTUALIZAR.py --dry-run` 100% compatible (0 errores).
  - Todas las copias espejo sincronizadas.

---

## 17. Registro de Alineación Operativa con Vercel Principal (Corte 26-oct-2026) e Incorporación del Proyecto 457 (26-oct-2026)
* **Sincronización Integral con el Tablero Operativo Principal (`tableros de proyectos/web`, Corte `2026-10-26`):**
  - Se actualizaron `data_func.json`, todos los JSON en `data_func/*.json` (incluyendo la generación dinámica de `419.json` a partir de `419-DEP.json` + `419-RAMA.json`) y `data_453_cpe.json` al corte oficial `2026-10-26`:
    - **005 (`004` SGDEA Positiva):** 13 Épicas en Azure (3 al 100% · **23,08%** estratégico, **26,15%** táctico), 41 Funcionalidades con HU (7 en prod. · 17,1% cerrado), 169 HU activas.
    - **POS (`355 + 416` Positiva Core):** 20 Épicas (0 al 100% · **0,00%** estratégico, **23,90%** táctico), 89 Funcionalidades en Azure (6 en prod. · 6,7% cerrado). Subproyecto **355**: 18 Épicas (**23,33%** táctico, 82 func., 6 en prod.). Subproyecto **416**: 2 Épicas (**29,00%** táctico, 7 func., 0 en prod.).
    - **384 (Core Fiduprevisora):** 33 Épicas válidas en Azure (1 al 100% · **3,03%** estratégico, **42,42%** táctico), 509 Funcionalidades con HU (92 en prod. · 18,1% cerrado), 5.229 HU activas (2.274 en prod., 83,33% avance ponderado).
    - **419 (Depósitos Judiciales):** Conserva excepción PMO de archivo local (**26,82%** estratégico = `125 / 466` funcionalidades, **12,01%** táctico) y actualiza su desglose vivo V2 en Azure al corte `2026-10-26`: **21 Épicas** (12 DEP + 9 RAMA), **196 Funcionalidades con HU** (`62` en prod. · **31,6% cerrado**) y **1.272 HU activas** (`419` en prod.).
    - **453 (Monitoreo de Equipos CPE 2026):** Actualizado al corte `2026-10-26` aplicando la homologación completa `estados_453` sobre los **74 Casos de Uso totales** (**70 CUs medibles** + 4 en `10. Transversal`): **28 CUs entregados** en estado `19. Entregado` (**40,00%** estratégico = `28 / 70`, **47,39%** táctico), con 332 HU activas (80,46% avance HU).
    - **421 (Balú):** 2 Frentes contractuales (**0,00%** estratégico, **35,00%** táctico), 66 Funcionalidades con HU en Azure (19 en prod. · 28,8% cerrado), 1.019 HU activas (632 en prod., 83,65% avance ponderado).
    - **348 (SGDEA Acueducto):** 10 Épicas contractuales (1 al 100% · **10,00%** estratégico, **25,29%** táctico), 115 Funcionalidades con HU en Azure (25 en prod. · 21,7% cerrado), 2.048 HU activas (223 en prod., 32,46% avance ponderado).
    - **397 (Core Andina):** 57 Épicas contractuales (52 al 100% · **91,18%** estratégico, **97,06%** táctico), 233 Funcionalidades en Azure (228 en prod. · 97,9% cerrado).
* **Validación e Incorporación del Proyecto `457` (`457 - PROYECTO PORTALES DIGITALES INTEGRADOS – LA EQUIDAD`):**
  - **Validación de Captura:** Confirmado al 100%. El proyecto `457` ya cuenta con extracción automatizada vía **Captura Directa** (`pull_azure_capturas_directas.py` y `pull_azure_tasks.py` sobre REST API / WIQL de Azure DevOps), con snapshots históricos desde el `2026-10-22` hasta el `2026-10-26` (`Epic`, `Feature`, `HU`, `Bug`, `Task`).
  - **Integración en el Tablero CMI PMO:** Incorporado en `P`, `FR`, `PROJ_CALLOUT_META`, `applyLiveFuncCmi` y `data_func/457.json`:
    - **Unidad de gobierno:** **5 Épicas** en Azure DevOps:
      1. *Portal de Formación* (`94588`): 16 func., 82 HU, 100% en prod. → Escala CMI **100% ✓**
      2. *Portal Clientes* (`94577`): 12 func., 42 HU, 100% en prod. → Escala CMI **100% ✓**
      3. *Portal Intermediarios* (`94578`): 15 func., 38 HU, 97,89% avance → Escala CMI **50%**
      4. *Transversales* (`149672`): 2 func., 12 HU, 79,17% avance → Escala CMI **20%**
      5. *Nuevas Funcionalidades* (`292522`): 3 func., 109 HU, 74,24% avance → Escala CMI **20%**
    - **Indicador Táctico CMI:** **58,00%** (`(1.0 + 1.0 + 0.5 + 0.2 + 0.2) / 5`).
    - **Indicador Estratégico CMI:** **40,00%** (`2 de 5` Épicas al 100% en producción).
    - **Desglose técnico Azure:** **48 Funcionalidades con HU** (`43 en prod.` · **89,6% cerrado**) y **284 HU activas** (`231 en prod.` · **88,95%** avance ponderado global).
    - **Estado financiero:** Registrado con `opOnly: true` (*Sin libro financiero cargado*), listo para enlazar cuando la PMO incorpore `Indicadores 457.xlsx`.
* **Actualización Dinámica de Rutas de Usuario (`Path.home()`):**
  - Todos los scripts (`ACTUALIZAR.py`, `actualizar_todo.py`, `sync_funcionalidades.py`, `enrich_func_cmi.py`, `ACTUALIZAR_TODO.bat`) utilizan ahora `Path.home()` (`C:\Users\IvanDarioPastorParra`), eliminando rutas fijas del perfil anterior.

---

## 18. Registro de Incorporación del Proyecto 020 (Servicios de Analítica) (29-oct-2026)
* **Proyecto 020 (020 - PROYECTO SERVICIOS DE ANALITICA):**
  - **Cliente y Entorno:** Positiva Compañía de Seguros · Servicios de Analítica.
  - **Modalidad de Ingesta:** Captura directa automatizada desde Azure DevOps (`pull_azure_capturas_directas.py` con `Epic`, `Feature`, `HU`, `Bug` y `Task`), corte oficial `2026-10-29`.
  - **Gobernanza CMI sobre 2 Épicas:**
    1. *OPERACIÓN* (`525431`): 5 funcionalidades, 43 HU activas, 33 en prod. (86,98% de avance) → Escala CMI **50,00%**.
    2. *SOPORTE* (`525428`): 2 funcionalidades, 18 HU activas, 16 en prod. (94,44% de avance) → Escala CMI **50,00%**.
  - **Indicadores Oficiales PMO:**
    - **Indicador Táctico:** **50,00%** (`(0.50 + 0.50) / 2`).
    - **Indicador Estratégico:** **0,00%** (`0 de 2` Épicas al 100% entregadas al cliente).
  - **Desglose Técnico en Azure DevOps:**
    - **7 Funcionalidades:** *Siniestros/Agentes* (16 HU), *Documentación* (15 HU), *Extracciones* (12 HU), *Looker pro* (10 HU), *Gobierno de datos* (4 HU), *Fraude* (3 HU · 100% en prod.), *Gestión* (1 HU).
    - **1 Funcionalidad cerrada en producción:** *Fraude* (14,3% cerrado).
    - **63 HU activas:** 51 en producción (81,0% en producción · 89,52% avance global).
  - **Integración en la Interfaz del Tablero:**
    - Chip interactivo en `#pchips`: `020 - PROYECTO SERVICIOS DE ANALITICA`.
    - Tarjeta operativa `#sem-op` con badge `Azure · 2 Épicas` y callout: `7 Funcionalidades en Azure` · `1 en prod.` · `14,3% cerrado`.
    - Ficha Operativa con árbol jerárquico interactivo completo: Épica → Funcionalidad → HU con sus responsables y descarga en CSV.
    - Estado financiero: Marcado como `opOnly: true` con nota explicativa `finNote`.
  - **Sincronización y Validación:**
    - Verificación exitosa con `python ACTUALIZAR.py --dry-run` (0 errores).
    - Sincronización completa en las 4 rutas espejo y despliegue a producción vía GitHub Pages.

---

## 19. Registro de Ajuste de Etiquetas Financieras (03-nov-2026)
* **Ajuste en la Sección Costos:**
  - Se renombró el indicador `Cumpl. REAL / PPTO` a **`Ejecución REAL/PPTO`** en la tarjeta de costos de todos los proyectos (`costBlock`).
* **Ajuste en Índices de Desempeño EVM (`evmCard`):**
  - En los paneles de **Escenario PPTO** y **Escenario FCST**, se ajustó el numerador de la fórmula del CPI:
    - Antes: `EV · Valor ganado`
    - Ahora: **`EV · Costo total ejecutado`**
* **Validación y Publicación:**
  - Verificación exitosa con `python ACTUALIZAR.py --dry-run` (0 errores).
  - Sincronización en las 4 rutas espejo y despliegue automático en GitHub Pages (`commit 37bbb5b`).

---

## 20. Registro de Incorporación del Proyecto 461 (Cuentas Claras · CNE) (03-nov-2026)
* **Proyecto 461 (461 - PROYECTO CUENTAS CLARAS):**
  - **Cliente y Entorno:** Consejo Nacional Electoral (CNE) · Cuentas Claras 2.0.
  - **Modalidad de Ingesta:** Captura directa automatizada desde Azure DevOps (`HU_461_20261103.csv`), corte oficial `2026-11-03`.
  - **Gobernanza CMI sobre 7 Épicas:**
    1. *Parametrización y Configuración* (`457548`): 7 features, 32 HU activas, 57,72% de avance → Escala CMI **20,00%**.
    2. *Gestión Electoral y Campañas* (`467870`): 5 features, 24 HU activas, 31,91% de avance → Escala CMI **0,00%**.
    3. *Acceso e Identidad (IAM)* (`435992`): 5 features, 18 HU activas, 67,72% de avance → Escala CMI **20,00%**.
    4. *Finanzas y Contabilidad de Campaña* (`487090`): 5 features, 11 HU activas, 22,00% de avance → Escala CMI **0,00%**.
    5. *Declaración Anual de Patrimonio* (`487098`): 5 features, 11 HU activas, 21,00% de avance → Escala CMI **0,00%**.
    6. *Rendición de Cuentas de Campaña* (`487094`): 4 features, 10 HU activas, 17,90% de avance → Escala CMI **0,00%**.
    7. *Transversales* (`467406`): 1 feature, 2 HU activas (1 en prod.), 80,00% de avance → Escala CMI **20,00%**.
  - **Indicadores Oficiales PMO:**
    - **Indicador Táctico:** **8,57%** (`(3 * 0.20 + 4 * 0.0) / 7 = 0.60 / 7`).
    - **Indicador Estratégico:** **0,00%** (`0 de 7` Épicas al 100% entregadas formalmente).
  - **Desglose Técnico en Azure DevOps:**
    - **32 Funcionalidades (Features)** registradas en Azure.
    - **0 Funcionalidades cerradas al 100% en producción**.
    - **108 HU activas** (1 en producción · 43,41% de avance ponderado global · 45 HU omitidas/cerradas).
  - **Integración en la Interfaz del Tablero:**
    - Chip interactivo en `#pchips`: `461 - PROYECTO CUENTAS CLARAS`.
    - Tarjeta operativa `#sem-op` con badge `Azure · 7 Épicas` y callout: `32 Funcionalidades en Azure` · `0 en prod.` · `0,0% cerrado`.
    - Ficha Operativa con árbol jerárquico interactivo completo: Épica → Funcionalidad → HU con sus responsables y descarga en CSV (`data_func/461.json`).
    - Estado financiero: Marcado como `opOnly: true` con nota explicativa `finNote` (*Pendiente cargue de libro financiero*).
  - **Sincronización y Validación:**
    - Verificación exitosa con `python ACTUALIZAR.py --dry-run` (0 errores de regex).
    - Sincronización completa en las 4 rutas espejo y despliegue a producción vía GitHub Pages.

---

## 21. Registro de Auditoría de Bugs, Curva ANS y Conciliación Financiera en 419 (Depósitos Judiciales) (04-nov-2026)
* **Contexto y Gobernanza de Defectos en 419 (Depósitos Judiciales):**
  - Además del control de avance funcional maestro (466 funcionalidades / 125 certificadas), se incorporó en la ficha operativa del proyecto 419 el panel integral de auditoría de defectos (Bugs) con trazabilidad entre Linktic y el cliente (Banco Agrario / Rama Judicial).
  - **Doble Validación en Azure DevOps:** 1.836 bugs auditados en total, diferenciando dos variantes operativas:
    - **Depósitos Judiciales (BAC):** 1.265 bugs (68,9%).
    - **Rama Judicial:** 571 bugs (31,1%).
* **Control de Tiempos de Respuesta vs ANS Contractual (Meta ≤ 3.0 días):**
  - **Tiempo Medio Global:** 15,2 días (Mediana 6,7 días).
  - **Evolución S1 ➔ S7 (Curva de Eficiencia):**
    - Reducción del **78,4%** en el tiempo de resolución: pasando de 25,0 días en Sprint 01 a 5,4 días en Sprint 07.
    - S1: 406 bugs (25,0d promedio · Brecha +22,0d vs ANS · Crítico).
    - S2: 175 bugs (21,4d promedio · Brecha +18,4d vs ANS · Crítico).
    - S3: 309 bugs (13,3d promedio · Brecha +10,3d vs ANS · Crítico).
    - S4: 231 bugs (9,5d promedio · Brecha +6,5d vs ANS · Crítico).
    - S5: 67 bugs (7,8d promedio · Brecha +4,8d vs ANS · Alerta).
    - S6: 197 bugs (6,2d promedio · Brecha +3,2d vs ANS · Alerta).
    - S7: 217 bugs (5,4d promedio · Brecha +2,4d vs ANS · Favorable / Cerca al ANS ≤ 6d).
    - Sin Sprint / Raíz: 225 bugs (16,1d promedio · Brecha +13,1d).
* **Conciliación de bug´s con reportados por Cliente (Rango B59:F63):**
  - Registro auditable del acuerdo comercial por defectos entre Linktic y el Cliente:
    - **Sp1:** 406 bugs Linktic $\rightarrow$ **$35.000.000 COP** (Conciliado y Facturado).
    - **Sp2:** 175 bugs Linktic $\rightarrow$ **$21.000.000 COP** (Conciliado y Facturado).
    - **Sp3:** 309 bugs Linktic vs 188 cliente (69 acordados) $\rightarrow$ **$74.000.000 COP** (Conciliado y Facturado).
    - **Total Liquidado (Sp1 a Sp3):** **$130.000.000 COP**.
    - **Sp4:** 231 bugs Linktic vs 250 cliente $\rightarrow$ Pendiente conciliación (**Mesa Técnica en Curso**).
* **Componentes de Interfaz Incorporados:**
  - `renderBugs419Section()`: 4 KPI tiles superiores (Bugs Totales, Tiempo Medio Global, Meta ANS, Evolución S1➔S7).
  - Gráfica combinada SVG `#c-bugs419`: Barras apiladas de volumen por sprint (azul BAC / púrpura Rama), línea de tendencia de tiempo promedio (ámbar) y línea de meta ANS punteada en rojo (3.0d) con tooltips interactivos (`renderBugs419Chart`).
  - Tabla ejecutiva de Conciliación y Liquidación Financiera (B59:F63).
  - Bloque colapsable con tabla detallada por sprint y semáforos ANS, más fichas de casos testigo certificados en Azure (IDs 502170, 522914, 532666, 539936).
  - Ubicación: Inmediatamente después del desglose funcional y antes de la curva acumulada de entregas y certificaciones (`#c-419`).
* **Sincronización y Validación:**
  - Verificación exitosa con `python ACTUALIZAR.py --dry-run` (0 errores).
  - Sincronización en las 4 rutas espejo y despliegue a producción vía GitHub Pages (`commit 309756b`).

---

## 22. Registro de Actualización del Indicador Estratégico en 419 (Depósitos Judiciales) (05-nov-2026)
* **Actualización del Indicador Estratégico Oficial PMO:**
  - A partir de la actualización global registrada en `Consolidado Indicadores PMO 01102026.xlsx` (hoja `CMI`, celda `K34 = K39/I39`), se ajustó el conteo oficial de entregables cumplidos al 100%:
    - **Antes:** 125 funcionalidades certificadas de 466 $\rightarrow$ **26,82%**.
    - **Ahora:** **80 funcionalidades certificadas de 466** $\rightarrow$ **17,17%**.
  - **Indicador Táctico:** Se mantiene en **11,96%** (promedio aritmético del avance sin seguimiento interno Linktic).
* **Ajustes en Componentes y Sincronizadores:**
  - `enrich_func_cmi.py`: Actualizado bloque 419 con `estrategico: 0.1716738197` (80/466) y `buckets: {'100': 80, '75': 0, '50': 40, '20': 18, '0': 328}`.
  - `ACTUALIZAR.py`: Ajustada la regla de inferencia de entregables para preservar el denominador maestro 466 (`d: 80, n: 466`) y evitar simplificación a 40/233.
  - `Tablero_CMI_PMO.html`:
    - Objeto de proyecto en `P` (`av: 0.1195777351, ent: 0.1716738197, n: 466, d: 80`).
    - Diagnóstico ejecutivo: *"Se han certificado 17,17% de las funcionalidades (80 de 466): avance táctico CMI 11,96%."*
    - Bloque `VAL`: `"419": {src: "CMI!I34 = 11,96% · K34 = 17,17% (80/466)", ...}`.
    - Banner CMI y Aclaración Metodológica: Actualizados a *"80 certificadas / 466 entregables"*.
    - Callout: Actualizado a 63 funcionalidades cerradas en producción de 194 en Azure (`32,5% cerrado`).
* **Sincronización y Validación:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (0 errores).
  - Sincronización completa en las 4 rutas espejo y publicación automática en GitHub Pages.

---

## 23. Registro de Rediseño Visual UX/UI v2 con 3 Indicadores CMI (05-nov-2026)
* **Arquitectura Visual Rediseñada (Mockup de Referencia `Tablero_CMI_PMO_redisenado_v2`):**
  - **Selector Avanzado de Proyectos (`.project-picker-redesign` en `#pchips`):**
    - Sustitución de los chips horizontales básicos por un componente de búsqueda rápida + menú desplegable estilizado (`#project-search-detail` y `#project-select-detail`).
    - **Orden numérico estricto y jerarquía de componentes del 416:** Se ordenan todos los proyectos ascendentemente según su número de código (005 ➔ 020 ➔ 348 ➔ 384 ➔ 397 ➔ 416 ➔ 419 ➔ 421 ➔ 453 ➔ 456 ➔ 457 ➔ 461). Los componentes del proyecto **416 (Positiva Core)** se agrupan de forma subordinada directamente bajo su proyecto padre como `↳ 355 · Positiva Core` y `↳ 416 · Evolutivos`, eliminando la notación redundante "Subproyecto" tanto en el menú desplegable como en los botones segmentados de la ficha.
    - **Sincronización reactiva de fecha de corte operativo:** Se actualizó la fecha oficial base a **04-Nov-2026** (corte vigente de los snapshots en `data_func.json`), integrando en `applyLiveFuncCmi` la actualización dinámica automática del encabezado `#hdr-corte-op` y de cada proyecto en `PROJ_DATES_META`.
    - Filtrado en vivo de proyectos y subproyectos por código, nombre o cliente.
    - Contador reactivo de elementos disponibles.
  - **Encabezado Integral del Detalle de Proyecto (`.project-detail-heading`):**
    - Título ejecutivo del proyecto seleccionado con badges de código y fecha de corte operativo oficial (`getProjDates(p).opDate`).
    - Conservación fluida de selector segmentado de subproyectos (e.g. 355 vs 416 en POS).
  - **Hero Grid de los 3 Indicadores CMI PMO (`.cmi-hero`):**
    - **01 · Indicador estratégico:** Mide el cumplimiento formal de entregables al 100% formalizados ante el cliente (`${pct(strategic)}`), con detalle cuantitativo inferior (`d de n al 100%`) y píldora semafórica de estado (`Favorable`, `En seguimiento`, `Requiere atención`).
    - **02 · Indicador de éxito:** Espacio habilitado y estandarizado para la futura medición por proyecto (`Por definir`), con píldora `Pendiente`.
    - **03 · Indicador táctico:** Avance promedio de funcionalidades / entregables bajo la escala CMI PMO (`${pct(tactical)}`), con universo medible inferior (`n en universo`) y píldora semafórica de estado.
* **Cumplimiento Estricto de Restricciones Negativas del Negocio:**
  - **Exclusión total de notas de interpretación:** No se incluye `.cmi-scale-note` (`Interpretación:...`), manteniendo la visual limpia y directa.
  - **Remoción de aclaraciones discursivas:** Se retiraron los textos descriptivos `.cmi-description` de las tarjetas de indicadores para preservar un aspecto ejecutivo, sin justificaciones metodológicas en bloque.
* **Estilos y Hoja de Ruta Visual (`/* ================= CMI PMO · REDISEÑO UX/UI ================= */`):**
  - Paleta refinada con degradados suaves, bordes limpios, sombras aeroespaciales y adaptación responsive completa (breakpoints en 850px y 620px).
* **Sincronización y Validación:**
  - Validación exitosa con `python ACTUALIZAR.py --dry-run` (0 errores de regex o estructuras).
  - Sincronización verificada en las 4 rutas espejo del sistema.
  - Publicación y despliegue en producción completado en GitHub Pages (`commit 2ca58c2`).

---

## 24. Registro de Corrección en Vistas Operativa y Financiera y Centrado Responsive (05-nov-2026)
* **Diagnóstico de la Incidencia:**
  - Al alternar entre la vista **Operativa** y la vista **Financiera** en la ficha de proyecto, o al cargar datos en vivo desde Azure DevOps (`fncLoad` / `fncChangeSub`), la interfaz no se renderizaba ni actualizaba correctamente.
  - **Causa raíz técnica:** En la aplicación previa del rediseño v2, la función `updateTopOpTiles(cmi, subLabel)` no quedó definida en el JavaScript, provocando una excepción no capturada `ReferenceError: updateTopOpTiles is not defined` en tiempo de ejecución. Esto detenía el flujo del motor de JavaScript, bloqueando la alternancia entre vistas y el refresco reactivo de los componentes.
  - Adicionalmente, el contenedor principal `.wrap` carecía de `margin: 0 auto;`, lo que generaba asimetría visual en pantallas panorámicas.
* **Soluciones Implementadas:**
  - **Restauración de `updateTopOpTiles`:** Se reintegró formalmente la función en el JavaScript con soporte para actualizar simultáneamente tanto los tiles operativos (`#op-tiles-top`) como las tarjetas Hero CMI superiores (`.cmi-hero-card`), contemplando la medición por Casos de Uso (453), Épicas/Frentes y Funcionalidades.
  - **Refresco Reactivo de Tarjetas:** Se integró la invocación de `renderOpCards()` dentro de `applyLiveFuncCmi()` para garantizar que todas las tarjetas del portafolio se recalculen inmediatamente al cargar los snapshots de Azure DevOps.
  - **Centrado y Adaptación Responsive:** Se corrigió `.wrap{max-width:1600px;margin:0 auto;padding:0 26px 36px}` para garantizar distribución y redimensionamiento perfectamente centrados en todas las resoluciones.
* **Sincronización y Despliegue:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (0 errores).
  - Sincronización exacta en las 4 rutas espejo verificada mediante SHA-256.
  - Publicación y despliegue completado en GitHub Pages (`commit d3838dd`).

---

## 25. Registro de Restauración de Carga Asíncrona Azure DevOps y Despliegue Automático Operativo (05-nov-2026)
* **Diagnóstico de la Incidencia:**
  - La sección operativa de cada proyecto no se desplegaba al ingresar al detalle ni al pulsar "Operativa", mostrando mensajes de carga permanentes o pantallas en blanco.
  - **Causa raíz técnica 1 (Funciones asíncronas ausentes):** Durante la refactorización se habían omitido las funciones críticas de carga asíncrona `ensureFuncIndex()` y `getJsonUrl(relPath)` (con soporte de fallback hacia GitHub Pages para entornos locales `file://`). Al invocarse al inicio o dentro de `renderFncSection(p)`, el navegador lanzaba `ReferenceError: ensureFuncIndex is not defined` y `ReferenceError: getJsonUrl is not defined`, bloqueando la descarga de `data_func.json` y el renderizado del árbol de Épicas, Funcionalidades y HUs.
  - **Causa raíz técnica 2 (Estado inicial colapsado):** La variable `mode` iniciaba en `null`, por lo que al entrar a la ficha de cualquier proyecto la sección de detalle permanecía colapsada requiriendo un clic manual explícito.
* **Soluciones Implementadas:**
  - **Restauración de Infraestructura de Datos (`ensureFuncIndex` + `getJsonUrl`):** Se reincorporó `GITHUB_PAGES_BASE`, `getJsonUrl(relPath)`, `_funcInitPromise` y `ensureFuncIndex()`. Ahora `data_func.json` y `data_453_cpe.json` se descargan e hidratan fluidamente tanto en entornos web como locales.
  - **Despliegue Operativo por Defecto (`mode = "op"`):** Se ajustó el valor por defecto de `mode` a `"op"` tanto en la inicialización como en `openProj()`. Al seleccionar cualquier proyecto en el desplegable numérico o desde las tarjetas, su desglose operativo (tiles, frentes, árboles de Azure, Casos de Uso en 453, bugs en 419 o escala en 456) se despliega inmediatamente de forma visible y completa.
* **Sincronización y Despliegue:**
  - Validación exitosa con `python ACTUALIZAR.py --dry-run` (0 errores).
  - Sincronización completa en las 4 rutas espejo verificada por SHA-256.
  - Publicación y despliegue en producción completado en GitHub Pages (`commit 7cd9c34`).

---

## 26. Registro de Implementación de Indicador de Éxito y Pestaña Desplegable CMI para 456 (05-nov-2026)
* **Lógica del Indicador de Éxito Contractual (Proyecto 456 - Aeronáutica Civil):**
  - **Universo Contractual:** 6 entregables distribuidos en 3 fases (Fase I: 30%, Fase II Parte I: 40%, Fase II Parte II: 30%), totalizando el 100% del peso.
  - **Éxito Real Entregado (18,00%):** Suma ponderada de los entregables recibidos formalmente al 100% por el cliente (*Entregable I Fase I: Propuesta metodológica e indicadores · Peso 18%*).
  - **Meta Proyectada a la Fecha de Corte (30,00%):** Suma ponderada de entregables cuya fecha fin en el cronograma ajustado más reciente es menor o igual a la fecha de corte actual (Entregable I al 15/07/2026 [18%] + Entregable II al 23/09/2026 [12%]).
  - **Brecha de Cumplimiento (-12,00 pp):** Diferencia entre lo ejecutado y lo comprometido a la fecha, originada en el *Entregable II de Fase I* (comprometido para el 23-Sep-2026 y que permanece al 50% en Gate 1).
* **Arquitectura Visual Ejecutiva en la Ficha del Proyecto:**
  - **Vista Inicial CMI (`.cmi-hero` con cuadrícula de 2 columnas `.grid-2`):**
    - `01 · Indicador Estratégico`: **16,67%** (1 de 6 entregables al 100% formal).
    - `02 · Indicador de Éxito`: **18,00%** (Ponderación entregada al 100% · Meta proyectada a la fecha: 30,00% · Píldora: `Brecha: -12 pp`).
  - **Sección Desplegable Interactiva (`<details class="cmi-accordion">`):**
    - Contiene la tarjeta destacada de `03 · Indicador Táctico` (**24,00%** bajo Escala CMI PMO).
    - Cuadro compacto de **Conciliación de Indicador de Éxito** con KPIs comparativos: `Real Entregado` (**18,00%** · 1 formalizado), `Meta Proyectada a la fecha` (**30,00%**) y `Brecha de Cumplimiento` (**-12,00 pp** · Alerta Gate 1), suprimiendo tablas y callouts redundantes que ya se exhiben en la vista operativa.
* **Sincronización y Validación:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (0 errores).
  - Sincronización en las 4 rutas espejo verificada por SHA-256.
  - Publicación y despliegue en producción completado en GitHub Pages (`commit 1350db5`).

---

## 27. Registro de Reestructuración Operativa para 456: Estatus por Fase y Desviación del Cronograma (05-nov-2026)
* **Reorganización Estructural (Paneles Apilados Verticalmente):**
  - Se sustituyó la antigua distribución en dos columnas (`g-2`) por dos paneles secuenciales de ancho completo (`.tbl-wrap` en `.section.panel`), garantizando legibilidad total sin compresión horizontal.
* **Panel 1: `Estatus por fase` (antes `Escala CMI por fase`):**
  - **Columnas integradas:**
    1. `Fase / Entregable Contractual`
    2. `Peso` (18%, 12%, 20%, 12%, 8%, 30% · Total 100%)
    3. `Cierre Proyectado` (fechas del último cronograma vigente: 15/07/2026, 23/09/2026, 19/11/2026, etc.)
    4. `% Avance` (expresado numéricamente: 100%, 50%, 0%, 0%, 0%, 0% · Total Ponderado: 24,00%)
    5. *(Visual de Escala CMI)* Columna gráfica sin encabezado de texto (`.col-bar` con barra coloreada según escala)
    6. `Estado` (`100% Producción`, `50% >80% (Gate 1)`, `0% <50% (En curso)`, etc.)
    7. `Desviación a la fecha` (días hábiles transcurridos a la fecha de corte `05-Nov-2026`: Entregable I con `0 d`, Entregable II con `+29 d hábiles`, demás en plazo con `0 d hábiles`).
* **Panel 2: `Desviación del Cronograma`:**
  - Ubicado inmediatamente debajo de `Estatus por fase`.
  - Se retiró la leyenda y el subtítulo previo `(Línea Base vs 05-oct-2026)`.
  - **Columnas normalizadas:**
    1. `Fase / Entregable Contractual`
    2. `Peso`
    3. `Inicio` (fecha inicial del cronograma inicial base)
    4. `Cierre planeado` (fecha de cierre del cronograma inicial base)
    5. `Cierre reprogramado` (fecha de cierre del cronograma vigente o modificado)
    6. `Ajuste en días hábiles` (diferencia en días hábiles entre Cierre Planeado y Cierre Reprogramado)
    7. `Desviación` (días hábiles transcurridos entre fecha de cierre reprogramada y fecha actual)
    8. `Estado` (solo `Estado`, sin `/ CMI`: `Entregado`, `En curso (Gate 1)`, `Pendiente`, `Cruza 2027`, `Desborde fiscal 2027`).
* **Sincronización y Validación:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (0 errores).
  - Sincronización en las 4 rutas espejo verificada por SHA-256.
  - Publicación y despliegue completado en GitHub Pages (`commit 64c207f`).

---

## 28. Registro de Generalización de la Arquitectura CMI de 2 Tarjetas y Desplegable Táctico/Éxito en Todo el Portafolio (05-nov-2026)
* **Unificación de la Visual Superior en Todo el Portafolio (`cmiOverviewHTML`):**
  - Se extendió a todos los proyectos del portafolio (005, 020, 348, 384, 397, POS, 355, 416, 419, 421, 453, 456, 457, 461) la estructura homogénea validada en 456:
    1. **Encabezado Inicial (`.cmi-hero-grid.grid-2`):**
       - **`01 · Indicador Estratégico`**: Particular de cada proyecto con su valor porcentual real, unidad correspondiente (Casos de Uso en 453, funcionalidades locales en 419, épicas/frentes en 005, 348, 384, 397, POS, 421, o entregables en 456) y píldora semafórica.
       - **`02 · Indicador de Éxito`**:
         - *En 456:* **`18,00%`** (Ponderación contractual entregada al 100% formal · Meta a la fecha: 30,00% · Brecha: -12 pp).
         - *En los demás proyectos:* **`Por definir`** (Medición particular según fases y entregables de cada proyecto · Píldora: `Pendiente`).
    2. **Acordeón Desplegable Interactivo (`<details class="cmi-accordion">`):**
       - **`03 · Indicador Táctico`**: Particular de cada proyecto con su valor numérico exacto de avance funcional/escala CMI y el tamaño de su universo medible.
       - **Caja de Conciliación de Indicador de Éxito:**
         - *En 456:* Desglose concreto de `Real Entregado` (18,00%), `Meta Proyectada a la fecha` (30,00%) y `Brecha de Cumplimiento` (-12,00 pp · Alerta Gate 1).
         - *En los demás proyectos:* Estructura homóloga preparada con los 3 bloques KPI (`Real Entregado`: Por definir, `Meta Proyectada`: Por definir, `Brecha`: — · Badge `En homologación PMO`), garantizando que cada proyecto mantenga sus datos individuales sin mezclar la distribución de 456.
* **Sincronización y Validación:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (0 errores).
  - Sincronización en las 4 rutas espejo verificada por SHA-256.
  - Publicación y despliegue completado en GitHub Pages (`commit d5843df`).


---

## 29. Registro de Integración de Triada de Control CMI, RQC y Cronograma de 10 Releases para Proyecto 421 - BALÚ (06-nov-2026)
* **Triada de Control Multidimensional en el Acordeón Desplegable:**
  - Se configuró para el proyecto 421 la arquitectura visual de 3 pilares ejecutivos dentro de `cmiOverviewHTML`:
    1. **03 · Indicador Táctico (Peso: 30%):** **`35,00%`** (Aporte: **`10,50%`** · Medición oficial sobre 2 Frentes Contractuales en escala CMI PMO).
    2. **📋 Cumplimiento RQC · Contrato (Peso: 40%):** **`49,37%`** (Aporte: **`19,75%`** · Cifra oficial del contrato: 311 cumplidos de 630 activos, descontando 283 removidos).
    3. **⏱️ Cumplimiento Cronograma (Peso: 30%):** **`17,49%`** (Aporte: **`5,25%`** · Avance real técnico de HUs en Azure frente a Meta Proyectada al corte: **`20,00%`** correspondiente a los Releases 1 y 2 · Brecha de cumplimiento: **`-2,51 pp`** con 15 HUs en validación UAT).
* **Fórmula Oficial del Indicador de Éxito (Tarjeta 02):**
  - $$	ext{Éxito (421)} = (35,00\% 	imes 0,30) + (49,37\% 	imes 0,40) + (17,49\% 	imes 0,30) = 10,50\% + 19,75\% + 5,25\% = \mathbf{35,50\%}$$.
  - Muestra en Hero Card 02: valor **`35,50%`**, subtítulo `Ponderado: Táctico (30%) · RQC (40%) · Cronograma (30%)` y píldora semafórica `En seguimiento`.
* **Pestaña Desplegable de Desviación del Cronograma (`renderCrono421Collapsible`):**
  - Acordeón interactivo `<details class="cmi-accordion" open>` con la tabla de los **10 Releases a Producción** (peso: 10,0% cada uno), con columnas homólogas a 456:
    - Release 1 (10-Oct · 10% peso): Avance Azure `88,5%` (64,9% Prod) · Desviación: `+18 d hábiles` (`+27 d cal`) · Estado: `🔴 Vencido (15 UAT)`.
    - Release 2 (24-Oct · 10% peso): Avance Azure `86,4%` (45,5% Prod) · Desviación: `+9 d hábiles` (`+13 d cal`) · Estado: `🔴 Vencido (9 UAT)`.
    - Release 3 (07-Nov · 10% peso): Avance Azure `76,4%` (42,9% Prod) · Desviación: `0 d hábiles` (`-1 d cal`) · Estado: `🟡 Vence en 1 día`.
    - Releases 4 a 10 (14-Nov a 20-Mar · 10% peso c/u): Estados `⚪ Futuro (En plazo)` con días a favor.
    - Total consolidado: Peso `100%`, Avance Ponderado Global `75,01%` (50,1% en Prod), Meta Corte `20,00%`, Real `17,49%`, Brecha `-2,51 pp`.
* **Archivo de Correlación Entregado en Carpeta Cronograma:**
  - `Información Financiera/421- BALÚ/Cronograma/Correlacion_Cronograma_vs_Azure_421.xlsx` con 4 hojas: Resumen Ejecutivo, Avance Cronograma (Peso 10%), Correlación Cronograma - Azure, HUs Sin Correlacionar y Features Sin Correlacionar.
* **Sincronización y Despliegue:**
  - Validado con `ACTUALIZAR.py --dry-run` (0 errores). Sincronizado en 4 rutas espejo y publicado en GitHub Pages (`commit 6f78b3b`).

---

## 30. Protocolo de Disparo: Ajuste de Indicadores de 421 a Funcionalidades de Azure
* **Frase Clave de Disparo (Únicamente cuando el usuario lo indique):**
  `"Ajusta el indicador tactico y estratégico a funcionalidades del proyecto 421"`
* **Acciones Inmediatas a Ejecutar:**
  1. **Indicador Estratégico:** Conmutar de `0,00%` (0/2 frentes) a **`26,87%`** (18 de 67 funcionalidades al 100% en producción).
  2. **Indicador Táctico:** Conmutar de `35,00%` (frentes) a **`53,43%`** (promedio aritmético de las 67 funcionalidades bajo la escala PMO: 18 en 100%, 32 en 50%, 9 en 20%, 8 en 0%).
  3. **Recálculo del Indicador de Éxito:**
     $$	ext{Éxito (421)} = (53,43\% 	imes 0,30) + (49,37\% 	imes 0,40) + (17,49\% 	imes 0,30) = 16,03\% + 19,75\% + 5,25\% = \mathbf{41,03\%}$$
     - Tarjeta 02 pasará de **35,50%** a **41,03%**.
     - Aporte táctico en el acordeón pasará de **10,50%** a **16,03%** con subtítulo `67 funcionalidades en universo · Escala CMI Oficial PMO`.
  4. **Archivos a Actualizar y Sincronizar:**
     - `enrich_func_cmi.py`
     - `data_func/421.json` y `data_func.json`
     - `Tablero_CMI_PMO.html` (array `P`, `PROJ_CALLOUT_META`, badge `Azure · 67 Func.`)
     - Ejecutar `ACTUALIZAR.py --dry-run` para validar 0 errores.
     - Sincronizar las 4 rutas espejo y desplegar automáticamente en GitHub Pages / Vercel con `git push origin main`.
  5. **Script de Ejecución Inmediata Preparado:**
     - `scratch/exec_ajuste_421_funcionalidades.py`


---

## 31. Registro de Retiro de Indicador de Avance Ponderado y Estado de Funcionalidades en Desglose Jerárquico Azure (06-nov-2026)
* **Objetivo de la Depuración Metodológica:**
  - Evitar discrepancias o confusiones entre los indicadores oficiales PMO CMI (Táctico y Estratégico) y los cálculos internos de desarrollo en Azure DevOps.
* **Componentes Retirados de Todo el Portafolio en el Espacio `🗂 Funcionalidades por frente · qué HU componen cada una`:**
  1. **Indicador de Avance Ponderado en Encabezado (`.fstrip`):**
     - Se eliminó el bloque de métrica `${stat(fncPct(k.pct_global), "Avance ponderado", "#a855f7")}` de la barra superior.
     - Quedan activos los 4 contadores objetivos: `Frentes`, `Funcionalidades`, `HU en producción` y `Al 100% sin cerrar`.
  2. **Estado en Azure de cada Funcionalidad (`fncTd(1, "")`):**
     - Se limpió el campo `Estado` en todas las filas de funcionalidades (`features`), eliminando estados ruidosos como `Active`, `Closed` y etiquetas de advertencia (`· al 100% sin cerrar`, `· removida con HU vivas`).
     - La columna ahora se rotula `Estado / Etapa` y se reserva exclusivamente para mostrar la **Etapa real de cada Historia de Usuario (HU)** (`4. En Producción`, `3. Pruebas UAT`, `2. Pruebas QA`, `1. Desarrollo`, etc.).
  3. **Depuración de Textos de Ayuda y Leyendas:**
     - Se retiró la frase `· avance ponderado por etapa...` del texto explicativo superior de la tarjeta.
* **Sincronización y Despliegue:**
  - Validado con `ACTUALIZAR.py --dry-run` (0 errores).
  - Sincronizado en las 4 rutas espejo y publicado en producción en GitHub Pages (`commit 4ea559b`).


---

## 32. Registro de Integración de Indicador de Éxito Escenario B.3 y Cronograma de 16 Sprints en Doble Momento para Proyecto 419 (Depósitos Judiciales) (06-nov-2026)
* **Arquitectura del Indicador de Éxito Oficial (Proyecto 419 - Depósitos Judiciales):**
  - Conforme a la definición del usuario, el indicador de éxito consolida dos dimensiones clave (Escenario B.3 Dual Integrado) sin incorporar el indicador táctico:
    1. **📋 Funcionalidades Certificadas por Cliente (Peso: 40,0%):**
       - Mide la totalidad de funcionalidades entregadas al cliente al 100% en producción sobre el universo completo de Features en Azure DevOps (sumando Banco Agrario y Rama Judicial).
       - Universo: **219 Features** (BAC: 157, RAMA: 62).
       - Features al 100% en producción: **63 Features** (BAC: 45, RAMA: 18) $\rightarrow$ **`28,77%`**.
       - Aporte al Éxito: $28,77\% \times 0,40 = \mathbf{11,51\%}$.
    2. **⏱️ Cumplimiento de Cronograma (Opción B.3 Dual Integrado - Peso: 60,0%):**
       - Mide los 16 Sprints del cronograma contractual oficial (`Cronograma_PY_Depositos_Especiales_v3.xlsx`), asignando un peso equitativo de **6,25% a cada sprint** ($16 \times 6,25\% = 100\%$), bajo los **dos momentos metodológicos**:
         - **Momento 1 · Linktic (Entrega Desarrollo a UAT):** HUs en State `8.2 Aprobación por Cliente UAT` y User History `08. Por aprobación del cliente`. Avance ejecutado: **`37,91%`** (Sprints 1 a 6 con 100% desarrollo entregado + Sprint 7 al 6,6%).
         - **Momento 2 · Cliente (Certificación UAT Formal):** HUs en State `4. Cerrado` y User History `20. Aprobado por cliente`. Avance ejecutado: **`34,38%`** (Sprints 1 a 5 con 100% certificados en UAT + Sprint 6 al 50% en pruebas del cliente).
         - **Real Promedio Dual B.3:** $(37,91\% + 34,38\%) / 2 = \mathbf{36,15\%}$.
         - **Meta Proyectada al Corte (06-Nov-2026):** **`40,63%`** (Sprints 1 a 6 completos [37,50%] + 50% Sprint 7 [3,13%]).
         - **Brecha de Cumplimiento:** **`-4,48 pp`** (Sprint 7 reprogramado a 07-Dic-2026 para entrega y 06-Ene-2027 para UAT).
         - Aporte al Éxito: $36,15\% \times 0,60 = \mathbf{21,69\%}$.
  - **Fórmula y Resultado Consolidado Tarjeta 02:**
    $$\text{Éxito (419)} = (28,77\% \times 0,40) + (36,15\% \times 0,60) = 11,51\% + 21,69\% = \mathbf{33,20\%}$$
    - Tarjeta 02 exhibe: valor **`33,20%`**, subtítulo `Ponderado: Funcionalidades 100% (40%) · Cronograma Dual B.3 (60%)` y píldora `En seguimiento`.
* **Tarjetas Discriminadas en el Acordeón Desplegable (`cmiOverviewHTML`):**
  - **03 · Indicador Táctico:** Mantiene el valor vigente de Vercel (**`11,96%`**), aclarando que no suma al éxito, y retirando leyendas/notas sobre el archivo local PMO para mantener la visual ejecutiva (`n funcionalidades en universo`).
  - **Tarjeta Funcionalidades Certificadas por Cliente (Peso: 40%):** Valor **`28,77%`**, con detalle `63 de 219 funcionalidades en prod (BAC: 45 · RAMA: 18)` y badge de aporte `11,51%`.
  - **Caja de Cumplimiento Cronograma Dual B.3 (Peso: 60%):** Aporte `21,69%`, con métricas de `Real Entregado (Dual)` (**`36,15%`**), `Meta Proyectada a la fecha` (**`40,63%`**), `Brecha de Cumplimiento` (**`-4,48 pp`** · Sprint 7 reprogramado) y detalle inferior de los dos momentos (Linktic 37,91% vs Cliente 34,38%).
* **Pestaña Desplegable de Desviación del Cronograma (`renderCrono419Collapsible`):**
  - Acordeón interactivo `<details class="cmi-accordion" open>` que visualiza los **16 Sprints en paralelo**:
    - Columnas generales: `Sprint`, `Peso` (6,25%), `Épicas Azure (BAC / RAMA)`.
    - Bloque **Momento 1 · Linktic** (verde azulado `#0f766e`): Fecha Plan/Reprog, Desviación en días hábiles (+21 d en Sp7), HUs UAT/Prod y Estado.
    - Bloque **Momento 2 · Cliente** (azul `#0284c7`): Fecha Plan/Reprog, Desviación en días hábiles (+23 d en Sp7), HUs en Prod y Estado.
    - Totales consolidados con semáforos, meta proyectada al corte (40,63%), promedio dual (36,15%), brecha (-4,48 pp) y mención de hito contractual final fijo (10-Sep-2027 en Sprint 16 UAT con 0 días de desviación).
* **Entregables y Correlación:**
  - Libro de trabajo completo generado en:
    `Información Financiera/419 - Depósitos Judiciales/Cronograma/Correlacion_Cronograma_vs_Azure_419.xlsx`
    con 5 hojas: *Resumen Ejecutivo 419*, *Correlación Sprints vs Azure*, *Features al 100%*, *Features en Curso o Pendientes* y *HUs por Sprint y Estado*.
* **Sincronización y Validación:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (0 errores de regex o de estructura).
  - Sincronización en las 4 rutas espejo verificada por SHA-256.
  - Publicación y despliegue completado en GitHub Pages (`commit 6895466`).


---

## 33. Registro de Ajuste de Indicadores de 421 a 56 Funcionalidades de Producto (06-nov-2026)
* **Alcance Exclusivo de Producto en Proyecto 421 - BALÚ:**
  - Atendiendo la directriz del usuario, se ajustaron los indicadores operativos (Táctico y Estratégico) a nivel de **Funcionalidades (Features)**, excluyendo estrictamente las funcionalidades que no corresponden a producto:
    - **Épicas Excluidas:**
      - *Funcionalidades Transversales* (10 Features en Azure: IDs 417232, 101755, 180126, 85105, 85107, 85104, 85109, 180688, 85108, 85119).
      - *Automatización_QA Balu* (2 Features en Azure: IDs 417212, 417189).
    - **Frentes de Cara a Producto Incluidos:**
      - *Afiliaciones y Novedades:* **29 Features**.
      - *Sistema de Recaudo y Cartera:* **27 Features**.
    - **Total Universo de Producto:** **56 Funcionalidades**.
* **Resultados de Indicadores CMI bajo Escala PMO:**
  - **Distribución en Cubos CMI:**
    - `100,00% (En Producción)`: **12 Features** (Afiliaciones: 5 · Recaudo: 7).
    - `75,00% (En UAT Cliente)`: **0 Features**.
    - `50,00% (En curso > 80%)`: **27 Features** (Afiliaciones: 15 · Recaudo: 12).
    - `20,00% (En curso 50-80%)`: **9 Features** (Afiliaciones: 6 · Recaudo: 3).
    - `0,00% (En curso < 50%)`: **8 Features** (Afiliaciones: 3 · Recaudo: 5).
  - **Indicador Táctico:** **`48,75%`** ($[12 \times 1,0 + 27 \times 0,5 + 9 \times 0,2 + 8 \times 0] / 56 = 27,3 / 56$).
  - **Indicador Estratégico:** **`21,43%`** ($12 / 56$ funcionalidades formalizadas al 100% en producción).
* **Recálculo del Indicador de Éxito (Tarjeta 02):**
  $$\text{Éxito (421)} = (48,75\% \times 0,30) + (49,37\% \times 0,40) + (17,49\% \times 0,30) = 14,63\% + 19,75\% + 5,25\% = \mathbf{39,62\%}$$
  - Hero Card 02 exhibe: valor **`39,46%`** (subió de 35,50% a 39,46%), subtítulo `Ponderado: Táctico (30%) · RQC (40%) · Cronograma (30%)` y estado `En seguimiento`.
  - Acordeón Desplegable: Tarjeta `03 · Indicador táctico` refleja **`48,75%`** con badge de aporte **`14,63%`** y leyenda inferior `56 funcionalidades en universo · Escala CMI Oficial PMO`.
* **Identidad Visual y Portafolio:**
  - Badge de origen: conmutado a `Azure · 56 Func.` con tooltip *"Medición oficial sobre 56 Funcionalidades de Producto (2 frentes de cara a producto: Afiliaciones y Recaudo)"*.
  - Callout de tarjeta: `56 Funcionalidades de Producto (2 Frentes)` · `12 en prod. · 21,4% cerrado`.
  - Filas resumen: subtítulos actualizados a `% Avance funcionalidades` y `% Cumplimiento funcionalidades`.
* **Sincronización y Validación:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (0 errores de regex).
  - `data_func.json` y `data_func/421.json` enriquecidos y sincronizados.
  - Sincronización en las 4 rutas espejo verificada y publicada en producción en GitHub Pages (`commit 6c1af56`).


## 34. Registro de Conexión 005 Positiva SGDEA 3T, Medición CMI 453 por Focos y Corte al 06-Nov-2026 (06-nov-2026)
* **Desconexión de 005 respecto a 004 y Conexión Directa a 005 Positiva SGDEA New (3T):**
  - Se eliminó el mapeo preliminar que redirigía `005` hacia el dataset legado `004`.
  - Se conectó directamente el tablero y pipeline de datos al proyecto activo **005 Positiva SGDEA New (3T)** (`HU_005_20261106.csv` / `005.json`):
    - **6 Épicas Válidas en Azure DevOps:** *NP - Migración* (100%), *NP - Evolutivos* (70,75%), *Deuda* (73,33%), *Deuda Técnica y Contractual* (41,87%), *Épica de gestión* (sin avance), *Prueba* (sin avance).
    - **Indicador Táctico:** **`23,33%`** ($[1 	imes 1,0 + 2 	imes 0,20 + 3 	imes 0,0] / 6 = 1,4 / 6$).
    - **Indicador Estratégico:** **`16,67%`** ($1 / 6$ épicas al 100% en producción: *NP - Migración*).
    - **Desglose Técnico Callout:** **22 Funcionalidades** en Azure (3T) · **5 en producción** (22,7% cerrado) · 128 HUs.
* **Homologación de Medición CMI para 453 (Monitoreo CPE) sobre sus 4 Focos Contractuales:**
  - En estricto apego a la directriz del usuario, los indicadores operativos de la PMO para el 453 se miden formalmente frente a sus **4 Focos**:
    - **Indicador Estratégico:** Focos cerrados o entregados formalmente al 100% sobre total focos ($D / N$).
      - Resultado: **`0,00%`** ($0 / 4$ focos cerrados).
    - **Indicador Táctico:** Avance de cada foco evaluado bajo la **Escala CMI por entregable**:
      - *Foco A (Agentes de monitoreo):* Avance real 86,69% (> 80%) $
ightarrow$ Escala CMI = **50,00%** (0,50).
      - *Foco B (Gestión analítica):* Avance real 17,50% (< 50%) $
ightarrow$ Escala CMI = **0,00%** (0,00).
      - *Foco C (Encuestas):* Avance real 12,00% (< 50%) $
ightarrow$ Escala CMI = **0,00%** (0,00).
      - *Foco D (Planes e indicadores):* Avance real 0,00% (< 50%) $
ightarrow$ Escala CMI = **0,00%** (0,00).
      - Promedio Aritmético: **`12,50%`** ($(0,50 + 0 + 0 + 0) / 4 = 0,50 / 4$).
    - **Resolución de Visualización Integral de Focos en Árbol Interactivo:**
      - Se corrigió `_cpeRamas` y `_cpeOrdenFocos` en el front-end para que los **4 focos (A, B, C, D)** siempre se inicialicen y visualicen como ramas independientes en la tabla jerárquica de Azure DevOps, evitando que los CUs sin HUs activas caigan erróneamente en `(sin foco)`.
      - Foco A: 44 CUs · 322 HUs · 86,7% avance.
      - Foco B: 1 CU · 0 HUs activas · 17,5% avance CU.
      - Foco C: 31 CUs · 185 HUs · 12,0% avance.
      - Foco D: 0 CUs · 0 HUs · Comprometido para 2026-12-30.
    - **Identidad en Portafolio y Ficha:** Badge `Azure · 4 Focos`, subtítulos `% Avance focos` y `% Cumplimiento focos`, y banner CMI ajustado a medición por foco.
* **Actualización del Portafolio al Corte Diario (06-Nov-2026):**
  - Todos los snapshots de Azure DevOps actualizados a la fecha del día (`2026-11-06`): 005, 453, 421, 384, 355, 416, 419, 348, 397, 420, 457, 020, 461.
  - Sincronización completa de `data_func.json`, carpeta `data_func/*.json` y `data_453_cpe.json`.
  - Validación con `ACTUALIZAR.py --dry-run` exitosa (0 errores de regex, cumplimiento de Regla 4).
  - Snapshot histórico preservado en `Histórico tablero/Tablero_CMI_PMO_20261106_141000.html`.
  - Despliegue en producción completado en GitHub Pages (`commit abf6f88`).


---

## 35. Registro de Incorporación Oficial del Proyecto 420 (Pólizas de Salud) y Medición CMI (06-nov-2026)
* **Incorporación en Portafolio y Datos Operativos:**
  - Proyecto oficial: **420 - PROYECTO PÓLIZAS DE SALUD** (Positiva Compañía de Seguros · Pólizas de Salud).
  - Integrado a la estructura operativa:
    - Agregado en `FR` (12 Épicas operativas bajo la escala CMI PMO).
    - Agregado al listado maestro de proyectos `P` con flag `opOnly: true`.
    - Agregado en `VAL`, `PROJ_CALLOUT_META`, `META_PROJ` y los dos mapeos `keyMap` de Azure DevOps.
  - Generado y sincronizado su dataset `data_func/420.json` y entrada en `data_func.json` a partir del snapshot `HU_420_20261106.csv`.
* **Gobernanza y Resultados de Indicadores CMI:**
  - **Universo de medición:** **12 Épicas** activas en Azure DevOps.
  - **Indicador Estratégico:** **`25,00%`** (3 de 12 Épicas cerradas al 100% en producción).
    - Épicas al 100%: *357080 Contingencia - Continuidad - Errores Integración*, *357556 Desarrollos internos*, *358841 Soportes*.
  - **Indicador Táctico:** **`62,50%`** (Promedio ponderado bajo la escala CMI: 3 épicas al 100% [1,0] + 9 épicas en curso >80% [0,50]: $\frac{3 \times 1,0 + 9 \times 0,50}{12} = \frac{7,5}{12} = 62,50\%$).
    - 9 épicas en rango 80–99% (Escala CMI = 50%): Cuentas médicas (88,9%), Usuarios (94,3%), Gestión red hospitalaria (99,2%), Transversales (91,4%), Atenciones Call Center (93,6%), Configuración (97,1%), Gestión Servicios Médicos (95,8%), Telemedicina MVP (88,0%), Perfil (96,0%).
  - **Desglose Técnico Callout:**
    - Badge: `Azure · 12 Épicas`.
    - Callout: `57 Funcionalidades en Azure` · `35 en prod. · 61,4% cerrado` (617 HU totales, 602 activas, 501 en producción).
* **Sincronización y Validación:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (0 errores de regex, cumplimiento estricto de Regla 4).
  - Sincronización completa en las 4 rutas espejo.
  - Publicación y despliegue completado en GitHub Pages (`commit 6ba08a8`).


---

## 36. Registro de Definición del Indicador de Éxito de 453 (Monitoreo CPE) y Homologación V2 (06-nov-2026)
* **Actualización Integral de la Escala de Avance (Homologación V2):**
  - Se sincronizó la tabla de homologación oficial desde `Homologación estados Azure proyectos V2.xlsx` (hoja `453` en `C:\Users\IvanDarioPastorParra\Documents\Optimización y Control\tableros de proyectos\indicadores\Tablero Operativo\Arquitectura`):
    - **Escala de Casos de Uso (Feature / `estados_453`):**
      - `19. Entregado`: **100,0%** (29 CUs)
      - `18. Despliegue QA a UAT`: **90,0%**
      - `17. Ejecución pruebas QA`: **80,0%** (1 CU)
      - `16. Ajustes desarrollo`: **40,0%** (corregido de 65% a 40% según V2)
      - `15. En desarrollo`: **50,0%** (6 CUs)
      - `13. Aprobado por cliente` / `09. Aprobado por cliente`: **20,0%**
      - `12. Escenarios RNF en revisión` / `08. Escenarios en revisión cliente` / `08. Pdte aprobación`: **17,5%** (1 CU)
      - `11. Escenarios RNF en refinamiento` / `07. Escenarios en refinamiento` / `07. QA-En refinamiento`: **13,5%**
      - `10. Escenarios RNF registrados` / `06. Escenarios registrados` / `06. Rq-En refinamiento`: **15,0%**
      - `09. En elaboración escenarios RNF` / `05. En elaboración Escenarios` / `05. QA-Co creación`: **12,5%** (25 CUs)
      - `04. CU en revisión cliente` / `04. Rq-Co creación`: **10,0%**
      - `03. CU en refinamiento`: **6,0%**
      - `03. QA-Artefacto registrado` / `02. CU registrado en herramienta` / `02. Rq-Artefacto registrado`: **7,5%** (2 CUs)
      - `01. En elaboración doc funcional`: **5,0%**
      - `00. En levantamiento/entendimiento`: **2,5%** (8 CUs)
      - `10. Transversal`: Excluido de medición (4 CUs)
    - **Escala de Historias de Usuario (HU):**
      - `10. En Producción`: **100,0%**
      - `9. Esperando Despliegue UAT-PROD`: **95,0%**
      - `8.2 Aprobación por cliente UAT`: **90,0%**
      - `8.1 Pruebas UAT`: **85,0%**
      - `8. Esperando despliegue de QA a UAT`: **80,0%**
      - `7.2 Aprobación por Cliente a QA` / `Aprobación cliente a QA`: **72,5%** (actualizado de 85% a 72,5%)
      - `7.1 Pruebas QA`: **65,0%** (actualizado de 60% a 65%)
      - `7. Backlog QA`: **57,5%**
      - `6.2 Ajustes Dev`: **45,0%**
      - `6.1 Esperando despliegue Dev a QA`: **50,0%**
      - `6. Desarrollo`: **40,0%**
      - `5. Backlog general`: **30,0%**
      - `4. Refinamiento`: **17,0%**
      - `3. Aprobación de HU y artefactos`: **20,0%**
      - `2. Elaboración HU` / `Elaboración de HU`: **15,0%** (actualizado de 12% a 15%)
      - `1. Levantamiento`: **10,0%**
      - `0. Pendiente Levantamiento`: **5,0%**
      - `0.0 Transversal`: OMITIR (52 HUs)
      - `x. Removido` / `Removido`: EXCLUIR (5 HUs)
* **Medición Oficial del Indicador de Éxito para 453:**
  - Siguiendo la metodología de 456, se pondera el peso asignado en cronograma a cada entregable (**4 Focos**) multiplicando por el porcentaje de avance promedio del campo `% de avance CU`:
    1. **Foco A (Agentes de monitoreo):** Peso **40,00%** · 40 CUs medibles (29 entregados al 100%) · Avance CU: **82,38%** $\rightarrow$ Aporte: **`32,95%`** (Hito reprogramado: 24/10/2026, Vencido).
    2. **Foco B (Gestión analítica):** Peso **30,00%** · 1 CU medible · Avance CU: **17,50%** $\rightarrow$ Aporte: **`5,25%`** (Hito reprogramado: 25/12/2026, En curso).
    3. **Foco C (Encuestas):** Peso **15,00%** · 31 CUs medibles · Avance CU: **10,73%** $\rightarrow$ Aporte: **`1,61%`** (Hito reprogramado: 30/10/2026, Vencido).
    4. **Foco D (Planes e indicadores):** Peso **15,00%** · 0 CUs medibles · Avance CU: **0,00%** $\rightarrow$ Aporte: **`0,00%`** (Hito: 30/12/2026, Sin iniciar).
  - **Fórmula de Éxito Ponderado Total:**
    $$\text{Éxito (453)} = (82,38\% \times 0,40) + (17,50\% \times 0,30) + (10,73\% \times 0,15) + (0,00\% \times 0,15) = 32,95\% + 5,25\% + 1,61\% + 0,00\% = \mathbf{39,81\%}$$
  - **Meta Proyectada al corte (06-Nov-2026):** **`55,00%`** (Foco A [40%] + Foco C [15%] con fechas comprometidas cumplidas al corte).
  - **Brecha de Cumplimiento:** **`-15,19 pp`** (Focos A y C con desviaciones en sus fechas reprogramadas).
* **Componentes de Interfaz Actualizados:**
  - **Hero Card 02 (Indicador de Éxito):** Muestra el valor oficial **`39,81%`**, subtítulo `Ponderado: Focos en Cronograma (100%) × % Avance CU` y píldora `En seguimiento`.
  - **Acordeón Desplegable:** Integra el bloque ejecutivo de conciliación con Real (39,81%), Meta (55,00%), Brecha (-15,19 pp) y la tabla completa de los 4 Focos similar a `tbl-estatus-456`.
  - **Ficha Operativa de 453 (`cpe453Card`):** Incorpora el panel superior *"⏱️ Desviación y Cumplimiento del Cronograma por Foco Contractual"* y actualiza el árbol interactivo de CUs y HUs con los porcentajes de la Homologación V2.
  - **Callout de Tarjeta:** Actualizado a `4 Focos en Cronograma · 76 Casos de Uso` · `29 CUs al 100%` · `39,8% éxito · 12,5% táctico`.
* **Sincronización y Despliegue:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (0 errores de regex, estricto apego a Regla 4).
  - Sincronización completa en las 4 rutas espejo y archivos de datos `data_func.json` y `data_453_cpe.json`.
  - Publicación y despliegue en producción completado en GitHub Pages (`commit 458e0ef`).

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

---

## 36. Registro de Indicador Estratégico Vivo Redimensionable en Aeronáutica (456) y Eliminación de Duplicidades Visuales Operativas (09-nov-2026)
* **Indicador Estratégico Vivo y Redimensionable a la Fecha en Aeronáutica Civil (Proyecto 456):**
  - **Lógica de redimensionamiento contractual:**
    - El denominador se redimensiona automáticamente conforme se cumpla la fecha contractual de entrega de los hitos ($N_{fecha}$, hitos con `date <= corte`).
    - El numerador se alimenta conforme se formalicen entregas al 100% ($D_{real}$, hitos cumplidos formalmente).
  - **Métricas al corte actual (`2026-11-09`):**
    - Hitos debidos a la fecha ($N_{fecha}$): **2 hitos** (Entregable I y Entregable II de Fase I vencidos al 15-Jul y 23-Sep).
    - Hitos entregados al 100% ($D_{real}$): **1 hito** (Entregable I formalizado).
    - Hitos totales del contrato ($N_{total}$): **6 hitos**.
    - **Indicador Estratégico Real a la fecha:** $\frac{1}{2} = \mathbf{50,00\%}$ (1 de 2 entregables debidos a la fecha).
    - **Meta proyectada a la fecha:** $\mathbf{100,00\%}$ (2 de 2 entregables debidos formalizados).
    - **Brecha de cumplimiento:** $\mathbf{-50,00\text{ pp}}$ (1 entregable con desfase en Gate 1).
    - **Indicador de Éxito Ponderado Contractual:** Real **18,00%**, Meta **30,00%**, Brecha **-12,00 pp**.
    - **Indicador Táctico:** **24,00%** (18% × 1.0 + 12% × 0.50).
  - **Componentes CMI actualizados en la Ficha de 456:**
    - **Hero Card `01 · Indicador estratégico`:** Valor principal `50,00%` con etiqueta inferior reactiva:
      `1 de 2 entregables a la fecha (1 de 6 contrato) · Meta proyectada a la fecha: 100,00% | Brecha: -50,00 pp`.
    - **Acordeón CMI (`📊 Ver Indicador Táctico y Discriminado del Indicador de Éxito`):**
      - **⏱️ Conciliación Indicador Estratégico:** Píldoras con Real 50,00%, Meta 100,00% y Brecha -50,00 pp.
      - **🎯 Conciliación Indicador de Éxito:** Píldoras con Real 18,00%, Meta 30,00% y Brecha -12,00 pp.
    - **Tarjeta de Portafolio (`#sem-op`):** Refleja `50,00%` estratégico, callout `Contractual · 1/2 Hitos a la fecha` y subtítulo con avance de hitos y éxito ponderado.
* **Eliminación de Duplicidades Visuales en Todo el Portafolio:**
  - **Retiro de `#op-tiles-top` en `renderOpBody`:** Se eliminaron las tarjetas estáticas/redundantes superiores del cuerpo operativo en todos los proyectos del portafolio (que repetían el Indicador Táctico y Estratégico ya presentados en el CMI Hero).
  - **Limpieza del Banner CMI en Desglose Funcional (`funcCard` y `cpe453Card`):** Se removió el bloque derecho de métricas numéricas duplicadas ("Indicador Táctico" e "Indicador Estratégico"), manteniendo intacto el encabezado de trazabilidad y los chips de Distribución en Escala (100%, 75%, 50%, 20%, 0%).
* **Sincronización, Compatibilidad y Despliegue:**
  - Validación con `ACTUALIZAR.py --dry-run` exitosa (**0 errores de regex**, Regla 4 estrictamente intacta).
  - Sincronización completa en las 4 rutas espejo del sistema.
  - Snapshot histórico guardado en `Histórico tablero/Tablero_CMI_PMO_20261109_085241.html`.
  - Despliegue en producción completado en GitHub Pages (`commit 7cac637`).

* **Ajuste y Clarificación de la Fórmula del Indicador Estratégico en 456:**
  - El denominador permanece constante sobre el **universo contractual completo de 6 entregables** ($N_{total} = 6$).
  - **Avance Real a la fecha:** $\frac{1}{6} = \mathbf{16,67\%}$ (1 entregable formalizado al 100%: Entregable I Fase I).
  - **Meta Proyectada a la fecha:** $\frac{2}{6} = \mathbf{33,33\%}$ (2 entregables con fecha comprometida/reprogramada debida al corte: Entregables I y II al 15-Jul y 23-Sep).
  - **Brecha de Cumplimiento:** $16,67\% - 33,33\% = \mathbf{-16,67\text{ pp}}$ (1 entregable pendiente con desfase en Gate 1).
  - Visualización en CMI Hero: `1 de 6 entregables formalizados (16,67%) · Meta proyectada a la fecha: 33,33% (2/6 hitos) | Brecha: -16,67 pp`.
  - Caja de Conciliación en Acordeón: Real 16,67%, Meta Proyectada 33,33%, Brecha -16,67 pp.

* **Retiro de Aclaración Metodológica PMO en Proyecto 456:**
  - Se removió el cuadro informativo secundario de "Aclaración Metodológica PMO" en la sección de funcionalidades del proyecto 456, manteniendo limpio el encabezado del proyecto sin redundancias.

* **Integración de Meta Proyectada a la Fecha y Brecha en Indicador Táctico de Aeronáutica (456):**
  - **Métrica Principal Preservada en Primer Nivel:** Se mantiene el avance real oficial de **24,00%** (18% × 100% Entregable I + 12% × 50% Entregable II).
  - **Meta Proyectada a la fecha:** **30,00%** (Fase I debida al 23-Sep: 18% + 12% = 30%).
  - **Brecha de Cumplimiento:** **-6,00 pp** (o 6,00% de desfase correspondiente al 50% restante del Entregable II en Gate 1).
  - **Visualización en CMI Hero (`03 · Indicador táctico`):**
    `Avance ponderado Fase I · Meta proyectada a la fecha: 30,00%` con píldora semafórica `Brecha: -6,00 pp`.
  - **Visualización en Portafolio Primer Nivel (`#sem-op`):**
    - Métrica táctica: **24,00%**.
    - Subtítulo KPI: `Meta: 30,0% · Brecha: -6,0 pp`.
    - Callout: `Táctico: 24,0% · Meta: 30,0% · Brecha: -6,0 pp`.
  - **Caja de Conciliación en Acordeón CMI:** Añadida la sección `📊 Conciliación Indicador Táctico (Avance Ponderado)` con Real 24,00%, Meta Proyectada 30,00% y Brecha -6,00 pp.

* **Ajuste Visual de la Ficha Táctica en Aeronáutica (456):**
  - Se restauró la línea estándar en `cmi-bottom` con: `6 entregables en universo · Escala CMI Oficial PMO` y la píldora `Requiere atención`.
  - Inmediatamente debajo, en el espacio blanco disponible, se ubicó una línea compacta y sutil (`font-size: 9.5px`) que en una sola línea presenta: `Meta proyectada a la fecha: 30,00%` junto a su píldora semafórica `Brecha: -6,00 pp`, logrando que toda la información se visualice sin saturar ni desplazar componentes.

* **Conciliación Táctica Desplegable (+) y Limpieza de Fechas de Corte en 456:**
  - **Subpestaña Desplegable en Tarjeta Táctica:** La conciliación detallada del Indicador Táctico (Real 24,00%, Meta 30,00%, Brecha -6,00 pp) se integró directamente como un acordeón interno interactivo (`+`/`−`) dentro de la tarjeta `03 · Indicador táctico`.
  - **Restauración de la Visual Inicial del Acordeón CMI:** El cuerpo del acordeón vuelve a su cuadrícula original de 3 tarjetas lado a lado:
    1. `03 · Indicador táctico` (con su subpestaña desplegable `+`).
    2. `⏱️ Conciliación Indicador Estratégico (Hitos Contractuales)`.
    3. `🎯 Conciliación Indicador de Éxito (Ponderación Contractual)`.
  - **Retiro de Fechas de Corte en Encabezados:** Se retiraron las etiquetas estáticas de fecha de corte (`Corte al...`) en todas las cajas de conciliación, dado que la vigencia temporal se infiere directamente de la fecha de última actualización operativa y contractual del proyecto.

* **Ajustes en Cronograma y Sección de Éxito de Balú (Proyecto 421):**
  - **Título Limpio de Cronograma:** Se renombró la sección a `🗓️ Desviación del Cronograma` (retirando la extensión de los 10 releases).
  - **Visualización de Avance Simplificada:** Se ocultó el porcentaje de texto numérico de avance en Azure, conservando visible la barra gráfica de avance ponderado (`col-bar`).
  - **Columna de Estado Homologada:** Se ajustó la columna a `Estado` con valores binarios normativos:
    - `Entregado` (verde) para funcionalidades/releases con 100% formalizado (Release 9).
    - `No entregado` (rojo/amarillo) para funcionalidades/releases con avance menor al 100% (Releases 1 al 8 y 10).
  - **Nota Aclaratoria en Cumplimiento Cronograma (Peso: 30%):** Se añadió en la caja de conciliación del Indicador de Éxito:
    *«ℹ️ Nota aclaratoria: El cumplimiento del cronograma se evalúa contra el archivo Excel debido a las 37 funcionalidades pendientes de correlacionar en Azure.»*


## 41. Registro de Actualización Operativa General desde Azure DevOps (09-nov-2026)

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


## 42. Registro de Ajuste de Release 3 Vencido en Cronograma Balú 421 (09-nov-2026)

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


## 43. Registro de Conciliación de Cronograma Balú 421 con Cronograma_BALU_2026_ y Matriz de Correlación (09-nov-2026)

- **Auditoría Exhaustiva de Cronograma_BALU_2026_.xlsx:**
  - El nuevo libro oficial integra por primera vez los dos frentes funcionales del proyecto: **Afiliaciones y Novedades (AyN)** (838 filas) y **Sistema de Recaudo y Cartera (RyC)** (1.015 filas).
  - La planeación de 10 Releases de despliegue a producción combina entregables de ambos frentes a partir de Release 4:
    - **Release 1 (10/10/2026):** AyN (Independientes Internos Medicina ind/masivo, Certificados especiales, Normalización I1).
    - **Release 2 (24/10/2026):** AyN (Certificados masivos Funcionario/Empleador).
    - **Release 3 (07/11/2026):** AyN (Actualizaciones sedes masivas).
    - **Release 4 (14/11/2026):** AyN (Recicladores, Voluntarios, Tipos doc, Y1, E1) + RyC (Cartera preventiva, Consulta Cotizantes/Aportantes).
    - **Release 5 (28/11/2026):** AyN (Carnés masivos Funcionario/Empleador).
    - **Release 6 (12/12/2026):** AyN (PPL, Gestores de paz, Cotizante 76, Norma 1641).
    - **Release 7 (23/01/2027):** AyN (Excepciones, Retroactivas, Liquidación, Pólizas, E2, E3) + RyC (Recobros Marcación/Reportes, Validación PILA LOG).
    - **Release 8 (20/02/2027):** AyN (Histórico actualizaciones, Permanencias, Retiro empleador) + RyC (Procesamiento 1% Fase 2).
    - **Release 9 (06/03/2027):** AyN (Novedades PILA permanentes VSP/VPC y transitorias).
    - **Release 10 (20/03/2027):** AyN (Módulo retiro independiente) + RyC (No Vinculados, Constitución de mora, Estado de cuenta).
- **Generación de la Nueva Matriz de Correlación Oficial (Matriz_Correlacion_Cronograma_BALU_vs_Azure_2026.xlsx):**
  - Ubicación física: Información Financiera\421- BALÚ\Cronograma\Matriz_Correlacion_Cronograma_BALU_vs_Azure_2026.xlsx (copiada también a Downloads\).
  - Consta de 4 hojas analíticas estructuradas:
    1. Resumen Ejecutivo: Métricas globales, triada CMI de Balú (Táctico 30% [48,21%], RQC 40% [49,37%], Cronograma 30% [25,13%], Indicador de Éxito 41,75%), resumen de correlación (46 ítems entregables vs 68 features en Azure) y estado de los 10 releases.
    2. Releases vs Azure: Mapeo exhaustivo de los 46 ítems de cronograma contra ID de Feature en Azure, Título, Estado, % Avance y Observaciones de correlación.
    3. Pendientes y Brechas: Detalle de 12 brechas críticas (bloqueos cliente, firmas pendientes, consultas normativas MinSalud/Positiva).
    4. Features Azure DevOps: Censo completo de las 68 Features de Azure (56 de cara a producto + 12 transversales/QA).
- **Actualización del Tablero CMI (Tablero_CMI_PMO.html):**
  - Se actualizaron los alcances de RELEASES_421 para reflejar la integración de AyN y RyC.
  - En 
enderCrono421Collapsible() se actualizaron los textos de cada release detallando los entregables de ambos frentes y la fila total de 10 releases integrados.
  - Se actualizó la nota aclaratoria:
    *«ℹ️ Nota aclaratoria: El cumplimiento del cronograma se evalúa contractualmente sobre los 10 Releases integrados (Afiliaciones y Novedades + Recaudo y Cartera) del archivo Cronograma_BALU_2026_, correlacionados contra Azure DevOps en la Matriz de Correlación BALÚ 2026 (46 ítems entregables vs 68 features en Azure).»*
- **Validación y Despliegue:**
  - erify_integrity.py OK (764 backticks pares).
  - ACTUALIZAR.py --dry-run OK (0 errores).
  - Sincronización en las 4 rutas espejo completada.
  - Respaldo creado en Histórico tablero/Tablero_CMI_PMO_20261109_120210.html.
  - Publicación a producción en GitHub Pages (commit 9359cb0).


## 44. Registro de Ponderación de 14 Releases al 7,14% y Desglose Visual AyN + RyC en Balú 421 (09-nov-2026)

- **Regla de Ponderación Uniforme (7,14% por Release):**
  - Se estructuró el universo contractual completo en **14 Releases a Producción** (100% / 14 = 7,142857% ~ **7,14% cada release**):
    - **10 Releases en Afiliaciones y Novedades (AyN):** 71,43% de peso contractual del proyecto.
    - **4 Releases en Sistema de Recaudo y Cartera (RyC):** 28,57% de peso contractual del proyecto.
- **Hoja Exclusiva de Validación Manual del Equipo:**
  - Se añadió la pestaña Features No Correlacionadas en Matriz_Correlacion_Cronograma_BALU_vs_Azure_2026.xlsx (en carpeta de proyecto y Downloads).
  - Lista las **49 Features de Azure DevOps** que no están correlacionadas directamente en los 14 releases, clasificadas por diagnóstico preliminar (Transversales/QA: 12, Fase Previa/MVP Cerrado 100%: 11, Operativas activas sin release asignado: 26).
  - Incluye columnas resaltadas en amarillo para el diligenciamiento manual del equipo (¿Aplica a Cronograma?, Release Sugerido, Frente Asignado, Justificación).
- **Arquitectura Visual en Tablero (
enderCrono421Collapsible):**
  - Desglose en dos bloques independientes con la misma estructura tabular:
    1. **Tabla 1 (AyN):** 10 Releases (7,14% c/u · Subtotal 71,43%), mostrando estado, avance, desviaciones en días hábiles y calendario, y fila subtotal.
    2. **Tabla 2 (RyC):** 4 Releases (7,14% c/u · Subtotal 28,57%) en fechas 14-Nov, 23-Ene, 20-Feb y 20-Mar, con avance técnico de sus features (92,5%, 22,7%, 48,6%, 68,4%) y fila subtotal.
    3. **Fila Total del Proyecto:** 14 Releases (100,00%), avance técnico global de 70,16%, Meta al corte de 21,43% (3 debidos de AyN), Real logrado de 17,95% y Brecha de cumplimiento de -3,48 pp.
- **Impacto en Cumplimiento de Cronograma e Indicador de Éxito:**
  - Denominador (Meta Proyectada): 3 de 14 releases debidos = **21,43%** (R1, R2 y R3 de AyN).
  - Numerador (Real Alcanzado en hitos debidos): **17,95%** (R1 6,32% + R2 6,17% + R3 5,46%).
  - Brecha de Cumplimiento: **-3,48 pp** (17,95% - 21,43%).
  - Indicador de Éxito: **39,60%** (Táctico 30% [14,46%] + RQC 40% [19,75%] + Cronograma 30% [5,39%]).
- **Sincronización y Publicación:**
  - Verificación con erify_integrity.py OK y ACTUALIZAR.py --dry-run OK.
  - Sincronización en las 4 rutas espejo y respaldo creado en Histórico tablero/Tablero_CMI_PMO_20261109_123037.html.
  - Publicación a producción en GitHub Pages (commit b3ba2bd).


## 45. Registro de Transición a 20 Releases Integrados (5,00% c/u), Incorporación de Fases Previas e Integración de Alerta de Gobernanza en BALÚ 421 (09-nov-2026)

- **Transición Metodológica a 20 Releases Homogéneos (5,00% cada uno · 100% Total):**
  - Se incorporaron formalmente las 3 fases contractuales previas históricas (37 entregables al 100%) como los Releases 1, 2 y 3 del proyecto:
    - **Release 1 (Histórico AyN · 27-Oct-2025):** 5 entregables (`Novedades Independiente`, `Afiliación Indep.`, `Gestión Funcionario`, `Actualizar Empleador/Trabajador`) · 100% Entregado.
    - **Release 2 (Histórico AyN · 26-Ene-2026):** 28 entregables (Masivos, Certificados, Liquidación, Reclasificación, Retiros) · 100% Entregado.
    - **Release 3 (Histórico AyN · 25-Jul-2026):** 4 entregables (Prórrogas, Riesgos, Contratos indep., Retiros retroactivos) · 100% Entregado.
  - El proyecto queda estructurado en **20 Releases Integrados**:
    - **Frente 1: Afiliaciones y Novedades (13 Releases):** 65,00% de peso contractual (3 históricos al 100% + 10 activos con fecha).
    - **Frente 2: Sistema de Recaudo y Cartera (7 Releases):** 35,00% de peso contractual (7 releases con fecha entre 16-Oct-2026 y 22-May-2027).
- **Métricas de Cronograma e Indicador de Éxito Ponderado:**
  - **Releases debidos al corte (09-Nov-2026):** 7 de 20 releases debidos (R1, R2, R3 históricos al 100% + R4, R5, R6 AyN + R14 RyC activos).
  - **Meta Proyectada al Corte:** **35,00%** (7 debidos $\times$ 5,00%).
  - **Real Logrado (Ponderado debidos):** **31,41%** (15,00% formalizado al 100% + 16,41% ponderado de los 4 debidos activos).
  - **Brecha de Cumplimiento:** **-3,59 pp** (31,41% vs 35,00%).
  - **Releases formalizados al 100%:** **3 de 7 debidos (15,00%)**.
  - **Indicador de Éxito Ponderado BALÚ:** **43,63%** (Táctico 30% [14,46%] + RQC 40% [19,75%] + Cronograma 30% [9,42%]).
- **Alerta de Gobernanza y Plazo Contractual al Final de la Tabla:**
  - Se ubicó al final de la sección de cronograma el banner de advertencia ejecutiva:
    `⚠️ Alerta de Gobernanza y Plazo Contractual: Existen 19 funcionalidades contractuales (14 en AyN y 5 en RyC) que registran avance técnico en Azure DevOps pero no tienen fecha pactada de paso a productivo con el cliente (ponderan el 15% de cada frente). Su falta de calendarización representa un riesgo crítico de prórroga contractual más allá de Mayo 2027.`
  - Incluye acordeón interactivo para consultar las 19 funcionalidades sin fecha pactada.
- **Sincronización y Publicación:**
  - Verificación exitosa con `python ACTUALIZAR.py --dry-run` (0 errores).
  - Sincronización en las 4 rutas espejo y respaldo creado en `Histórico tablero/`.
  - Publicación a producción en GitHub Pages (commit `eba68b1`).

---

## 46. Registro de Ajuste Integral en Proyecto 419 (Depósitos Judiciales): Base Oficial de 466 Funcionalidades, Tabla Desviación de Cronograma, Mora de Revisión Cliente y Certificado con Acta (09-nov-2026)
* **Homologación de Funcionalidades Certificadas por Cliente (Peso: 40%):**
  - Se unificó el cálculo del componente de funcionalidades al denominador oficial contractual del proyecto: **466 funcionalidades** (en lugar de las 219 de Azure DevOps).
  - Fórmula actualizada: `var1_419 = 80 / 466 = 17,17%` (80 certificadas por cliente sobre 466 totales).
  - Aporte al Éxito del Portafolio: `17,17% × 40% = 6,87%` (antes 11,51%).
  - Indicador de Éxito Ponderado 419: **28,55%** (Aporte Funcionalidades 6,87% + Aporte Cronograma Dual 21,69%).
  - Tarjeta del discriminado actualizada: `📋 Funcionalidades Certificadas por Cliente (Peso: 40%)` con `80 de 466 funcionalidades certificadas por cliente`.
* **Ajustes en la Sección "Desviación de Cronograma" (16 Sprints):**
  1. **Nombre de la Sección:** Se simplificó a **`🗓️ Desviación de Cronograma`** (eliminando el subtítulo extenso en el encabezado).
  2. **Encabezados Homologados:** Se cambió `HUs UAT/Prod` (Momento 1) y `HUs en Prod` (Momento 2) a **`Funcionalidades al 100%`**.
  3. **Estado Momento 1 (Linktic):** Sprints 1 a 6 cambiados a **`🟢 Entregado`** (desarrollo culminado y puesto a disposición de UAT).
  4. **Causa de Reprogramación en Sprint 7 (Momento 1):** El Sprint 7 tiene fecha reprogramada al `07/12/2026` con **`+21 d hábiles`** de desviación respecto a su línea base original (prevista para finales de octubre 2026) debido a ajustes de alcance y dependencias técnicas pendientes, registrando actualmente 6,6% de avance (15/229 HUs).
  5. **Estado Momento 2 (Cliente):** Sprints 1 y 2 actualizados a **`🟢 Revisado`**.
  6. **Cálculo de Desviación en Días Hábiles en Momento 2 (Mora de Revisión del Cliente al corte 09/11/2026):**
     - **Sprint 5 (Plan: 26/06/2026):** **`+90 d hábiles`** de retraso en revisión y aprobación por parte del cliente.
     - **Sprint 4 (Plan: 25/08/2026):** **`+52 d hábiles`** de retraso en revisión y aprobación por parte del cliente.
     - **Sprint 3 (Plan: 26/08/2026):** **`+51 d hábiles`** de retraso en revisión y aprobación por parte del cliente.
     - **Sprint 1 y 2 (Plan: 31/07/2026):** `0 d` (ya atendidos en estado `🟢 Revisado`).
     - **Sprint 6 (Plan: 07/12/2026):** `0 d (En plazo)` (fecha posterior al corte oficial).
     - **Sprint 7 (Plan: 06/01/2027):** `+23 d hábiles` (reprogramación acumulada por efecto de Momento 1).
  7. **Nueva Columna "Certificado con Acta":**
     - Sprints 1 y 2: **`🟡 En proceso`** (previamente certificados por cliente, pendiente formalización documental).
     - Sprints 3 a 7: **`⚪ Pendiente`**.
     - Sprints 8 a 16: **`⚪ Futuro`**.
     - Fila Total: **`2 en proceso`**.
* **Sincronización y Publicación:**
  - Verificación exitosa de compatibilidad con `python ACTUALIZAR.py --dry-run` (0 errores).
  - Respaldo generado en `Histórico tablero/Tablero_CMI_PMO_20261109_152811.html`.
  - Sincronización en las 4 rutas espejo y despliegue a producción en GitHub Pages (commit `0c2279a`).

---

## 47. Registro de Ajustes en 419 (Funcionalidades en Cronograma, Conciliación de Bugs visible y Retiro de Gráfica) y Actualización Financiera Portafolio a Octubre 2026 (09-nov-2026)

* **Ajuste de Conteo de Funcionalidades en Cronograma 419:**
  - Se sustituyeron las cifras de HUs por el conteo real de **Funcionalidades** (Features) asociadas a cada Sprint en Azure DevOps:
    - **Sprint 1:** **42 Funcionalidades** en total (34 de Banco Agrario en Épica `291675` + 8 de Rama Judicial en Épica `360573`), con 42 entregadas en Momento 1 (100%) y 42 revisadas en Momento 2 (100%).
    - **Sprint 2:** 25 Funcionalidades (18 entregadas M1 / 18 revisadas M2).
    - **Sprint 3:** 16 Funcionalidades (16 entregadas M1 / 0 M2).
    - **Sprint 4:** 23 Funcionalidades (23 entregadas M1 / 0 M2).
    - **Sprint 5:** 11 Funcionalidades (11 entregadas M1 / 0 M2).
    - **Sprint 6:** 15 Funcionalidades (15 entregadas M1 / 2 M2).
    - **Sprint 7:** 30 Funcionalidades (0 entregadas M1 / 0 M2).
    - **Sprint 8:** 28 Funcionalidades (0 entregadas M1 / 0 M2).
  - Se ajustó el encabezado de las columnas tanto en Momento 1 como en Momento 2 a **`Funcionalidades`**.

* **Reorganización de la Sección de Defectos (Bugs) y Conciliación 419:**
  - **Tabla de Conciliación Visible Directamente:** La tabla `💵 Conciliación de bug´s con reportados por Cliente` queda visible inmediatamente al abrir el proyecto.
  - **Encabezado Actualizado:** Se cambió `Total Facturado / Conciliado` a **`Total conciliado`**.
  - **Columna Eliminada:** Se retiró la columna `Estado Comercial` de la tabla de conciliación.
  - **Acordeón Desplegable para Gráfica y ANS:** La gráfica `🐛 Evolución Consolidada de Bugs 419 (DEP vs RAMA) y Tiempos de Respuesta vs ANS (3 Días)` y sus KPI tiles se ubicaron dentro de una pestaña desplegable interactiva (`<details class="cmi-accordion">`), permitiendo consultar el detalle sin sobrecargar la vista principal.
  - **Retiro Definitivo de Gráfica de Entregas y Certificaciones:** Se eliminó la sección y contenedor de `#c-419` (`Entregas y certificaciones`), dado que la información oficial está consolidada en el desglose funcional vivo y en la tabla de cronograma.

* **Actualización Financiera a Octubre 2026 (Libros `20261109`):**
  - **Proyecto 419 (Depósitos Judiciales - `Indicadores_419_V11 20261109.xlsx`):**
    - Facturación acumulada real: **$5.640,6 M Sin IVA / $6.712,3 M Con IVA** (19,80% avance).
    - EVM Real acumulado: **$4.565,0 M** (Octubre: $460,3 M).
    - Métricas: CPI ppto **0,4742**, CPI fcst **0,2743**, ICFF **1,5609**.
  - **Proyecto 421 (BALÚ - `IndicadoresBalu 20261109.xlsx`):**
    - Facturación acumulada real: **$38.071,8 M Sin IVA / $45.305,4 M Con IVA** (37,72% avance).
    - EVM Real acumulado: **$13.863,3 M** (Octubre: $999,6 M).
    - Métricas: CPI ppto **1,1874**, CPI fcst **0,8273**, ICFF **1,2412**.
  - **Proyecto 453 (CPE - `Indicadores_CPE 20261109.xlsx`):**
    - EVM Real acumulado: **$1.337,1 M** (Septiembre: $248,6 M, Octubre: $231,1 M).
    - Métricas: CPI ppto **0,1352**, CPI fcst **0,1405**, ICFF **7,9320**.
  - **Proyecto 456 (Aeronáutica Civil - `Indicadores456 20261109.xlsx`):**
    - EVM Real acumulado: **$423,8 M** (Octubre: $76,6 M).
    - Métricas: CPI ppto **0,3663**, CPI fcst **0,4437**, ICFF **1,6554**.

* **Sincronización y Publicación:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (**0 errores**, patrón `FR` intacto).
  - Sincronización en las 4 rutas espejo completada.
  - Publicación y despliegue en producción completado en GitHub Pages (`commit edb1abe`).

---

## 48. Registro de Visibilidad Financiera en Vercel, CMI de 456 sobre Features de Azure DevOps y Medición de 453 sobre 76 Casos de Uso (09-nov-2026)

* **Activación de Visibilidad Financiera Ejecutiva en Vercel y Producción:**
  - **Causa identificada:** Los contenedores `#tiles` (KPIs financieros del portafolio) y `#cash-cost` (Del contrato a la caja y Costo real 2026 vs forecast) contenían el atributo HTML `hidden`, impidiendo su despliegue en la Vista de Dirección tanto en Vercel como en entornos web y locales.
  - **Solución implementada:** Se removió el atributo `hidden` de ambos contenedores (`<div class="grid g-tiles" id="tiles">` y `<div class="section grid g-2" id="cash-cost">`), dejando inmediatamente visibles:
    1. Los 5 Tiles Financieros Ejecutivos del Portafolio: Total valor contrato, Total facturado, Recaudo efectivo, Costo real 2026 y Forecast 2026 (con conmutador Sin/Con IVA).
    2. Las dos secciones financieras de Dirección: "Del contrato a la caja" (`#flow`) y "Costo real 2026 vs forecast" (`#c-costport`).

* **Proyecto 456 (Aeronáutica Civil) · Medición sobre Funcionalidades de Azure DevOps:**
  - Se desacopló la medición contractual hardcodeada de 6 hitos, calculando ahora los indicadores CMI directamente sobre las **4 Funcionalidades (Features)** activas en Azure DevOps (`545363`, `545458`, `545459`, `545460`):
    - **Indicador Táctico:** **15,00%** (3 funcionalidades en escala 20% + 1 en escala 0% = 60% / 4).
    - **Indicador Estratégico:** **0,00%** (0 de 4 funcionalidades formalizadas en producción).
    - **Insignia y Callout:** Badge actualizado a `Azure · 4 Func.` y callout `4 Funcionalidades en Azure · 0 en prod. · 0,0% cerrado`.
    - Hero cards CMI integradas al cálculo estándar por funcionalidades vivas.

* **Proyecto 453 (Monitoreo CPE) · Medición sobre 76 Casos de Uso y Limpieza de Controles:**
  - **Medición sobre la Totalidad de Casos de Uso:**
    - Se eliminó el cálculo restringido a los 4 Focos, evaluando ahora la totalidad de los **76 Casos de Uso** del proyecto:
      - **Indicador Táctico:** **40,00%** (29 CUs al 100% + 7 CUs al 20% + 40 CUs a 0% evaluados bajo la Escala CMI PMO).
      - **Indicador Estratégico:** **38,16%** (**29 de 76 Casos de Uso** entregados al 100% en estado `19. Entregado`).
      - **Insignia y Callout:** Badge actualizado a `Azure · 76 CUs` y callout `76 Casos de Uso en Azure · 29 en prod. · 38,2% cerrado`.
  - **Depuración de Interfaz en Ficha Operativa:**
    - Se renombró el banner a: `Insumo CMI Oficial PMO · Indicadores Táctico y Estratégico (Medición por Casos de Uso)` con tag `76 Casos de Uso`.
    - Se retiraron por completo los botones interactivos de conmutación metodológica `▶ Por ejecución` / `◆ Por compromiso` y la nota explicativa *"cada HU cuenta en SU iteración — en qué se trabaja de verdad"*, garantizando una visual limpia y libre de ruidos metodológicos.

* **Sincronización y Publicación:**
  - Verificación exitosa con `python ACTUALIZAR.py --dry-run` (0 errores).
  - Respaldo generado en `Histórico tablero/Tablero_CMI_PMO_20261109_162542.html`.
  - Sincronización completa en las 4 rutas espejo y archivos JSON (`data_func.json`, `data_453_cpe.json`).
  - Publicación y despliegue en producción completado en GitHub Pages y Vercel (`commit 775d8c0`).

---

## 49. Registro de Ajuste Integral de Visualización Financiera al 09-Nov-2026 (Corte Octubre 2026) en 419, 421, 453 y 456 (09-nov-2026)

* **Causa Raíz Identificada:**
  - Aunque los números de EVM y las curvas `m` se habían actualizado a Octubre 2026, la interfaz gráfica mantenía ataduras visuales y constantes rígidas:
    1. `const CUT=8`: Limitaba el cálculo acumulado (`ytd`) y el gráfico mensual SVG (`renderMonth`) a los primeros 8 meses (Ene–Ago), sombreando Septiembre y Octubre como "Proyección" y ocultando las barras reales de Octubre 2026.
    2. Etiquetas hardcodeadas en `renderCost` y `renderFact`: Decían literalmente *"Información actualizada al 1 de octubre de 2026"*, *"Real ene–ago"* y *"Forecast ene–ago"*.
    3. Metadatos de libros locales en `PROJ_DATES_META`: Apuntaban a archivos de fecha `20260929` y fecha de corte `01-Oct-2026`.
    4. Encabezado principal del tablero: Mostraba `Act. Financiera: 01-Oct-2026 (Archivos locales)`.

* **Soluciones Implementadas:**
  - **Función Dinámica de Corte Real (`getProjCut`):** Se implementó `const getProjCut = p => { ... }` que evalúa dinámicamente hasta qué mes tiene ejecución real cada proyecto:
    - Proyectos con libro a Octubre 2026 (419, 421, 453, 456): su corte dinámico es **mes 10 (Octubre)**, dibujando las barras reales de Septiembre y Octubre, y proyectando únicamente Noviembre y Diciembre.
    - Proyectos con corte a Septiembre (348, 397): corte en mes 9.
    - Proyectos con corte a Agosto (005, POS): corte en mes 8.
  - **Actualización de Metadatos de Libros `20261109`:**
    - Encabezado general: `Act. Financiera: 09-Nov-2026 (Corte mensual Octubre 2026 · Libros 09-Nov-2026)`.
    - 419: `finDate: "09-Nov-2026"`, `finFile: "Indicadores_419_V11 20261109.xlsx · 419_Resumen 20261109.xlsx (Corte Oct-2026)"`.
    - 421: `finDate: "09-Nov-2026"`, `finFile: "IndicadoresBalu 20261109.xlsx (Corte Oct-2026)"`.
    - 453: `finDate: "09-Nov-2026"`, `finFile: "Indicadores_CPE 20261109.xlsx (Corte Oct-2026)"`.
    - 456: `finDate: "09-Nov-2026"`, `finFile: "Indicadores456 20261109.xlsx (Corte Oct-2026)"`.
  - **Textos Reactivos en Pestañas "Costos" y "Facturación":**
    - Subtítulos dinámicos: *"Información actualizada al 09 de noviembre de 2026 (Corte mensual Octubre 2026)"*.
    - Indicadores del gráfico mensual: `Real ene–oct` y `Forecast ene–oct`.
    - Leyenda de proyección: `Millones COP · real cerrado ene–oct · nov–dic proyección`.
  - **Actualización en Pestaña "Costo Personal" (`team`):**
    - Fuentes actualizadas a los libros `20261109` y periodos ajustados a `Octubre 2026`.

* **Sincronización y Publicación:**
  - Verificación exitosa con `python ACTUALIZAR.py --dry-run` (0 errores).
  - Respaldo generado en `Histórico tablero/Tablero_CMI_PMO_20261109_163716.html`.
  - Sincronización en las 4 rutas espejo y despliegue a producción en GitHub Pages y Vercel (`commit b2c696c`).

---

## 50. Registro de Restauración de Indicadores Operativos Contractuales en Proyecto 456 (Aeronáutica Civil) (09-nov-2026)

* **Alcance de la Restauración:**
  - Por solicitud del usuario, se restauraron los **indicadores operativos** del proyecto **456 (Aeronáutica Civil)** a su modelo previo de **Supervisión Contractual por Hitos**, conservando intacta toda la actualización de la información **Financiera** con corte a Octubre 2026 (`Indicadores456 20261109.xlsx`):
    - **Indicador Táctico:** **24,00%** (avance ponderado según pesos contractuales de las 3 fases: 18% × 1 + 12% × 0,5).
    - **Indicador Estratégico:** **16,67%** (**1 de 6 entregables** formalizados al 100% · Meta a la fecha: 2/6 · 33,33% · Brecha: -16,67 pp).
    - **Indicador de Éxito Contractual:** **18,00%** (Meta al corte: 30,00% · Brecha: -12,00 pp).
    - **Identidad Visual:**
      - Insignia (badge): **`Contractual · 6 Hitos`**.
      - Callout ejecutivo: `1 de 6 hitos formalizados (Meta a la fecha: 2/6 · 33,3% · Brecha: -16,7 pp) · Táctico: 24,0% · Meta: 30,0% · Brecha: -6,0 pp`.
      - Ficha y Hero Cards CMI: Reactivadas las tarjetas de supervisión contractual viva con meta proyectada a la fecha reprogramada y brecha en pp.
      - Banner de captura Azure DevOps en la ficha: `Supervisión Contractual (6 Hitos) + Captura Azure DevOps`.
  - **Dimensión Financiera Preservada:**
    - Se mantiene el libro oficial `Indicadores456 20261109.xlsx`, fecha `09-Nov-2026 (Corte Octubre 2026)`, corte dinámico `getProjCut` en mes 10 (Octubre), EVM acumulado ($423,8 M), CPI ppto 0,37 / fcst 0,44, ICFF 1,66 y desglose del equipo.

* **Sincronización y Publicación:**
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (**0 errores**).
  - Respaldo generado en `Histórico tablero/Tablero_CMI_PMO_20261109_164423.html`.
  - Sincronización en las 4 rutas espejo y archivos de datos.
  - Publicación y despliegue completado en GitHub Pages y Vercel (`commit 86fb741`).


---

## 51. Registro de Incorporación Financiera del Proyecto 020 (Positiva Servicios de Analítica) (09-nov-2026)

* **Incorporación del Libro Oficial:**
  - Se incorporó formalmente el libro `020 analitica 20261109.xlsx` (`Información Financiera\020- Analítica de datos\`).
  - Proyecto **020 (020 - PROYECTO SERVICIOS DE ANALITICA)** pasa de estado `opOnly: true` a proyecto con seguimiento financiero pleno e ingresa formalmente a la lista `FIN`, sumando a los totales y gráficos ejecutivos del portafolio (`#tiles`, `#flow`, `#c-costport`).

* **Dimensiones Financieras Habilitadas:**
  1. **Contrato y Facturación:**
     - **Valor Contrato Sin IVA:** **$1.936,5 M** (`$1.936.471.859`).
     - **Valor Contrato Con IVA:** **$2.304,4 M** (`$2.304.401.512`).
     - **Facturación Real Acumulada Sin IVA:** **$1.761,0 M** (`$1.761.025.200`) (**90,94%** de avance contractual sobre valor sin IVA).
     - **Facturación Real Acumulada Con IVA:** **$1.821,7 M** (`$1.821.697.469`) (**79,05%** de avance contractual con IVA).
     - **IVA Facturado Acumulado:** **$60,7 M** (`$60.672.269`).
     - **Retenciones Acumuladas:** **$73,0 M** (`$73.002.210`).
     - **Facturación Pendiente:** **$175,4 M** (Sin IVA) / **$482,7 M** (Con IVA).
     - **Cumplimiento de Facturación:** **76,42%** (Brecha: -$543,4 M frente a la facturación planeada acumulada de $2.304,4 M).
  2. **Recaudo:**
     - **Recaudo Real Acumulado:** **$1.588,3 M** (`$1.588.328.466`).
     - **Recaudo Esperado Neto:** **$1.748,7 M** (`$1.748.695.259`).
     - **Pendiente de Recaudo:** **$160,4 M** (`$160.366.793`).
     - **Cumplimiento de Recaudo:** **90,83%** (Brecha: -$160,4 M).
  3. **Costos y EVM (Corte Octubre 2026):**
     - **Presupuesto Original (PV ppto):** **$1.826,8 M** (`$1.826.755.950`).
     - **Presupuesto Forecast (PV fcst):** **$1.625,1 M** (`$1.625.095.728`).
     - **Costo Real Acumulado (AC):** **$1.136,1 M** (`$1.136.056.311`).
     - **Avance Táctico:** **58,75%** (2 de 8 funcionalidades entregadas al 100%).
     - **Valor Ganado (EV) PPTO:** **$1.073,2 M** (`$1.073.219.121`).
     - **Valor Ganado (EV) FCST:** **$954,7 M** (`$954.743.740`).
     - **CPI Escenario PPTO:** **0,94** (`0.9447`).
     - **CPI Escenario FCST:** **0,84** (`0.8404`).
     - **ICFF Escenario FCST:** **1,37** (`1.3708`).
     - **Curva Mensual 2026:** Ene-Oct con costos reales ($55,6 M, $132,0 M, $131,9 M, $149,3 M, $136,6 M, $129,5 M, $89,8 M, $63,5 M, $106,8 M, $141,1 M) y proyecciones Nov ($184,3 M) y Dic ($124,7 M).
  4. **Equipo de Trabajo (`team`):**
     - Costo acumulado Ene-Oct: **$616,2 M** (14 HC, fuente: `020 analitica 20261109 · Indicadores Costo`).
  5. **Hitos Contractuales (`hitos`):**
     - 14 hitos en total: 12 de Operación e Infraestructura ($160,4 M c/u; Ene–Jun facturados al 100%, Jul–Dic pendientes) y 2 de Iniciativa 1 POC ($190,0 M c/u; Hito 1 facturado, Hito 2 pendiente).

* **Metadata y Sincronización:**
  - `PROJ_DATES_META["020"]` actualizado a `finDate: "09-Nov-2026"` y `finFile: "020 analitica 20261109.xlsx (Corte Oct-2026)"`.
  - Validación con `python ACTUALIZAR.py --dry-run` exitosa (**0 errores de regex**).
  - Sincronización completa en las 4 rutas espejo:
    1. `c:\Users\IvanDarioPastorParra\Indicadores estra y tac\index.html`
    2. `c:\Users\IvanDarioPastorParra\Indicadores estra y tac\Tablero_CMI_PMO.html`
    3. `C:\Users\IvanDarioPastorParra\Documents\PMO INDICADORES\CMI\Tablero_CMI_PMO.html`
    4. `C:\Users\IvanDarioPastorParra\Downloads\Tablero_CMI_PMO.html`
  - Publicación y despliegue a producción completado en GitHub Pages y Vercel (`commit ed4d1cb`).


---

## 52. Registro de Implementación de la Visual Espejo Protegida por Key y Master Key PMO (09-nov-2026)

* **Respaldo Local Previo:**
  - Copia de seguridad íntegra generada y guardada en `Histórico tablero/Tablero_CMI_PMO_20261109_171657.html`.

* **Arquitectura de Doble Visual:**
  1. **Visual Administradora (`index.html`):**
     - Mantiene el 100% de la información operativa, estratégica y financiera del portafolio.
     - Incorpora el botón ejecutivo en el header: `🛡️ Visual Espejo (Clientes)` que enlaza a `consulta.html`.
  2. **Visual Espejo (`consulta.html`):**
     - Portal de acceso seguro para clientes y líderes técnicos.
     - Protegido mediante pantalla de autenticación con validación criptográfica **SHA-256 en el navegador** (`crypto.subtle`).
     - Al ingresar la clave de un proyecto específico (ej. `DEP-419-JUDICIAL`):
       - Oculta el portafolio consolidado, gráficos globales y datos de los demás proyectos.
       - Aísla la memoria a ese proyecto y muestra directamente su ficha operativa CMI, Azure DevOps y finanzas específicas.
       - Muestra el banner superior: `🛡️ Consulta Exclusiva: [Nombre Proyecto]` con botón `🚪 Cerrar Sesión`.
       - Bloquea cualquier intento de navegación hacia proyectos no autorizados.
     - Al ingresar la **Master Key PMO (`PMO-MASTER-2026*`)**:
       - Desbloquea todos los proyectos y el portafolio completo en modo administrador (`👑 Modo Administrador PMO`).

* **Directorio de Claves Predeterminadas (`DIRECTORIO_CLAVES_PMO.md`):**
  - **Master Key PMO:** `PMO-MASTER-2026*`
  - **005 (Positiva SGDEA):** `POS-005-SGDEA`
  - **POS (Core Positiva Consolidado):** `POS-CORE-GLOBAL`
  - **355 (Positiva Core 355):** `POS-355-CORE`
  - **416 (Positiva Core 416):** `POS-416-CORE`
  - **384 (Core Fiduprevisora):** `FIDU-384-CORE`
  - **419 (Depósitos Judiciales):** `DEP-419-JUDICIAL`
  - **421 (Balú):** `BALU-421-RECAUDO`
  - **453 (Monitoreo CPE):** `CPE-453-MONITOR`
  - **456 (Aeronáutica Civil):** `AERO-456-INNOV`
  - **348 (SGDEA Acueducto):** `EAAB-348-SGDEA`
  - **397 (Core Andina):** `ANDI-397-CORE`
  - **457 (Portales La Equidad):** `EQUI-457-PORTAL`
  - **020 (Analítica Positiva):** `POS-020-DATA`
  - **461 (Cuentas Claras CNE):** `CNE-461-CUENTAS`
  - **420 (Pólizas de Salud Positiva):** `POS-420-SALUD`

* **Sincronización y Despliegue en Producción:**
  - Archivos sincronizados en las 4 rutas espejo:
    1. `c:\Users\IvanDarioPastorParra\Indicadores estra y tac\index.html` (Administradora)
    2. `c:\Users\IvanDarioPastorParra\Indicadores estra y tac\consulta.html` (Visual Espejo)
    3. `C:\Users\IvanDarioPastorParra\Documents\PMO INDICADORES\CMI\Tablero_CMI_PMO.html` y `consulta.html`
    4. `C:\Users\IvanDarioPastorParra\Downloads\Tablero_CMI_PMO.html` y `consulta.html`
  - Verificación exitosa con `python ACTUALIZAR.py --dry-run` (0 errores de regex).
  - Publicación a producción en GitHub Pages y Vercel.


---

## 53. Registro de Automatización y Tubería Unificada para las Tres Visuales PMO (09-nov-2026)

* **Ecosistema de las Tres Visuales:**
  1. **Visual 1: Vista Libre Actual (`index.html`):**
     - URL: `https://ivanpastor-debug.github.io/Tablero-CMI-PMO/`
     - Acceso libre directo para consulta general de todo el portafolio.
     - Enlaces cruzados en cabecera: `🛡️ Vista por Clave` y `👑 Master PMO`.
  2. **Visual 2: Master PMO (`master.html`):**
     - URL: `https://ivanpastor-debug.github.io/Tablero-CMI-PMO/master.html`
     - Acceso restringido exclusivo para Dirección y PMO.
     - Protegido mediante la **Master Key PMO (`PMO-MASTER-2026*`)**.
     - Desbloquea la totalidad del portafolio consolidado, EVM, flujo contractual y todos los proyectos.
     - Banner superior: `👑 Panel Master PMO · Vista de Dirección Completa`.
  3. **Visual 3: Vista con Key por Proyecto (`consulta.html`):**
     - URL: `https://ivanpastor-debug.github.io/Tablero-CMI-PMO/consulta.html`
     - Acceso restringido por proyecto para clientes y líderes técnicos.
     - Al ingresar la clave de un proyecto (ej. `DEP-419-JUDICIAL`):
       - Oculta el portafolio global y los demás proyectos.
       - Reemplaza el selector de búsqueda por una tarjeta exclusiva de proyecto autorizado.
       - Despliega de inmediato la ficha integral del proyecto (CMI, Azure DevOps, Bugs, Cronograma, Finanzas).
       - Fija la navegación impidiendo acceso a datos ajenos.
     - Al ingresar la **Master Key (`PMO-MASTER-2026*`)**, desbloquea todos los proyectos en modo administrador.

* **Tubería Automática de Sincronización Disparada (`generate_three_views.py`):**
  - Cualquier actualización operativa o financiera disparada mediante:
    - `python ACTUALIZAR.py`
    - `python actualizar_todo.py`
    - `ACTUALIZAR_TODO.bat`
  - Ejecuta automáticamente `generate_three_views.py`, propagando los datos actualizados a las **tres visuales** simultáneamente:
    - `index.html` (Vista libre)
    - `master.html` (Master PMO)
    - `consulta.html` (Vista por clave)
  - Y sincroniza a las 3 ubicaciones locales (Repositorio de despliegue, Copia maestra CMI y Downloads).

* **Validación y Despliegue:**
  - `python ACTUALIZAR.py --dry-run` verificado con **0 errores**.
  - Desplegado en GitHub Pages y Vercel (`commit 2ad15b1`).


---

## 54. Registro de Ocultamiento de Métricas Consolidadas en Vista de Dirección y Entrega de Directorio Excel (09-nov-2026)

* **Depuración de la "Vista de Dirección" (`#v-res`):**
  - Conforme a la instrucción del usuario, se ocultaron las métricas y gráficos consolidados del portafolio en la Vista de Dirección:
    - Ocultado `#tiles`: *Total valor contrato ($176.508 M)*, *Total facturado ($56.325 M)* y *Total recaudado ($49.541 M)*.
    - Ocultado `#cash-cost`: Secciones *Del contrato a la caja* (`#flow`) y *Costo real 2026 vs forecast* (`#c-costport`).
  - **Alcance resultante en "Vista de Dirección":** Muestra **únicamente las tarjetas/etiquetas de proyecto** (`#sem-op`), donde cada proyecto presenta de forma autónoma su propio indicador táctico y estratégico, desglose funcional Azure DevOps y su bloque financiero enriquecido (`finMini`: Contrato Sin/Con IVA, Facturado con % avance, Recaudado, CPI ppto/fcst).
  - En **Master PMO (`master.html`)**, las métricas consolidadas se mantienen habilitadas para la Dirección General una vez validada la Master Key.

* **Entrega de Directorio de Claves y Enlaces en Excel (`Directorio_Claves_y_Accesos_PMO.xlsx`):**
  - Generado libro oficial con estilo corporativo PMO:
    - **Hoja 1:** Directorio con las 3 URLs públicas activas en GitHub Pages/Vercel y las 16 claves criptográficas (Master Key PMO + 15 claves de proyectos).
    - Disponible en:
      1. `C:\Users\IvanDarioPastorParra\Documents\PMO INDICADORES\CMI\Directorio_Claves_y_Accesos_PMO.xlsx`
      2. `C:\Users\IvanDarioPastorParra\Downloads\Directorio_Claves_y_Accesos_PMO.xlsx`
      3. `c:\Users\IvanDarioPastorParra\Indicadores estra y tac\Directorio_Claves_y_Accesos_PMO.xlsx`

* **Sincronización y Despliegue:**
  - `python ACTUALIZAR.py --dry-run` verificado con **0 errores**.
  - Sincronizado en las 4 rutas espejo y publicado en producción en GitHub Pages y Vercel (`git push origin main`).


---

## 55. Registro de Ponderación Oficial del Cronograma en Proyecto 421 (Balú) con Funcionalidades No Comprometidas (09-nov-2026)

* **Definición Metodológica de Ponderación Contractual Solicitada:**
  - Conforme a la instrucción del usuario, se ajustó la estructura de pesos del proyecto **421 - Balú** para transparentar las 19 funcionalidades contractuales que no cuentan con fecha de paso a producción pactada:
    1. **Funcionalidades No Comprometidas (Sin fecha de release pactada): 20,00% del proyecto**.
       - **Frente 1: Afiliaciones y Novedades (AyN):** 14 funcionalidades (Prioridades P3 y P4) -> **10,00% de peso**.
       - **Frente 2: Recaudo y Cartera (RyC):** 5 funcionalidades (Transferencias Masivo/WS y WS SISE Fase 2) -> **10,00% de peso**.
    2. **20 Releases Calendarizados: 4,00% de peso cada uno (80,00% del proyecto)**.
       - 13 Releases de AyN: $13 \times 4,00\% = \mathbf{52,00\%}$.
       - 7 Releases de RyC: $7 \times 4,00\% = \mathbf{28,00\%}$.
    3. **Total Proyecto Balú:** $52\% + 10\% + 28\% + 10\% = \mathbf{100,00\%}$.

* **Métricas Oficiales al Corte del Cronograma (09-Nov-2026):**
  - **Releases debidos a la fecha:** 7 releases de 20 (R1 a R6 de AyN + R14 de RyC).
  - **Meta proyectada de releases debidos:** $7 \times 4,00\% = \mathbf{28,00\%}$ (ajustada desde 35,00%).
  - **Real logrado de releases debidos (ponderado):** $\mathbf{25,12\%}$ (ajustado desde 31,41%):
    - R1: 4,00% · R2: 4,00% · R3: 4,00% (12,00% certificado en producción).
    - R4: 2,96% (74,1% técnico) · R5: 3,18% (79,5% técnico) · R6: 3,18% (79,5% técnico) · R14: 3,80% (95,0% técnico).
  - **Brecha de cumplimiento del cronograma:** $25,12\% - 28,00\% = \mathbf{-2,88\text{ pp}}$ (antes -3,59 pp).
  - **Indicador de Éxito Balú (421):**
    $$\text{Éxito 421} = (48,21\% \times 30\%) + (49,37\% \times 40\%) + (25,12\% \times 30\%) = \mathbf{41,75\%}$$

* **Modificaciones en la Interfaz y Ficha Operativa (`renderCrono421Collapsible`):**
  - **Columna `Peso`:** Actualizada a `4,00%` en cada una de las 20 filas de releases calendarizados.
  - **Filas de Funcionalidades No Comprometidas:**
    - Fila destacada en ámbar antes del subtotal de AyN: *⚠️ Funcionalidades AyN Sin Fecha Pactada (14 ítems)* con peso **10,00%**, avance en Azure del 81,2%, desviación "Sin fecha pactada" y estado "No comprometido".
    - Fila destacada en ámbar antes del subtotal de RyC: *⚠️ Funcionalidades RyC Sin Fecha Pactada (5 ítems)* con peso **10,00%**, avance en Azure del 53,4%, desviación "Sin fecha pactada" y estado "No comprometido".
  - **Subtotales y Totales:**
    - Subtotal AyN: **62,00%** (Meta corte: 24,00% · Real corte: 21,32% · Brecha: -2,68 pp).
    - Subtotal RyC: **38,00%** (Meta corte: 4,00% · Real corte: 3,80% · Brecha: -0,20 pp).
    - Total Proyecto: **100,00%** (Meta corte: 28,00% · Real logrado: 25,12% · Brecha: -2,88 pp).
  - **Resumen inferior y Alerta de Gobernanza:** Detalla la distribución $80\% / 20\%$ y el desglose de los 19 ítems para gestión de prórrogas con el cliente.

* **Sincronización de las Tres Visuales y Despliegue:**
  - Ejecutado `python generate_three_views.py`, actualizando:
    - `index.html` (Vista libre en producción)
    - `master.html` (Master PMO)
    - `consulta.html` (Visual Espejo protegida por clave)
  - Validación con `python ACTUALIZAR.py --dry-run` con **0 errores**.
  - Sincronización en las 4 rutas espejo y publicación automática en GitHub Pages (`commit 36ebfcb`).


---

## 56. Registro de Actualización de Nota Aclaratoria de Cumplimiento de Cronograma en Proyecto 421 (09-nov-2026)

* **Texto Homologado Solicitado:**
  - En la píldora de *Cumplimiento Cronograma (Peso: 30%)* del proyecto **421 - Balú**, se actualizó la nota aclaratoria inferior para reflejar exactamente el texto requerido:
    > *ℹ️ **Nota aclaratoria:** el cumplimiento del cronograma se evalúa contra el archivo Excel suministrado por el proyecto debido a las 53 funcionalidades pendientes de correlacionar en Azure.*

* **Sincronización en las Tres Visuales:**
  - Propagado automáticamente vía `generate_three_views.py` a:
    1. `index.html` (Vista libre en producción).
    2. `master.html` (Master PMO).
    3. `consulta.html` (Visual Espejo protegida por clave).
    4. Copias espejo locales (`Downloads`, `Documents/PMO INDICADORES/CMI` e `Indicadores estra y tac`).

* **Validación y Despliegue:**
  - `python ACTUALIZAR.py --dry-run` verificado con **0 errores** (regex intacto).
  - Cambios publicados en producción en GitHub Pages y Vercel (`commit dcbfb75`).


---

## 57. Registro de Generación de Excel Oficial de Funcionalidades Cerradas en Proyecto 419 (10-nov-2026)

* **Entrega de Archivo Excel Oficial (`Funcionalidades_Cerradas_419_Depositos_y_Rama.xlsx`):**
  - Se estructuró un libro corporativo de Excel con formato directivo PMO para transparentar las funcionalidades cerradas de **419-DEP (Depósitos Judiciales / BAC)** y **419-RAMA (Rama Judicial)**:
    1. **Hoja 1 (`Resumen Ejecutivo`):** Tarjetas KPI y tablas comparativas por frente (DEP vs RAMA), análisis de HUs terminadas y matriz de cruce entre avance al 100% y estado formal en Azure.
    2. **Hoja 2 (`100% Producción (63)`):** Relación de las **63 funcionalidades** cuyo avance técnico de HUs en producción es del 100,0% (**45** en Depósitos Judiciales y **18** en Rama Judicial). Incluye ID, Subproyecto, Épica, Title, Estado Actual, Etapa (HUs en producción), HUs activas, HUs terminadas y % Avance.
    3. **Hoja 3 (`Estado 4. Cerrado (88)`):** Relación de las **88 funcionalidades** con estado de Work Item `4. Cerrado` en Azure DevOps (**66** en Depósitos Judiciales y **22** en Rama Judicial).
    4. **Hoja 4 (`Consolidado Total (90)`):** Universo unificado de **90 funcionalidades únicas** clasificadas según criterio de cierre (100% en producción y cerrado, 100% en producción entregado, o cerrado con avance parcial).

* **Ubicaciones del Archivo:**
  - `C:\Users\IvanDarioPastorParra\Documents\PMO INDICADORES\CMI\Funcionalidades_Cerradas_419_Depositos_y_Rama.xlsx`
  - `C:\Users\IvanDarioPastorParra\Downloads\Funcionalidades_Cerradas_419_Depositos_y_Rama.xlsx`
  - `c:\Users\IvanDarioPastorParra\Indicadores estra y tac\Funcionalidades_Cerradas_419_Depositos_y_Rama.xlsx` (commiteado en `main`: `commit 2ed1501`).


---

## 58. Registro de Definición e Implementación del Indicador de Éxito en Proyecto 020 (10-nov-2026)

* **Definición Metodológica por Épicas de Azure DevOps:**
  - Conforme a la instrucción del usuario, se definió el **Indicador de Éxito** del proyecto **020 (Positiva Servicios de Analítica)** ponderando las tres épicas activas en Azure DevOps según los pesos asignados:
    1. **OPERACIÓN (Infraestructura):** Peso **35,58%** · Avance real: **91,15%** (44/52 HUs terminadas · 5 features) $\rightarrow$ Aporte: **32,43%**.
    2. **SOPORTE (Soporte y Mantenimiento):** Peso **47,93%** · Avance real: **92,86%** (18/21 HUs terminadas · 2 features) $\rightarrow$ Aporte: **44,51%**.
    3. **POC (Iniciativa 1):** Peso **16,49%** · Avance real: **100,00%** (7/7 HUs terminadas · 1 feature) $\rightarrow$ Aporte: **16,49%**.
  - **Indicador de Éxito Consolidado:**
    $$\text{Éxito 020} = 32,43\% + 44,51\% + 16,49\% = \mathbf{93,43\%} \quad (\text{Semáforo: Sobresaliente 🟢})$$

* **Presentación en la Interfaz (`cmiOverviewHTML`):**
  - **Hero Card `02 · Indicador de éxito`:** Muestra el valor **93,43%**, subtítulo `Ponderado por Épicas: Operación (35,58%) · Soporte (47,93%) · POC (16,49%)` e insignia `Favorable` / `Sobresaliente`.
  - **Sección de Conciliación de Indicador de Éxito:** Por instrucción del usuario, se mantuvo sin diligenciar por el momento (conserva el bloque estándar en homologación).

* **Sincronización y Publicación:**
  - Sincronizado en las tres visuales (`index.html`, `master.html`, `consulta.html`) mediante `generate_three_views.py`.
  - Verificado con `python ACTUALIZAR.py --dry-run` (**0 errores de regex**).
  - Desplegado a producción en GitHub Pages y Vercel (`commit 34a9925`).


---

## 59. Registro de Calibración de Escala Táctica CMI (Homologación V2) y Actualización Financiera Plurianual (10-nov-2026)

* **Calibración Metodológica de la Escala Táctica CMI:**
  - En base al libro maestro `Homologación estados Azure proyectos V2.xlsx` y tras la revisión exhaustiva del ciclo de vida del software, se refinó la función de homologación `huEscalaPmo`:
    1. **Requerimientos / Levantamiento (0% a 20% en ponderación):** Computa al **0,00%** de la escala CMI PMO.
    2. **Desarrollo (20% a 50% en ponderación):** Computa al **0,00%** de la escala CMI PMO (<50%), dado que el desarrollo culmina formalmente al alcanzar el 50% al desplegar a DEV/QA.
    3. **QA / Calidad (50% a 80% en ponderación):** Computa formalmente al **20,00%** de la escala CMI PMO (inicia formalmente desde Backlog QA y cubre todas las pruebas de integración y funcionales de calidad).
    4. **Pre-UAT / QA Concluido (80% a 85% en ponderación):** Computa al **50,00%** de la escala CMI PMO.
    5. **UAT del Cliente / Certificación (85% a 95% en ponderación):** Computa al **75,00%** de la escala CMI PMO.
    6. **Pase a Producción / Terminado (100% formal):** Computa al **100,00%** de la escala CMI PMO (y aporta al indicador estratégico).

* **Gobernanza de Indicadores Tácticos y Estratégicos del Portafolio:**
  - **004 (SGDEA 2024):** Táctico **29,60%** | Estratégico 17,07% (7/41)
  - **005 (SGDEA 2026):** Táctico **32,56%** | Estratégico 25,00% (6/24)
  - **020 (Analítica):** Táctico **88,01%** | Estratégico 25,00% (2/8)
  - **348 (Acueducto):** Táctico **33,98%** | Estratégico 23,48% (27/115)
  - **355 (Core Positiva ARL):** Táctico **48,98%** | Estratégico 7,14% (6/84)
  - **384 (Core Fiduprevisora):** Táctico **66,71%** | Estratégico 19,68% (98/498)
  - **397 (Core Andina):** Táctico **97,06%** | Estratégico 91,18% (52/57 épicas al 100% en prod.)
  - **416 (Core Positiva Vida):** Táctico **29,00%** | Estratégico 0,00% (0/2 ramos)
  - **POS (Consolidado Core Positiva):** Táctico **48,52%** | Estratégico 6,98% (6/86 entregables)
  - **419 (Depósitos Judiciales):** Táctico consolidado maestro en **11,96% ~ 12,0%** (466 funcionalidades); variantes de Azure actualizadas en **63,21%** (DEP) y **58,20%** (RAMA).
  - **420 (Pólizas de Salud):** Táctico **86,73%** | Estratégico 61,40% (35/57)
  - **421 (Balú):** **🔒 CONGELADO / EXCLUIDO** por directriz del usuario en **48,21%** táctico y **21,43%** estratégico (12 de 56 funcionalidades).
  - **453 (Monitoreo CPE):** Táctico **40,00%** | Estratégico 38,16% (29 de 76 casos de uso / items entregados al 100%).
  - **456 (Aeronáutica):** Táctico **24,00%** | Estratégico 16,67% (1 de 6 hitos formalizados).
  - **457 (Portal Web Previsora):** Táctico **96,03%** | Estratégico 92,16% (47/51)
  - **461 (Facturación Electrónica):** Táctico **14,79%** | Estratégico 0,00% (0/32)

* **Actualización Financiera Integral a Corte 09-Nov-2026:**
  - **421 (Balú):** Incorporado `IndicadoresBalu 20261109.xlsx` con Presupuesto plurianual $59.367,5 M, Forecast $42.303,0 M, Costo real acumulado $19.725,9 M, CPI Ppto 1,4509, CPI Forecast 1,0339, ICFF 0,9702, Facturación con IVA $45.305,4 M, Recaudo real $40.346,3 M (96,35% de cumplimiento frente a esperado neto $41.873,0 M) y márgenes neto real 32,9% / directo real 48,1%.
  - **453 (Monitoreo CPE):** Incorporado `Indicadores_CPE 20261109.xlsx` con Presupuesto $1.442,1 M, Forecast $1.547,8 M, Costo real acumulado $1.337,1 M, EVM oficial con avance táctico de 40,00% en 76 casos de uso / items: CPI Ppto 0,4314, CPI Forecast 0,4630, ICFF 1,0538, márgenes directo real -49,0% y neto real -73,9%.
  - **456 (Aeronáutica Civil):** Incorporado `Indicadores456 20261109.xlsx` con Presupuesto $647,0 M, Forecast actualizado a $801,6 M, Costo real acumulado $424,0 M, CPI Ppto 0,3662, CPI Forecast 0,4537, ICFF 1,4820, Facturación con IVA $338,8 M, Recaudo neto al día en $296,9 M (100% cumplimiento) y curva de costos mensuales ajustada (Octubre $76,6 M, Noviembre $87,5 M, Diciembre $201,0 M).
  - **419 (Depósitos Judiciales):** Incorporado `Indicadores_419_V11 20261109.xlsx` con Presupuesto $18.098,6 M, Forecast $10.471,2 M, Costo real acumulado $4.565,0 M, Facturación con IVA $6.712,3 M, Recaudo real acumulado $5.155,1 M (81,10% de cumplimiento sobre recaudo esperado neto de $6.356,4 M, pendiente $1.201,3 M) y márgenes neto real 0,7% / directo real 18,8%.
  - **020 (Analítica de Datos):** Incorporado `020 analitica 20261109.xlsx` con Presupuesto $1.826,8 M, Forecast $1.625,1 M, Costo real acumulado $1.136,6 M. EVM recalculado sobre el avance táctico calibrado de 88,01%: CPI Presupuesto **1,4145** y CPI Forecast **1,2584**. Facturación con IVA $1.821,7 M y Recaudo acumulado de $1.588,3 M (90,83% de cumplimiento sobre esperado neto de $1.748,7 M).

* **Generación del Archivo Excel Maestro de Alineación:**
  - Archivo generado con formato corporativo PMO: `Alineacion_Gestion_CMI_PMO_20261110.xlsx` (en carpeta de trabajo y en Downloads), con 5 hojas estructuradas (`1. Escala Calibrada`, `2. Homologación Azure V2`, `3. Indicadores Portafolio`, `4. Financiero 09-Nov-2026`, `5. Bitácora de Gestión`).

* **Sincronización y Despliegue:**
  - Verificado con `python ACTUALIZAR.py --dry-run` (**0 errores de regex**).
  - Sincronizado en las 4 rutas espejo maestras.
  - Publicado y desplegado a producción en GitHub Pages (`commit ac77485`).

---

## 60. Registro de Ajuste Operativo y Funcional en 348 (SGDEA Acueducto) a Épicas de Certificación (11-nov-2026)

* **Alcance Exclusivo Solicitado:**
  - En la sección *🗂 Funcionalidades por frente · qué HU componen cada una*, el proyecto **348 (SGDEA Acueducto)** se filtró para contemplar **únicamente** las dos épicas contractuales de certificación:
    1. **Certificación Temáticos** (Epic ID 539569): 9 funcionalidades, 279 Historias de Usuario (HUs).
    2. **Certificación CORE** (Epic ID 539200): 11 funcionalidades, 119 Historias de Usuario (HUs).
  - Todas las demás épicas (11 frentes) y sus 95 funcionalidades restantes quedaron excluidas de la vista operativa y del cálculo de los indicadores.

* **Recalibración de Indicadores Táctico y Estratégico PMO:**
  - **Total Funcionalidades Medidas:** **20 funcionalidades** (con 398 HUs en Azure DevOps).
  - **Funcionalidades al 100% (Entregadas en Producción):** **12 funcionalidades**:
    - *Certificación Temáticos (4):* Sistec-EPNT, Conceptos Jurídicos, Historias Clinicas Ocupacionales, Predial.
    - *Certificación CORE (8):* Firmas, RYD, TRD, Archivo Fisico, Expedientes, Prestamos Documental, Comunicado Interno, Acto administrativo.
  - **Distribución en Escala CMI PMO (Buckets):**
    - 100% ✓ (En producción): **12 funcionalidades**
    - 75% (En UAT cliente): **0 funcionalidades**
    - 50% (En curso >80%): **4 funcionalidades** (Sistec-GNET, PQRSD, Calidad y Procesos, Transversal)
    - 20% (En curso 50-80%): **1 funcionalidad** (Correspondencia)
    - % (En curso <50%): **3 funcionalidades** (Gestión del Conocimiento, Acuerdos de gestión, Historias Laborales)
  - **Indicador Táctico Recalculado:** **73,80%** (Promedio ponderado de avance CMI de las 20 funcionalidades).
  - **Indicador Estratégico Recalculado:** **60,00%** (12 de 20 funcionalidades entregadas al 100% formal).

* **Ajustes en Componentes y Tubería de Automatización:**
  - data_func/348.json: Filtrado exclusivamente a las 2 épicas, 20 features y 398 HUs, con KPI y bloque cmi actualizados.
  - data_func.json: Metadata de 348 sincronizada con 20 funcionalidades, 73,80% táctico y 60,00% estratégico.
  - Tablero_CMI_PMO.html:
    - P[348].op: {av:0.7380, ent:12/20, n:20, d:12, u:"funcionalidades", isAzure:true}.
    - PROJ_CALLOUT_META["348"]: 	ag: "Azure · 20 Func.", sub: "20 Funcionalidades en Azure (2 Épicas de Certificación)", ent: "12 en prod.", pct: "60,0% cerrado".
    - VAL["348"]: Aclaración técnica de las 20 funcionalidades bajo Certificación Temáticos y CORE.
  - enrich_func_cmi.py y sync_funcionalidades.py: Incorporada la regla de negocio permanente ilter_348 para garantizar que cualquier futura sincronización desde Tableros preserve automáticamente el filtro a las 2 épicas de certificación.

* **Sincronización y Despliegue:**
  - Verificado con python ACTUALIZAR.py --dry-run (**0 errores de regex**).
  - Sincronizado en las 4 rutas espejo maestras (Indicadores estra y tac/index.html, Indicadores estra y tac/Tablero_CMI_PMO.html, Documents/PMO INDICADORES/CMI/Tablero_CMI_PMO.html, Downloads/Tablero_CMI_PMO.html).
  - Publicado y desplegado a producción en GitHub Pages (commit ea3265e).

---

## 61. Registro de Actualización Exclusiva de la Vista Operativa de 005 (Positiva SGDEA) a Corte 11-Nov-2026

* **Captura Directa de Azure DevOps (11-Nov-2026):**
  - Se incorporó la captura viva de Azure DevOps (HU_005_20261111.csv) para el proyecto **005 - PROYECTO POSITIVA SGDEA 2026 - 3T**.
  - **Volumetría Operativa Actualizada:**
    - **Funcionalidades:** Creció de 24 a **63 funcionalidades** (incorporación formal de frentes y funcionalidades cerradas en Deuda y Evolutivos).
    - **Historias de Usuario (HUs):** Creció de 137 a **250 HUs** (153 HUs terminadas formalmente en producción).
    - **Entregadas en Producción (100%):** Aumentó de 6 a **44 funcionalidades**.
* **Recalibración de Indicadores PMO para 005:**
  - **Indicador Táctico:** Se incrementó de 32,56% a **74,72%**.
  - **Indicador Estratégico:** Se incrementó de 25,00% (6/24) a **69,84%** (44 / 63 funcionalidades al 100%).
  - **Distribución en Buckets CMI:** 100%: 44 | 75%: 2 | 50%: 0 | 20%: 6 | 0%: 11.
* **Preservación Estricta del Resto del Portafolio y de los Indicadores Financieros:**
  - Siguiendo la instrucción estricta del usuario, **no se modificó ningún indicador financiero** de 005 ni del resto de proyectos, manteniendo intactos todos los libros contables, EVM, márgenes y facturación.
  - El resto de proyectos del portafolio (348, 419, 453, 421, 397, 384, POS, 416, 355, 020, 456, 457, 461) no sufrieron alteración alguna.
* **Componentes y Despliegue:**
  - data_func/005.json y data_func.json actualizados al corte 2026-11-11.
  - Tablero_CMI_PMO.html: P[005].op ({av: 0.7472, ent: 44/63, n: 63, d: 44}), callout Azure · 63 Func. (44 en prod. · 69,8% cerrado) y fecha operativa 11-Nov-2026.
  - Sincronizado en las 4 rutas espejo maestras y publicado en GitHub Pages (commit ead5e94).


---

## 62. Registro de Certificación y Blindaje Permanente de 421 (Balú): Exclusión Estricta de Épicas Transversales y Automatización QA

* **Regla de Gobernanza de Producto para Balú 421:**
  - El alcance operativo y contractual de **421 - PROYECTO BALÚ** se mide única y exclusivamente sobre sus **2 Frentes de Producto de cara al cliente**:
    1. **Afiliaciones y Novedades:** 29 funcionalidades de producto.
    2. **Sistema de Recaudo y Cartera:** 27 funcionalidades de producto.
    - **Total oficial de Producto:** **56 funcionalidades**.
  - **Exclusión Estricta y Permanente:** Quedan 100% excluidas de cualquier cálculo, visualización, tabla jerárquica y descarga de datos las épicas:
    - `Funcionalidades Transversales` (10 funcionalidades excluidas).
    - `Automatización_QA Balu` / `Automatización QA Balu` (2 funcionalidades excluidas).

* **Blindaje en la Tubería de Automatización y Datos:**
  - **`sync_funcionalidades.py`:** Incorporada la función `filter_421(target_dir)` que se ejecuta automáticamente tras copiar desde Tableros, asegurando que `data_func/421.json` y `data_func.json` queden purgados a 2 épicas, 56 funcionalidades y sus 867 HUs activas.
  - **`enrich_func_cmi.py`:** Filtra los frentes antes de calcular los CMI e inyecta el `kpi` depurado en `index_data['proyectos']['421']`.
  - **`Tablero_CMI_PMO.html`:**
    - `FR["421"]`: Ajustado a `[["Afiliaciones y Novedades",29,0.5],["Sistema de Recaudo y Cartera",27,0.2]]` (56 func en 2 frentes).
    - `fncBody(C)`: Doble filtro en JavaScript para que la tabla interactiva ignore cualquier frente transversal o de automatización.
    - `fncCsv(cod)`: Exportación CSV restringida exclusivamente a las 56 funcionalidades de producto.
    - `PROJ_CALLOUT_META["421"]`: `Azure · 56 Func.` (13 en prod. · 23,2% cerrado).
    - `P[421].op`: `{av: 0.7488, ent: 13/56, n: 56, d: 13, u: "funcionalidades"}`.

* **Métricas Oficiales Certificadas al Corte:**
  - **Indicador Táctico:** **74,88%** (Promedio del % táctico de las 56 funcionalidades de producto).
  - **Indicador Estratégico:** **23,21%** (13 de 56 funcionalidades cerradas al 100%).
  - **HUs Activas Evaluadas:** **867 HUs** (100% prod: 469 | 75% UAT: 185 | 50%: 0 | 20% QA: 60 | 0% Dev: 153).
  - **RQC 421:** **48,41%** (305 / 630 activos cumplidos, 283 removidos).
  - **Indicador de Éxito Balú:** **48,38%** (30% Táctico + 40% RQC + 30% Cronograma).


---

## 63. Registro de Blindaje y Auditoría Arquitectónica Integral, Limpieza de Reglas y Saneamiento del Repositorio (12-Nov-2026)

* **Diagnóstico de Brechas y Causa Raíz de Desajustes:**
  - Se identificó que scripts históricos (`ACTUALIZAR.py`) conservaban lógica rígida que intentaba sobreescribir frentes y métricas de proyectos certificados (como 348 con 95 frentes antiguos de octubre, o 419) a partir de libros consolidados obsoletos, compitiendo contra la tubería moderna de Azure DevOps.
  - Se detectó acumulación de más de 10 scripts temporales de prueba (`check_*.py`, `test_run.py`, `inspect_*.py`, etc.) en la raíz del espacio de trabajo.
  - En el repositorio GitHub Pages (`Indicadores estra y tac`) existían archivos `.xlsx` y cachés `__pycache__` ignorados que generaban desorden visual.

* **Blindaje y Refactorización Arquitectónica:**
  - **`verify_cmi_architecture.py` (Nuevo Guardián de Arquitectura):**
    - Módulo de auditoría integral automatizado en 5 dimensiones:
      1. *Integridad Estructural:* Declaración estricta de `const FR=...; const BOOK416=`, `let FIN=`, `PROJ_CALLOUT_META`, `BUGS_419_DATA`, `#sem-op`, `#fncBody`, `updateTopOpTiles`.
      2. *Reglas de Negocio Certificadas:* Validación de métricas oficiales de 005 (63 func / 44 prod · 74,72% / 69,84%), 348 (20 func / 17 prod · 90,85% / 85,00%), 421 (56 func · 74,88% / 23,21%), 419 (466 func · 11,96% / 17,17%), 456 (2 columnas obligatorias) y 397 (57 épicas).
      3. *Tubería JSON:* Integridad y consistencia de `data_func.json`, `data_453_cpe.json`, `data_rqc.json` y los JSON individuales de `data_func/`.
      4. *Sincronía de Visuales:* Verificación MD5 estricta entre las 3 visuales (`index.html`, `master.html`, `consulta.html`) en el repositorio y en local.
      5. *Limpieza de Espacio de Trabajo:* Asegura que no queden scripts de depuración en la raíz.
  - **`ACTUALIZAR.py` Protegido:**
    - Se eliminó la sobreescritura destructiva de `FR["348"]`, protegiendo la gobernanza de 348 desde Azure DevOps.
    - Se incorporó la validación final mediante `verify_cmi_architecture.py`.
  - **`actualizar_todo.py` Unificado:**
    - Integra la auditoría de arquitectura como compuerta de paso obligatoria: si la auditoría detecta cualquier desalineación, se cancela automáticamente la publicación a producción (`git push`) para evitar desajustes en GitHub Pages.

* **Limpieza Exhaustiva y Organización:**
  - **Espacio de Trabajo PMO (`Documents/PMO INDICADORES/CMI`):**
    - Todos los scripts de prueba (`check_diff_rf.py`, `check_dim.py`, `check_mockup_mode.py`, `check_modes.py`, `check_opcards.py`, `check_syntax.py`, `inspect_020_hus.py`, `inspect_348_target_epics.py`, `show_5_objs.py`, `test_run.py`, `temp_test.js`, `apply_financial_updates_all_projects.py`) fueron archivados ordenadamente en la carpeta `scratch/`.
    - La raíz queda compuesta exclusivamente por los archivos y scripts maestros de producción.
  - **Repositorio GitHub (`Indicadores estra y tac`):**
    - Eliminadas las cachés `__pycache__` y los archivos `.xlsx` huérfanos que estaban en `.gitignore`.
    - Repositorio con árbol de trabajo 100% limpio (`working tree clean`).
  - **`REGLAS_DE_NEGOCIO_CMI.md`:**
    - Matriz maestra actualizada al corte vigente con la totalidad de los 13 proyectos y sus casuísticas particulares.

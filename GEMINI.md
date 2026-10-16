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
1. `c:\Users\Usuario1\Indicadores estra y tac\index.html` (Punto de entrada web para GitHub Pages).
2. `c:\Users\Usuario1\Indicadores estra y tac\Tablero_CMI_PMO.html` (Copia local de trabajo).
3. `C:\Users\Usuario1\Documents\PMO INDICADORES\CMI\Tablero_CMI_PMO.html` (Copia maestra del usuario).
4. `C:\Users\Usuario1\Downloads\Tablero_CMI_PMO.html` (Copia de consulta rápida).

---

## 4. Restricciones Críticas y Compatibilidad de Automatización
1. **Script de Automatización `ACTUALIZAR.py`:**
   * Ubicación: `C:\Users\Usuario1\Documents\PMO INDICADORES\CMI\ACTUALIZAR.py`.
   * **REGLA ESTRICTA:** El script busca la declaración de datos mediante la expresión regular:
     `FR_PATTERN = re.compile(r"const FR=(\{[\s\S]*?\});\s*const BOOK416=")`
     Bajo ninguna circunstancia se debe romper la línea de código `const FR=...; const BOOK416=`.
   * Antes de hacer push, siempre verificar con:
     `python "C:\Users\Usuario1\Documents\PMO INDICADORES\CMI\ACTUALIZAR.py" --dry-run`

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
Copy-Item "c:\Users\Usuario1\Indicadores estra y tac\index.html" "c:\Users\Usuario1\Indicadores estra y tac\Tablero_CMI_PMO.html" -Force
Copy-Item "c:\Users\Usuario1\Indicadores estra y tac\index.html" "C:\Users\Usuario1\Documents\PMO INDICADORES\CMI\Tablero_CMI_PMO.html" -Force
Copy-Item "c:\Users\Usuario1\Indicadores estra y tac\index.html" "C:\Users\Usuario1\Downloads\Tablero_CMI_PMO.html" -Force

# 2. Validar con el script de actualización
python "C:\Users\Usuario1\Documents\PMO INDICADORES\CMI\ACTUALIZAR.py" --dry-run

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


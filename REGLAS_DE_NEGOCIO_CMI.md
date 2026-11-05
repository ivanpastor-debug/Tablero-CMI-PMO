# Reglas de Negocio · Tablero de Control Estratégico y Táctico (CMI) PMO

## 1. Propósito y Alcance del Tablero
El Tablero CMI PMO es el instrumento ejecutivo y táctico para la supervisión integral de proyectos estratégicos de Linktic. Consolida en una vista unificada tres dimensiones de control:
1. **Dimensión Operativa / Táctica:** Nivel de avance en el ciclo de vida de desarrollo de software y construcción de entregables.
2. **Dimensión Estratégica / Contractual:** Porcentaje de cumplimiento formal frente a los compromisos entregados y aceptados formalmente por el cliente.
3. **Dimensión Financiera y de Costos (EVM):** Valor contractual, facturación con/sin IVA, recaudo, control de costos, índices de desempeño ($CPI_P$, $CPI_F$, $ICFF$), nómina y márgenes de rentabilidad.

---

## 2. Gobernanza de Indicadores Operativos CMI

### 2.1. Escala Oficial CMI por Entregable PMO
Cada unidad de medición contractual es evaluada bajo los 5 cubos de la escala oficial de entregables:
* **`100,00%` (1.00):** **Entregado / En Producción.** Ítems formalmente recibidos, desplegados en producción o con avance ponderado $\ge 99,9\%$.
* **`75,00%` (0.75):** **En Pruebas UAT del Cliente.** Funcionalidades en proceso de validación o aceptación formal.
* **`50,00%` (0.50):** **En Curso > 80%.** Funcionalidades en desarrollo/QA avanzado con avance superior al 80%.
* **`20,00%` (0.20):** **En Curso 50% – 80%.** Funcionalidades en construcción con avance en rango medio.
* **`0,00%` (0.00):** **En Curso < 50% / Inicial.** Funcionalidades en levantamiento, diseño o avance inferior al 50%.

### 2.2. Indicador Táctico (% de Avance Ponderado)
* **Definición:** Refleja el avance real en la tubería de construcción según el estado de madurez de cada entregable.
* **Fórmula:**
  $$\text{Indicador Táctico} = \frac{\sum_{i=1}^{n} \text{Valor en Escala CMI}(E_i)}{n}$$
  *(Donde $E_i$ es el entregable $i$ y $n$ es el total de entregables medibles).*

### 2.3. Indicador Estratégico (% de Cumplimiento Contractual)
* **Definición:** Proporción de entregables completados formalmente al 100% sobre el alcance contractual total comprometido.
* **Fórmula:**
  $$\text{Indicador Estratégico} = \frac{\text{Entregables al 100\% (en producción / formalmente entregados)}}{\text{Total de entregables comprometidos}} = \frac{d}{n}$$

### 2.4. Unidad Oficial de Gobierno
* **Regla General:** Para proyectos en Azure DevOps, la unidad contractual de gobierno CMI se mide sobre las **Épicas (Epics / Frentes)**.
* **Desglose de Soporte:** En callouts y fichas de detalle se presenta la trazabilidad técnica viva de **Funcionalidades (Features)** e **Historias de Usuario (HU)**, sin alterar la unidad oficial de gobierno.

---

## 3. Reglas Específicas y Excepciones por Proyecto

| Proyecto | Unidad de Gobierno CMI | Indicador Táctico | Indicador Estratégico | Regla de Negocio Específica |
| :--- | :---: | :---: | :---: | :--- |
| **005** · Positiva SGDEA 2026 - 3T | **13 Épicas** | `26,15%` | `23,08%` (3/13) | Conexión directa a Azure DevOps. Desglose complementario de 41 funcionalidades (7 en producción). |
| **POS** · Core Positiva (Consolidado) | **20 Épicas** | `23,90%` | `0,00%` (0/20) | Integra subproyecto 355 (18 épicas, avance `23,33%`) y subproyecto 416 (2 épicas, avance `29,00%`). Comparte libro financiero consolidado (carpeta 416). |
| **384** · Core Fiduprevisora | **33 Épicas** | `42,42%` | `3,03%` (1/33) | Evaluado sobre las 33 épicas válidas de Azure DevOps con desglose técnico de >500 funcionalidades (90 en producción). |
| **419** · Depósitos Judiciales | **466 Funcionalidades** | `11,96%` | `17,17%` (80/466) | **Excepción Oficial PMO:** Se rige por el archivo maestro local PMO (80 certificadas de 466). **Exclusión estricta:** Se descarta la épica interna `▾ 419DPJ_EP_LT_Seguimiento_Transversal_Linktic` (`id: 327682`, 5 func.) por ser control interno. En paralelo visualiza 194 func. en Azure (DEP + RAMA) y auditoría de 1.836 bugs con ANS de 3 días y liquidación comercial. |
| **453** · Monitoreo CPE 2026 | **71 Casos de Uso** | `47,85%` | `39,44%` (28/71) | **Medición Exclusiva por Casos de Uso:** Evalúa el campo Estado Interno `estados_453`. Excluye CUs en `10. Transversal`. Incorpora Focos (A, B, C, D) con Línea Base vs Reprogramada y releases por iteración. |
| **456** · Innovación Aeronáutica | **6 Entregables Contractuales** | `24,00%` | `16,67%` (1/6) | **Supervisión Contractual en 3 Fases:** 6 hitos (1 al 100%, 1 al 50%). **Regla de Interfaz:** Ficha operativa en **dos columnas lado a lado (`g-2`)** (Columna 1: Escala CMI + Columna 2: Desviación del Cronograma) y debajo el árbol vivo de Azure (1 épica, 4 func., 16 HU). |
| **348** · SGDEA Acueducto | **10 Épicas** | `25,29%` | `10,00%` (1/10) | 10 épicas contractuales (1 al 100%: *Assesment de Madurez*). Desglose técnico de 115 funcionalidades (26 en producción). |
| **397** · Core Andina | **57 Épicas** | `97,06%` | `91,18%` (52/57) | Medición formal sobre 57 épicas (52 cerradas) con soporte de 233 funcionalidades (228 en producción · 97,9% cerrado). |
| **421** · BALÚ | **2 Frentes** | `35,00%` | `0,00%` (0/2) | Medición contractual sobre *Afiliaciones y Novedades* (50%) y *Recaudo y Cartera* (20%). |
| **457** · Portales La Equidad | **5 Épicas** | `64,00%` | `40,00%` (2/5) | Ingesta por Captura Directa desde Azure DevOps (`opOnly: true`). 2 épicas al 100% (*Portal Formación* y *Portal Clientes*). |
| **020** · Servicios de Analítica | **2 Épicas** | `50,00%` | `0,00%` (0/2) | Ingesta por Captura Directa desde Azure DevOps (`opOnly: true`). 2 épicas activas (*OPERACIÓN* al 86,98% y *SOPORTE* al 94,44% en Escala CMI 50%). |
| **461** · Cuentas Claras CNE | **7 Épicas** | `8,57%` | `0,00%` (0/7) | Ingesta por Captura Directa desde Azure DevOps (`opOnly: true`). 3 épicas en Escala CMI 20% y 4 en 0%. Soporte de 32 features y 108 HU activas. |

### 3.1. Marco de Gestión de Defectos (Bugs), Curva ANS y Liquidación Comercial en Proyecto 419 (Depósitos Judiciales)
En el marco de la supervisión integral de Depósitos Judiciales, el proyecto incorpora un módulo especializado para la gobernanza de defectos técnicos (Bugs) con las siguientes reglas de negocio:

1. **Segmentación de Variantes Operativas (Bug´s de Desarrollo - Fuente de información Azure DevOps Linktic):**
   * La medición de defectos se divide en dos frentes operacionales con dinámicas de desarrollo independientes:
     * **Depósitos Judiciales (BAC - Banco Agrario de Colombia):** 1.265 bugs (68,9% del volumen global).
     * **Rama Judicial:** 571 bugs (31,1% del volumen global).
   * **Universo Total Auditado:** 1.836 work items de tipo Bug consolidados con doble validación al 100% en Azure DevOps.

2. **Compromiso Contractual y Tiempos de Respuesta (ANS):**
   * **Meta ANS Contractual:** Tiempo máximo de resolución esperado $\le 3,0$ días hábiles.
   * **Tiempo Promedio Global:** 15,2 días de resolución (con una mediana de 6,7 días).
   * **Fórmula de Brecha ANS por Sprint:**
     $$\text{Brecha ANS} = T_{\text{cons}} - 3,0\text{ días}$$
     *(Donde $T_{\text{cons}}$ es el tiempo promedio ponderado de resolución del sprint).*
   * **Criterio Semafórico ANS:**
     * **Verde (`good`):** *Cerca al ANS* ($\le 6,0\text{ d}$, brecha $\le +3,0\text{ d}$).
     * **Amarillo (`warn`):** *Fuera de ANS Moderado* ($> 6,0\text{ d}$ y $\le 8,0\text{ d}$, brecha entre $+3,1\text{ d}$ y $+5,0\text{ d}$).
     * **Rojo (`crit`):** *Fuera de ANS Crítico* ($> 8,0\text{ d}$, brecha $> +5,0\text{ d}$).

3. **Curva de Eficiencia Operativa (S1 ➔ S7):**
   * El indicador evalúa la evolución de los tiempos entre el arranque del proyecto y el sprint vigente:
     $$\text{Reducción de Tiempo} = \frac{T_{\text{S1}} - T_{\text{S7}}}{T_{\text{S1}}} \times 100 = \frac{25,0\text{ d} - 5,4\text{ d}}{25,0\text{ d}} \times 100 = 78,4\%$$
   * Esta reducción del **78,4%** en tiempos de atención certifica la curva de aprendizaje, estabilización de código y madurez en la mesa de soporte.

4. **Reglas de Conciliación de Bug´s con Reportados por Cliente (Rango B59:F63):**
   * Los defectos reportados se someten a mesas de conciliación técnica periódicas con el cliente (Banco Agrario / Rama Judicial) para definir los defectos imputables y su liquidación económica:
     * **Sprint 01:** 406 bugs Linktic $\rightarrow$ **$35.000.000 COP** (Conciliado y Facturado).
     * **Sprint 02:** 175 bugs Linktic $\rightarrow$ **$21.000.000 COP** (Conciliado y Facturado).
     * **Sprint 03:** 309 bugs Linktic vs 188 cliente (69 bugs formalmente acordados) $\rightarrow$ **$74.000.000 COP** (Conciliado y Facturado).
     * **Subtotal Facturado/Liquidado:** **$130.000.000 COP**.
     * **Sprint 04:** 231 bugs Linktic vs 250 cliente $\rightarrow$ En proceso de concertación (*Mesa Técnica en Curso*).

5. **Auditoría de Testigos en Azure DevOps:**
   * Toda cifra y estado conciliado cuenta con respaldo en work items específicos tipo Bug registrados en Azure DevOps (con ID, título, fecha de creación `fc`, fecha de resolución `fr`, severidad y tiempo efectivo transcurrido), garantizando trazabilidad y transparencia contractual.

---

## 4. Reglas Operativas y Tratamiento de Work Items (Azure DevOps)

1. **Depuración de HU Activas:**
   * Solo suman al cálculo las Historias de Usuario activas. Se descartan ítems en estados `EXCLUIR`, `OMITIR`, `X. Removido` o en papelera.
   * Las HU removidas no aportan al numerador ni al denominador del avance.
2. **Cálculo de Avance de Funcionalidades:**
   * El % de avance de una funcionalidad es el promedio aritmético ponderado de sus HUs activas hijas. Si no cuenta con HUs con avance, se registra como `null`.
3. **Consistencia Jerárquica del Árbol:**
   * Toda HU debe pertenecer a una funcionalidad existente, y toda funcionalidad a una Épica visible. Los ítems sin asignación se agrupan bajo `(sin frente)` para visibilidad del 100% de la carga.

---

## 5. Reglas Financieras y Gestión del Valor Ganado (EVM)

### 5.1. Tratamiento del IVA y Cifras Contractuales
* **Conmutador Global `Sin IVA` / `Con IVA`:** Permite evaluar el contrato, plan de facturación y facturación real en valor neto o con el 19% de IVA aplicado.

### 5.2. Bloque de Costos (`costBlock`)
* **Dimensiones Comparativas:** Presupuesto (`PPTO`), Proyección (`FCST`) y Costo Ejecutado (`REAL`).
* **Variaciones:** `FCST vs PPTO`, `REAL vs PPTO` y `REAL vs FCST`.
* **Indicador de Ejecución Presupuestal:**  
  * **`Ejecución REAL/PPTO`:** Relación porcentual entre el costo real acumulado y el presupuesto asignado ($\text{REAL} / \text{PPTO}$).
  * **`Cumpl. REAL / FCST`:** Relación porcentual entre el costo real y el forecast proyectado ($\text{REAL} / \text{FCST}$).

### 5.3. Índices de Desempeño EVM (`evmCard`)
* Se presentan dos escenarios independientes de evaluación de eficiencia: **Escenario PPTO** y **Escenario FCST**.
* **Fórmula del CPI (Cost Performance Index):**
  $$\text{CPI} = \frac{\text{EV · Costo total ejecutado}}{\text{AC · Costo real acumulado}}$$
  *(Donde el numerador representa el valor ganado medido por el costo ejecutado correspondiente al avance físico, y el denominador el costo real devengado).*
* **ICFF (Índice de Cumplimiento Financiero):**
  $$\text{ICFF} = \frac{\text{Valor Facturado}}{\text{Costo Real Incurrido}}$$
* **Semáforos de Rendimiento Financiero:**
  * **Verde:** $\text{CPI} \ge 1.0$ (eficiencia en costos / bajo presupuesto).
  * **Amarillo:** $0.85 \le \text{CPI} < 1.0$ (desviación controlada).
  * **Rojo:** $\text{CPI} < 0.85$ (sobrecosto crítico).

---

## 6. Reglas de Trazabilidad y Fechas de Actualización

1. **Doble Fecha de Corte Independiente:**
   * **Fecha Operativa:** Fecha del último corte de snapshots / sincronización de Azure DevOps por proyecto (ej. `29-Oct-2026`).
   * **Fecha Financiera:** Fecha oficial de los libros Excel financieros locales (ej. `01-Oct-2026` o `07-Oct-2026`).
2. **Proyectos Solo Operativos (`opOnly: true`):**
   * Aquellos proyectos sin libro financiero cargado en `Información Financiera` (ej. 457, 020) muestran la nota aclaratoria `finNote` y no alteran los totales consolidados de facturación, costos ni caja del portafolio.

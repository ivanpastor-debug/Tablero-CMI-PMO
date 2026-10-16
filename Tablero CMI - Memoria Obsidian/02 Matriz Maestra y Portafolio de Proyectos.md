---
title: Matriz Maestra y Portafolio de Proyectos PMO
tags:
  - pmo
  - cmi
  - portafolio
  - proyectos
  - entregables
---

# 📋 Matriz Maestra y Portafolio de Proyectos PMO

> [!INFO] Alcance del Portafolio
> Supervisión de los 9 proyectos estratégicos de la PMO al corte oficial del `01-Oct-2026`.

---

## 1. Tabla Maestra de Indicadores Operativos y Financieros

| Código PMO | Nombre Oficial del Proyecto | Cliente / Entidad | Unidad de Medición | Indicador Táctico | Indicador Estratégico | Volumetría Azure / Contrato | Valor Contrato (Sin IVA) | Facturado (Sin IVA) |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :---: | :---: |
| **005** | `005 - PROYECTO POSITIVA SGDEA 2026 - 3T` | Función Pública / MinTrabajo | **18 Épicas** | **50,56%** | **38,89%** | 7 de 18 Épicas · 77 Func · 43 en prod (55,8%) | $3.986 M | $1.536 M (38,5%) |
| **416 / POS** | `416 - PROYECTO DE DESARROLLO Y SOPORTE CORE POSITIVA` | Positiva Compañía de Seguros | **20 Épicas** | **21,85%** | **0,00%** | 0 de 20 Épicas · 87 Func · 6 en prod (6,9%) | $6.067 M | $1.739 M (28,7%) |
| ↳ *355* | *Subproyecto 355 · Positiva Core* | Positiva Seguros | 18 Épicas | 21,05% | 0,00% | 0 de 18 Épicas · 80 Func · 6 en prod (7,5%) | *(Libro 416)* | *(Libro 416)* |
| ↳ *416* | *Subproyecto 416 · Evolutivos* | Positiva Seguros | 2 Épicas | 29,00% | 0,00% | 0 de 2 Épicas · 7 Func · 0 en prod (0,0%) | *(Libro 416)* | *(Libro 416)* |
| **384** | `384 - PROYECTO CORE FIDUPREVISORA` | Fiduprevisora S.A. | **32 Épicas** | **42,19%** | **3,12%** | 1 de 32 Épicas · 543 Func · 155 en prod (28,6%) | $21.017 M | $2.380 M (11,3%) |
| **419** | `419- DEPOSITOS JUDICIALES` | Banco Agrario / Rama Judicial | **466 Func.** *(Local)* | **12,01%** | **26,82%** | 125 de 466 Certificadas · 168 Func en Azure (35,7%) | $28.493 M | $5.227 M (18,3%) |
| **421** | `421 - PROYECTO BALÚ` | Fiduprevisora · Afiliaciones | **2 Frentes** | **35,00%** | **0,00%** | 0 de 2 Frentes · 66 Func · 19 en prod (28,8%) | $100.945 M | $38.249 M (37,9%) |
| **453** | `453 - PROYECTO MONITOREO DE EQUIPOS CPE 2026` | MinEducación · CPE | **45 Casos de Uso** | **30,30%** | **8,89%** | 4 de 45 CUs entregados (Estado 19) | *Sin contrato* | *Sin facturación* |
| **456** | `456 - PROYECTO INNOVACION AEREONAUTICA CIVIL` | Aeronáutica Civil | **6 Hitos Contractuales** | **24,00%** | **16,67%** | 1 de 6 Hitos (Entregable I Fase I) | $1.582 M | $284 M (18,0%) |
| **348** | `348 - PROYECTO SGDEA ACUEDUCTO` | EAAB (Acueducto Bogotá) | **10 Épicas** | **25,29%** | **10,00%** | 1 de 10 Épicas · 95 Func · 15 en prod (15,8%) | $11.031 M | $3.517 M (31,9%) |
| **397** | `397 - PROYECTO CORE ANDINA` | Andina Seguros (Colfondos) | **57 Épicas** | **97,06%** | **91,18%** | 52 de 57 Épicas · 233 Func · 228 en prod (97,8%) | $1.450 M | $1.392 M (96,0%) |

---

## 2. Fichas de Identidad y Excepciones Clave

### 397 · PROYECTO CORE ANDINA
- **Cliente Oficial:** Andina Seguros (antiguo cruce con Colfondos/Previsora corregido).
- **Gobernanza:** 57 Épicas contractuales (52 al 100%). Desglose técnico de 233 Features en Azure (228 cerradas).
- **Financiero:** CPI fcst 1,02, facturación al 96% con recaudo neto al 100%.

### 453 · PROYECTO MONITOREO DE EQUIPOS CPE 2026
- **Medición Exclusiva por Casos de Uso:** 45 CUs medibles en 4 focos. 4 CUs en estado `19. Entregado` (100%).
- **Conmutador Metodológico:** Filtro por **Ejecución** (iteración real de las HU) vs **Compromiso** (iteración comprometida del Caso de Uso).

### 419 · 419- DEPOSITOS JUDICIALES
- **Excepción Local PMO:** Conserva el indicador táctico (12,01%) y estratégico (26,82% = 125/466) del archivo maestro local.
- **Trazabilidad Azure:** 168 Funcionalidades (60 en prod · 35,7% cerrado) mostradas inmediatamente antes de la gráfica de certificaciones.

### 456 · PROYECTO INNOVACION AEREONAUTICA CIVIL
- **Estructura Especial:** 2 columnas lado a lado (`g-2`): Columna 1 (*Escala CMI por fase*) + Columna 2 (*Desviación del Cronograma Contractual*).
- **Desviación:** Desplazamiento del cierre contractual de 30-dic-2026 al 28-ene-2027 (+29 días cal.), generando cruce de vigencia fiscal.

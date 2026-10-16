---
title: Marco Metodológico · Escala CMI y Gobernanza de Entregables
tags:
  - pmo
  - cmi
  - metodologia
  - escala-entregables
  - formulas
---

# 🎯 Marco Metodológico · Escala CMI y Gobernanza de Entregables

> [!INFO] Definición
> El Cuadro de Mando Integral (CMI) evalúa la salud operativa de cada proyecto midiendo el avance ponderado de sus entregables frente al cliente formal.

---

## 1. La Escala CMI Oficial por Entregable

Cada entregable del proyecto se califica dentro de **5 cubos estandarizados**:

```mermaid
flowchart LR
    C0["0,00%<br>En curso <50%"] --> C20["20,00%<br>En curso 50–80%"]
    C20 --> C50["50,00%<br>En curso >80%"]
    C50 --> C75["75,00%<br>En UAT cliente"]
    C75 --> C100["100,00% ✓<br>En producción"]

    style C0 fill:#ef4444,stroke:#b91c1c,color:#fff
    style C20 fill:#f97316,stroke:#c2410c,color:#fff
    style C50 fill:#f59e0b,stroke:#b45309,color:#fff
    style C75 fill:#0284c7,stroke:#0369a1,color:#fff
    style C100 fill:#10b981,stroke:#047857,color:#fff
```

### Reglas de Clasificación Técnica:
- **`100,00%` ✓:** En producción ($\text{pct} \ge 0.999$).
- **`75,00%`:** En pruebas UAT del cliente.
- **`50,00%`:** En curso $>80\%$ ($\text{pct} > 0.80$).
- **`20,00%`:** En curso $50\text{--}80\%$ ($\text{pct} \ge 0.50$).
- **`0,00%`:** En curso $<50\%$ ($\text{pct} < 0.50$).

---

## 2. Formulación Matemática de Indicadores

### 2.1 Indicador Táctico (% de Avance)
Es la media aritmética del puntaje obtenido por cada entregable bajo la escala:

$$\text{Indicador Táctico} = \frac{1}{N} \sum_{i=1}^{N} \text{Escala}(E_i)$$

Donde:
- $N$ es el total de entregables del proyecto.
- $\text{Escala}(E_i) \in \{0.00, 0.20, 0.50, 0.75, 1.00\}$.

### 2.2 Indicador Estratégico (% de Cumplimiento)
Porcentaje de entregables que ya han sido puestos en producción formalmente:

$$\text{Indicador Estratégico} = \frac{\text{Entregables al 100\% (en Producción)}}{\text{Total de Entregables Contractuales}} = \frac{D}{N}$$

---

## 3. Gobernanza de Entregables por Tipo de Proyecto

| Proyecto | Unidad Oficial de Entregable CMI | Justificación y Regla Metodológica |
| :--- | :---: | :--- |
| **005, POS, 384, 421, 348, 397** | **Épicas (Epics / Frentes)** | Se gobiernan contractualmente a nivel de Épicas de Azure DevOps, con trazabilidad simultánea a las funcionalidades (Features) componentes. |
| **453 CPE 2026** | **Casos de Uso (CUs)** | Excepción oficial: Se mide frente a 45 Casos de Uso evaluados por su Estado Interno (`estados_453`). No se mide sobre HUs. |
| **456 Aeronáutica** | **6 Hitos Contractuales** | Supervisión contractual en 3 fases metodológicas (Fase I, II-1, II-2) y tabla de desviación del cronograma. |
| **419 Depósitos** | **466 Funcionalidades (Archivo Local)** | Excepción oficial PMO: Mantiene los 125 entregados sobre 466 del archivo maestro local, con seguimiento a sus 168 Features en Azure. |

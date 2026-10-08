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


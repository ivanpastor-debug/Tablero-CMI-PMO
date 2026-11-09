# 🔐 Directorio Oficial de Claves · Tablero CMI PMO

Este documento contiene el directorio confidencial de **claves de acceso (Keys)** para la **Visual Espejo** (`consulta.html`) y la **Visual Administradora** del Tablero de Control Estratégico y Táctico de la PMO.

---

## 👑 1. Master Key PMO (Acceso Total de Dirección)

| Rol / Alcance | Clave Predeterminada (Key) | Nivel de Acceso |
| :--- | :--- | :--- |
| **Dirección PMO / Administrador Global** | `PMO-MASTER-2026*` | **Total (Portafolio, EVM, Finanzas y todos los proyectos)** |

*Al ingresar `PMO-MASTER-2026*` en `consulta.html`, se desbloquea la totalidad de los proyectos y las métricas consolidadas del portafolio.*

---

## 🛡️ 2. Directorio de Claves por Proyecto (Visual Espejo para Clientes)

Cada cliente o líder técnico utiliza su clave única para consultar **exclusivamente la información de su proyecto**, sin tener acceso a cifras contractuales ni avances de otros clientes.

| Código PMO | Proyecto Oficial | Cliente / Entidad | Clave Predeterminada (Key) |
| :---: | :--- | :--- | :--- |
| **005** | 005 - PROYECTO POSITIVA SGDEA 2026 - 3T | Positiva Compañía de Seguros | `POS-005-SGDEA` |
| **POS** | 416 - PROYECTO CORE POSITIVA (Consolidado) | Positiva Compañía de Seguros | `POS-CORE-GLOBAL` |
| **355** | Positiva Core · Subproyecto 355 | Positiva Compañía de Seguros | `POS-355-CORE` |
| **416** | 416 - Subproyecto Evolutivos Core | Positiva Compañía de Seguros | `POS-416-CORE` |
| **384** | 384 - PROYECTO CORE FIDUPREVISORA | Fiduprevisora | `FIDU-384-CORE` |
| **419** | 419- DEPOSITOS JUDICIALES | Banco Agrario / Rama Judicial | `DEP-419-JUDICIAL` |
| **421** | 421 - PROYECTO BALÚ | Fiduprevisora | `BALU-421-RECAUDO` |
| **453** | 453 - PROYECTO MONITOREO DE EQUIPOS CPE 2026 | Computadores para Educar (CPE) | `CPE-453-MONITOR` |
| **456** | 456 - PROYECTO INNOVACION AEREONAUTICA CIVIL | Aeronáutica Civil | `AERO-456-INNOV` |
| **348** | 348 - PROYECTO SGDEA ACUEDUCTO | Empresa de Acueducto de Bogotá (EAAB) | `EAAB-348-SGDEA` |
| **397** | 397 - PROYECTO CORE ANDINA | Andina Seguros | `ANDI-397-CORE` |
| **457** | 457 - PROYECTO PORTALES DIGITALES INTEGRADOS | La Equidad Seguros | `EQUI-457-PORTAL` |
| **020** | 020 - PROYECTO SERVICIOS DE ANALITICA | Positiva Compañía de Seguros | `POS-020-DATA` |
| **461** | 461 - PROYECTO CUENTAS CLARAS | Consejo Nacional Electoral (CNE) | `CNE-461-CUENTAS` |
| **420** | 420 - PROYECTO PÓLIZAS DE SALUD | Positiva Compañía de Seguros | `POS-420-SALUD` |

---

## 🌐 3. Enlaces Públicos en Producción

* **Visual Administradora (Completa):**  
  👉 **https://ivanpastor-debug.github.io/Tablero-CMI-PMO/**  
  *(Contiene el 100% de la información operativa, estratégica y financiera del portafolio)*.

* **Visual Espejo (Protegida por Clave por Proyecto):**  
  👉 **https://ivanpastor-debug.github.io/Tablero-CMI-PMO/consulta.html**  
  *(Solicita la clave correspondiente para desbloquear únicamente el proyecto consultado)*.

---

## 🔒 4. Seguridad y Criptografía

1. Las claves no se almacenan en texto plano en la aplicación web; se comparan mediante resúmenes **SHA-256 criptográficos estándar** en el navegador (`crypto.subtle`).
2. Al ingresar la clave de un proyecto, la aplicación bloquea en memoria las referencias y componentes visuales de los otros proyectos del portafolio.
3. La sesión queda guardada de forma segura en `sessionStorage` hasta que el usuario hace clic en **"Cerrar Sesión"** o cierra la pestaña del navegador.

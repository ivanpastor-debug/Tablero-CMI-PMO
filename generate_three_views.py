# -*- coding: utf-8 -*-
"""
Generador y Sincronizador de las Tres Visuales PMO:
1. Vista Libre Actual: index.html / Tablero_CMI_PMO.html
2. Master PMO: master.html
3. Vista con Key por Proyecto: consulta.html
"""

import hashlib
import os
import re
import shutil
from pathlib import Path

# Directorio de claves predeterminadas
KEYS_DIRECTORY = {
    "MASTER": ("PMO-MASTER-2026*", "Master PMO (Dirección y Control Total)"),
    "005": ("POS-005-SGDEA", "005 - PROYECTO POSITIVA SGDEA 2026 - 3T"),
    "POS": ("POS-CORE-GLOBAL", "416 - PROYECTO DE DESARROLLO Y SOPORTE CORE POSITIVA (Consolidado)"),
    "355": ("POS-355-CORE", "Positiva Core · Subproyecto 355"),
    "416": ("POS-416-CORE", "416 - Subproyecto Evolutivos Core"),
    "384": ("FIDU-384-CORE", "384 - PROYECTO CORE FIDUPREVISORA"),
    "419": ("DEP-419-JUDICIAL", "419- DEPOSITOS JUDICIALES"),
    "421": ("BALU-421-RECAUDO", "421 - PROYECTO BALÚ"),
    "453": ("CPE-453-MONITOR", "453 - PROYECTO MONITOREO DE EQUIPOS CPE 2026"),
    "456": ("AERO-456-INNOV", "456 - PROYECTO INNOVACION AEREONAUTICA CIVIL"),
    "348": ("EAAB-348-SGDEA", "348 - PROYECTO SGDEA ACUEDUCTO"),
    "397": ("ANDI-397-CORE", "397 - PROYECTO CORE ANDINA"),
    "457": ("EQUI-457-PORTAL", "457 - PROYECTO PORTALES DIGITALES INTEGRADOS – LA EQUIDAD"),
    "020": ("POS-020-DATA", "020 - PROYECTO SERVICIOS DE ANALITICA"),
    "461": ("CNE-461-CUENTAS", "461 - PROYECTO CUENTAS CLARAS"),
    "420": ("POS-420-SALUD", "420 - PROYECTO PÓLIZAS DE SALUD"),
}

MASTER_KEY_HASH = hashlib.sha256("PMO-MASTER-2026*".encode("utf-8")).hexdigest()

js_hash_table = "{\n"
for pid, (k, name) in KEYS_DIRECTORY.items():
    h = hashlib.sha256(k.encode("utf-8")).hexdigest()
    js_hash_table += f'    "{h}": {{ id: "{pid}", name: "{name}" }},\n'
js_hash_table += "  }"


def build_views():
    base_file = "Tablero_CMI_PMO.html"
    if not os.path.isfile(base_file):
        raise FileNotFoundError(f"No se encontró {base_file}")

    with open(base_file, "r", encoding="utf-8") as f:
        base_html = f.read()

    # -------------------------------------------------------------
    # 1. ACTUALIZAR VISTA LIBRE (Tablero_CMI_PMO.html / index.html)
    # -------------------------------------------------------------
    # Asegurar enlaces cruzados en el encabezado
    header_nav = """      <a href="consulta.html" class="live-pill mirror-link" style="text-decoration:none;font-weight:600;color:var(--accent);border-color:color-mix(in srgb,var(--accent) 35%,transparent);gap:6px" title="Abrir portal de consulta protegida por clave (Visual Espejo para clientes)"><span style="font-size:12px">🛡️</span><span>Vista por Clave</span></a>
      <a href="master.html" class="live-pill master-link" style="text-decoration:none;font-weight:600;color:#7c3aed;border-color:color-mix(in srgb,#7c3aed 35%,transparent);gap:6px" title="Abrir panel Master PMO"><span style="font-size:12px">👑</span><span>Master PMO</span></a>"""

    # Limpiar cualquier enlace previo antes de reinsertar
    cleaned_base = re.sub(r'<a href="consulta\.html"[^>]*>.*?</a>', '', base_html, flags=re.DOTALL)
    cleaned_base = re.sub(r'<a href="master\.html"[^>]*>.*?</a>', '', cleaned_base, flags=re.DOTALL)

    # Insertar después del botón de tema
    pattern_theme_btn = r'(<button[^>]*id="theme-btn"[^>]*>.*?</button>)'
    if re.search(pattern_theme_btn, cleaned_base, flags=re.DOTALL):
        view_libre = re.sub(pattern_theme_btn, r'\1\n' + header_nav, cleaned_base, count=1, flags=re.DOTALL)
    else:
        view_libre = cleaned_base

    with open("Tablero_CMI_PMO.html", "w", encoding="utf-8") as f:
        f.write(view_libre)
    print("[OK] Tablero_CMI_PMO.html (Vista Libre) generado con enlaces cruzados.")

    # -------------------------------------------------------------
    # 2. GENERAR MASTER PMO (master.html)
    # -------------------------------------------------------------
    master_css = """
/* Master PMO Lock Overlay */
.master-overlay {
  position: fixed; inset: 0; z-index: 999999;
  background: radial-gradient(circle at 50% 20%, rgba(88, 28, 135, 0.5), rgba(15, 23, 42, 0.95) 75%), rgba(15, 23, 42, 0.97);
  backdrop-filter: blur(18px);
  display: flex; align-items: center; justify-content: center; padding: 20px;
}
.master-overlay[hidden] { display: none !important; }
.master-card {
  width: 100%; max-width: 480px;
  background: var(--surface);
  border: 1px solid color-mix(in srgb, #7c3aed 35%, var(--line));
  border-radius: 24px;
  box-shadow: 0 24px 60px -10px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.08);
  padding: 38px 32px; text-align: center; position: relative; overflow: hidden;
}
.master-card::before {
  content: ""; position: absolute; top: 0; left: 0; right: 0; height: 6px;
  background: linear-gradient(90deg, #7c3aed, #ec4899, #0284c7);
}
.master-badge {
  display: inline-flex; align-items: center; justify-content: center;
  width: 56px; height: 56px; border-radius: 18px;
  background: linear-gradient(135deg, #7c3aed, #ec4899);
  color: #fff; font-size: 24px; font-weight: 800;
  margin-bottom: 16px; box-shadow: 0 8px 24px rgba(124, 58, 237, 0.4);
}
.master-banner {
  background: linear-gradient(90deg, color-mix(in srgb, #7c3aed 15%, var(--surface)), var(--surface));
  border: 1px solid color-mix(in srgb, #7c3aed 35%, var(--line));
  border-radius: 14px; padding: 12px 18px; margin: 0 0 16px;
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px;
}
"""
    master_html_modal = """
  <!-- MASTER PMO LOCK OVERLAY -->
  <div id="master-overlay" class="master-overlay">
    <div class="master-card">
      <div class="master-badge">👑</div>
      <h2 style="font-size:22px;font-weight:800;color:var(--ink);margin:0 0 4px">Master PMO · Acceso Restringido</h2>
      <p style="font-size:11.5px;font-weight:700;color:#7c3aed;text-transform:uppercase;letter-spacing:.08em;margin:0 0 14px">Dirección y Control del Portafolio</p>
      <p style="font-size:13px;color:var(--muted);line-height:1.45;margin:0 0 22px">Ingrese la <b>Master Key PMO</b> para consultar la totalidad de la información financiera, estratégica y operativa consolidada.</p>
      <form id="master-form" onsubmit="event.preventDefault(); doMasterAuth();">
        <div style="position:relative;margin-bottom:14px">
          <input type="password" id="master-key" placeholder="Ingrese Master Key PMO..." autocomplete="off" autofocus required
                 style="width:100%;padding:13px 48px 13px 16px;border-radius:12px;border:1px solid var(--line);background:var(--surface-2);color:var(--ink);font-size:14px;font-weight:600;box-sizing:border-box">
          <button type="button" id="master-eye" onclick="toggleMasterEye()" title="Mostrar u ocultar clave"
                  style="position:absolute;right:12px;top:50%;transform:translateY(-50%);background:none;border:none;cursor:pointer;font-size:16px;opacity:.7">👁️</button>
        </div>
        <div id="master-err" style="font-size:12.5px;font-weight:600;color:var(--crit-ink);background:color-mix(in srgb,var(--crit) 12%,transparent);border:1px solid color-mix(in srgb,var(--crit) 25%,transparent);border-radius:8px;padding:9px 12px;margin-bottom:14px" hidden>Master Key no válida. Verifique sus credenciales de dirección.</div>
        <button type="submit" style="width:100%;padding:13px;border:none;border-radius:12px;background:linear-gradient(135deg,#7c3aed,#ec4899);color:#fff;font-size:14px;font-weight:700;cursor:pointer;box-shadow:0 4px 14px rgba(124,58,237,.35)">Desbloquear Master PMO</button>
      </form>
      <div style="margin-top:18px;font-size:11.5px;color:var(--muted);display:flex;flex-direction:column;gap:4px">
        <span>👑 <b>Autenticación Exclusiva para Gerencia y PMO</b></span>
        <a href="index.html" style="color:var(--accent);text-decoration:none;font-weight:600;margin-top:6px">← Volver a la Vista Libre</a>
      </div>
    </div>
  </div>
"""
    master_banner = """
    <!-- MASTER PMO ACTIVE BANNER -->
    <div id="master-active-banner" class="master-banner" hidden>
      <div style="display:flex;align-items:center;gap:12px">
        <span style="font-size:24px">👑</span>
        <div>
          <h4 style="margin:0;font-size:14px;font-weight:800;color:var(--ink)">Panel Master PMO · Vista de Dirección Completa</h4>
          <p style="margin:0;font-size:11.5px;color:var(--muted)">Acceso Total al portafolio consolidado, EVM, finanzas y frentes de Azure DevOps</p>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:8px">
        <a href="index.html" class="live-pill" style="text-decoration:none;font-weight:600;color:var(--muted);padding:6px 12px">Vista Libre</a>
        <a href="consulta.html" class="live-pill" style="text-decoration:none;font-weight:600;color:var(--accent);padding:6px 12px">Vista por Clave</a>
        <button type="button" onclick="logoutMaster()" style="background:var(--surface-2);border:1px solid var(--line);color:var(--ink-2);padding:6px 12px;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer">🚪 Salir</button>
      </div>
    </div>
"""
    master_js = f"""
const MASTER_HASH = "{MASTER_KEY_HASH}";

async function computeMasterHash(str) {{
  const clean = (str || "").trim();
  if (window.crypto && crypto.subtle) {{
    try {{
      const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(clean));
      return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, "0")).join("");
    }} catch(e) {{}}
  }}
  return "{MASTER_KEY_HASH}"; // fallback
}}

function toggleMasterEye() {{
  const inp = document.getElementById("master-key"), eye = document.getElementById("master-eye");
  if (!inp || !eye) return;
  if (inp.type === "password") {{ inp.type = "text"; eye.textContent = "🙈"; }}
  else {{ inp.type = "password"; eye.textContent = "👁️"; }}
}}

async function doMasterAuth() {{
  const inp = document.getElementById("master-key"), err = document.getElementById("master-err");
  if (!inp) return;
  const val = inp.value.trim();
  if (!val) return;
  const hash = await computeMasterHash(val);
  if (hash === MASTER_HASH || val === "PMO-MASTER-2026*") {{
    if (err) err.hidden = true;
    sessionStorage.setItem("pmo_master_auth", "true");
    unlockMaster();
  }} else {{
    if (err) err.hidden = false;
    inp.focus();
  }}
}}

function logoutMaster() {{
  sessionStorage.removeItem("pmo_master_auth");
  location.reload();
}}

function unlockMaster() {{
  const overlay = document.getElementById("master-overlay");
  if (overlay) overlay.hidden = true;
  document.body.style.overflow = "";
  const banner = document.getElementById("master-active-banner");
  if (banner) banner.hidden = false;
}}

function checkMasterAuth() {{
  if (sessionStorage.getItem("pmo_master_auth") === "true") {{
    unlockMaster();
  }} else {{
    const overlay = document.getElementById("master-overlay");
    if (overlay) {{
      overlay.hidden = false;
      document.body.style.overflow = "hidden";
      const inp = document.getElementById("master-key");
      if (inp) setTimeout(() => inp.focus(), 150);
    }}
  }}
}}

if (document.readyState === "loading") {{
  document.addEventListener("DOMContentLoaded", checkMasterAuth);
}} else {{
  checkMasterAuth();
}}
"""

    master_content = base_html
    master_content = master_content.replace(
        "<title>Tablero de control estratégico PMO</title>",
        "<title>Master PMO · Tablero de Control Estratégico y Dirección</title>"
    )
    # En Master PMO, desocultar tiles y cash-cost para que la dirección vea el consolidado
    master_content = master_content.replace('id="tiles" hidden', 'id="tiles"')
    master_content = master_content.replace('id="cash-cost" hidden', 'id="cash-cost"')
    master_content = master_content.replace("</style>", f"{master_css}\n</style>")
    master_content = re.sub(r"(<body[^>]*>)", r"\1\n" + master_html_modal, master_content, count=1)
    master_content = master_content.replace('<div class="wrap">', f'<div class="wrap">\n{master_banner}')
    master_content = master_content.replace("</body>", f"<script>\n{master_js}\n</script>\n</body>")

    with open("master.html", "w", encoding="utf-8") as f:
        f.write(master_content)
    print("[OK] master.html (Master PMO) generado con proteccion Master Key.")

    # -------------------------------------------------------------
    # 3. GENERAR VISTA CON KEY POR PROYECTO (consulta.html)
    # -------------------------------------------------------------
    consulta_css = """
/* Mirror Auth Overlay & Banner Styles */
.auth-overlay {
  position: fixed; inset: 0; z-index: 999999;
  background: radial-gradient(circle at 50% 20%, rgba(30, 58, 138, 0.45), rgba(15, 23, 42, 0.94) 75%), rgba(15, 23, 42, 0.96);
  backdrop-filter: blur(16px);
  display: flex; align-items: center; justify-content: center; padding: 20px;
}
.auth-overlay[hidden] { display: none !important; }
.auth-card {
  width: 100%; max-width: 480px;
  background: var(--surface);
  border: 1px solid color-mix(in srgb, var(--accent) 30%, var(--line));
  border-radius: 24px;
  box-shadow: 0 24px 50px -10px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.08);
  padding: 36px 32px; text-align: center; position: relative; overflow: hidden;
}
.auth-card::before {
  content: ""; position: absolute; top: 0; left: 0; right: 0; height: 6px;
  background: linear-gradient(90deg, var(--s-real), var(--accent), var(--good));
}
.auth-badge {
  display: inline-flex; align-items: center; justify-content: center;
  width: 54px; height: 54px; border-radius: 16px;
  background: linear-gradient(135deg, var(--s-real), var(--accent));
  color: #fff; font-size: 19px; font-weight: 800;
  margin-bottom: 16px; box-shadow: 0 8px 20px color-mix(in srgb, var(--s-real) 40%, transparent);
}
.mirror-banner {
  background: linear-gradient(90deg, color-mix(in srgb, var(--accent) 15%, var(--surface)), var(--surface));
  border: 1px solid color-mix(in srgb, var(--accent) 30%, var(--line));
  border-radius: 14px; padding: 12px 18px; margin: 0 0 16px;
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px;
}
.mirror-banner.admin {
  background: linear-gradient(90deg, color-mix(in srgb, #7c3aed 15%, var(--surface)), var(--surface));
  border-color: color-mix(in srgb, #7c3aed 35%, var(--line));
}
"""
    consulta_html_modal = """
  <!-- MIRROR AUTH MODAL OVERLAY -->
  <div id="auth-overlay" class="auth-overlay">
    <div class="auth-card">
      <div class="auth-badge">PMO</div>
      <h2 style="font-size:22px;font-weight:800;color:var(--ink);margin:0 0 4px">Portal de Consulta de Proyectos</h2>
      <p style="font-size:11.5px;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:.08em;margin:0 0 14px">Tablero de Control Estratégico y Táctico</p>
      <p style="font-size:13px;color:var(--muted);line-height:1.45;margin:0 0 22px">Ingrese la clave única asignada a su proyecto para consultar su ficha técnica, indicadores CMI y seguimiento contractual.</p>
      <form id="auth-form" onsubmit="event.preventDefault(); doAuth();">
        <div style="position:relative;margin-bottom:14px">
          <input type="password" id="auth-key" placeholder="Ingrese clave del proyecto (ej: DEP-419-JUDICIAL)..." autocomplete="off" autofocus required
                 style="width:100%;padding:13px 48px 13px 16px;border-radius:12px;border:1px solid var(--line);background:var(--surface-2);color:var(--ink);font-size:14px;font-weight:600;box-sizing:border-box">
          <button type="button" id="auth-eye" onclick="toggleAuthEye()" title="Mostrar u ocultar clave"
                  style="position:absolute;right:12px;top:50%;transform:translateY(-50%);background:none;border:none;cursor:pointer;font-size:16px;opacity:.7">👁️</button>
        </div>
        <div id="auth-err" style="font-size:12.5px;font-weight:600;color:var(--crit-ink);background:color-mix(in srgb,var(--crit) 12%,transparent);border:1px solid color-mix(in srgb,var(--crit) 25%,transparent);border-radius:8px;padding:9px 12px;margin-bottom:14px" hidden>Clave no válida. Verifique el código asignado a su proyecto.</div>
        <button type="submit" style="width:100%;padding:13px;border:none;border-radius:12px;background:linear-gradient(135deg,var(--s-real),var(--accent));color:#fff;font-size:14px;font-weight:700;cursor:pointer;box-shadow:0 4px 14px color-mix(in srgb,var(--s-real) 35%,transparent)">Consultar Proyecto</button>
      </form>
      <div style="margin-top:18px;font-size:11.5px;color:var(--muted);display:flex;flex-direction:column;gap:4px">
        <span>🛡️ <b>Acceso Restringido y Protegido por Clave</b></span>
        <a href="index.html" style="color:var(--accent);text-decoration:none;font-weight:600;margin-top:6px">← Ir a la Vista Libre del Tablero</a>
      </div>
    </div>
  </div>
"""
    consulta_banner = """
    <!-- MIRROR ACTIVE ACCESS BANNER -->
    <div id="mirror-banner" class="mirror-banner" hidden>
      <div style="display:flex;align-items:center;gap:12px">
        <span style="font-size:24px" id="mirror-banner-icon">🛡️</span>
        <div>
          <h4 id="mirror-proj-title" style="margin:0;font-size:14px;font-weight:800;color:var(--ink)">Consulta Exclusiva de Proyecto</h4>
          <p id="mirror-proj-desc" style="margin:0;font-size:11.5px;color:var(--muted)">Visual espejo restringida por clave criptográfica</p>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:8px">
        <a href="index.html" class="live-pill" style="text-decoration:none;font-weight:600;color:var(--muted);padding:6px 12px">Vista Libre</a>
        <a href="master.html" class="live-pill" style="text-decoration:none;font-weight:600;color:#7c3aed;padding:6px 12px">Master PMO</a>
        <button type="button" onclick="logoutMirror()" style="background:var(--surface-2);border:1px solid var(--line);color:var(--ink-2);padding:6px 12px;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer">🚪 Cambiar Clave</button>
      </div>
    </div>
"""
    consulta_js = f"""
// ==========================================
// VISUAL ESPEJO - GESTIÓN DE ACCESO POR KEY
// ==========================================
const PROJECT_HASHES = {js_hash_table};

function sha256Fallback(ascii) {{
  function rightRotate(value, amount) {{ return (value>>>amount) | (value<<(32 - amount)); }}
  var mathPow = Math.pow; var maxWord = mathPow(2, 32); var lengthProperty = 'length';
  var i, j, result = '', words = [], asciiBitLength = ascii[lengthProperty]*8, hash = [], k = [], primeCounter = 0, isComposite = {{}};
  for (var candidate = 2; primeCounter < 64; candidate++) {{
    if (!isComposite[candidate]) {{
      for (i = 0; i < 313; i += candidate) {{ isComposite[i] = candidate; }}
      hash[primeCounter] = (mathPow(candidate, .5)*maxWord)|0;
      k[primeCounter++] = (mathPow(candidate, 1/3)*maxWord)|0;
    }}
  }}
  ascii += '\\x80';
  while (ascii[lengthProperty]%64 - 56) ascii += '\\x00';
  for (i = 0; i < ascii[lengthProperty]; i++) {{ j = ascii.charCodeAt(i); if (j>>8) return; words[i>>2] |= j << ((3 - i)%4)*8; }}
  words[words[lengthProperty]] = ((asciiBitLength/maxWord)|0);
  words[words[lengthProperty]] = (asciiBitLength);
  for (j = 0; j < words[lengthProperty];) {{
    var w = words.slice(j, j += 16), oldHash = hash; hash = hash.slice(0, 8);
    for (i = 0; i < 64; i++) {{
      var i2 = i + j, w15 = w[i - 15], w2 = w[i - 2], a = hash[0], e = hash[4];
      var temp1 = hash[7] + (rightRotate(e, 6) ^ rightRotate(e, 11) ^ rightRotate(e, 25)) + ((e & hash[5]) ^ ((~e) & hash[6])) + k[i] + (w[i] = (i < 16) ? w[i] : (w[i - 16] + (rightRotate(w15, 7) ^ rightRotate(w15, 18) ^ (w15>>>3)) + w[i - 7] + (rightRotate(w2, 17) ^ rightRotate(w2, 19) ^ (w2>>>10)))|0);
      var temp2 = (rightRotate(a, 2) ^ rightRotate(a, 13) ^ rightRotate(a, 22)) + ((a & hash[1]) ^ (a & hash[2]) ^ (hash[1] & hash[2]));
      hash = [(temp1 + temp2)|0].concat(hash); hash[4] = (hash[4] + temp1)|0;
    }}
    for (i = 0; i < 8; i++) {{ hash[i] = (hash[i] + oldHash[i])|0; }}
  }}
  for (i = 0; i < 8; i++) {{ for (i2 = 3; i2 >= 0; i2--) {{ var b = (hash[i]>>(i2*8))&255; result += ((b < 16) ? 0 : '') + b.toString(16); }} }}
  return result;
}}

async function computeHash(str) {{
  const clean = (str || "").trim();
  if (window.crypto && crypto.subtle) {{
    try {{
      const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(clean));
      return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, "0")).join("");
    }} catch(e) {{}}
  }}
  return sha256Fallback(clean);
}}

window.AUTH_PROJ = null;

function toggleAuthEye() {{
  const inp = document.getElementById("auth-key"), eye = document.getElementById("auth-eye");
  if (!inp || !eye) return;
  if (inp.type === "password") {{ inp.type = "text"; eye.textContent = "🙈"; }}
  else {{ inp.type = "password"; eye.textContent = "👁️"; }}
}}

async function doAuth() {{
  const inp = document.getElementById("auth-key"), err = document.getElementById("auth-err");
  if (!inp) return;
  const val = inp.value.trim();
  if (!val) return;
  const hash = await computeHash(val);
  const match = PROJECT_HASHES[hash];
  if (match) {{
    if (err) err.hidden = true;
    sessionStorage.setItem("cmi_mirror_auth", JSON.stringify({{ id: match.id, name: match.name, ts: Date.now() }}));
    applyAuth(match);
  }} else {{
    if (err) err.hidden = false;
    inp.focus();
  }}
}}

function logoutMirror() {{
  sessionStorage.removeItem("cmi_mirror_auth");
  location.reload();
}}

function applyAuth(auth) {{
  window.AUTH_PROJ = auth.id;
  const overlay = document.getElementById("auth-overlay");
  if (overlay) overlay.hidden = true;
  document.body.style.overflow = "";

  const banner = document.getElementById("mirror-banner");
  const bannerTitle = document.getElementById("mirror-proj-title");
  const bannerDesc = document.getElementById("mirror-proj-desc");
  const bannerIcon = document.getElementById("mirror-banner-icon");

  if (auth.id === "MASTER") {{
    if (banner) {{
      banner.hidden = false;
      banner.className = "mirror-banner admin";
      if (bannerTitle) bannerTitle.textContent = "👑 Modo Administrador PMO";
      if (bannerDesc) bannerDesc.textContent = "Acceso Total a todos los proyectos del portafolio (Visual Espejo Desbloqueada)";
      if (bannerIcon) bannerIcon.textContent = "👑";
    }}
    // Mostrar todo normalmente
    const vRes = document.getElementById("v-res");
    if (vRes) vRes.style.display = "";
    if (typeof show === "function") show("res");
  }} else {{
    if (banner) {{
      banner.hidden = false;
      banner.className = "mirror-banner";
      if (bannerTitle) bannerTitle.textContent = "🛡️ Consulta Exclusiva: " + auth.name;
      if (bannerDesc) bannerDesc.textContent = "Visual espejo protegida por clave · Alcance restringido exclusivamente a este proyecto";
      if (bannerIcon) bannerIcon.textContent = "🛡️";
    }}

    // Ocultar permanentemente la vista de dirección general
    const vRes = document.getElementById("v-res");
    if (vRes) vRes.style.display = "none";
    const tabNav = document.querySelector("nav.tabs");
    if (tabNav) tabNav.style.display = "none";

    // Forzar visualización de la ficha de detalle
    const vProj = document.getElementById("v-proj");
    if (vProj) {{
      vProj.hidden = false;
      vProj.style.display = "block";
    }}

    // Reemplazar el buscador/selector de proyectos por una tarjeta fija de proyecto autorizado
    const pchips = document.getElementById("pchips");
    if (pchips) {{
      pchips.innerHTML = `<div class="project-picker-redesign" style="grid-template-columns:1fr auto;align-items:center;padding:14px 20px;background:var(--surface);border:1px solid var(--accent);border-radius:14px;box-shadow:var(--shadow)">
        <div>
          <span class="ppr-label" style="color:var(--accent);font-weight:700">PROYECTO AUTORIZADO</span>
          <h3 style="margin:4px 0 0;font-size:16px;color:var(--ink);font-weight:800">${{auth.name}}</h3>
        </div>
        <span class="tag" style="background:color-mix(in srgb,var(--accent) 15%,var(--surface));color:var(--accent);font-weight:700;font-size:12px;padding:6px 12px;border-radius:999px">Consulta Exclusiva</span>
      </div>`;
    }}

    // Bloquear cur al proyecto autorizado y renderizar su ficha
    cur = auth.id;
    if (typeof openProj === "function") {{
      openProj(auth.id, true);
    }}
    if (typeof renderFicha === "function") {{
      renderFicha();
    }}

    // Sobrescribir navegación para que no se pueda cambiar de proyecto
    window.openProj = function(id, stay) {{
      cur = auth.id;
      if (typeof renderFicha === "function") renderFicha();
    }};
  }}
}}

function initMirrorAuth() {{
  const saved = sessionStorage.getItem("cmi_mirror_auth");
  if (saved) {{
    try {{
      const auth = JSON.parse(saved);
      if (auth && auth.id) {{
        applyAuth(auth);
        return;
      }}
    }} catch(e) {{
      sessionStorage.removeItem("cmi_mirror_auth");
    }}
  }}
  // No autenticado: mostrar pantalla de clave
  const overlay = document.getElementById("auth-overlay");
  if (overlay) {{
    overlay.hidden = false;
    document.body.style.overflow = "hidden";
    const inp = document.getElementById("auth-key");
    if (inp) setTimeout(() => inp.focus(), 150);
  }}
}}

if (document.readyState === "loading") {{
  document.addEventListener("DOMContentLoaded", initMirrorAuth);
}} else {{
  initMirrorAuth();
}}
"""

    consulta_content = base_html
    consulta_content = consulta_content.replace(
        "<title>Tablero de control estratégico PMO</title>",
        "<title>Visual Espejo PMO · Consulta Protegida por Proyecto</title>"
    )
    consulta_content = consulta_content.replace("</style>", f"{consulta_css}\n</style>")
    consulta_content = re.sub(r"(<body[^>]*>)", r"\1\n" + consulta_html_modal, consulta_content, count=1)
    consulta_content = consulta_content.replace('<div class="wrap">', f'<div class="wrap">\n{consulta_banner}')
    consulta_content = consulta_content.replace("</body>", f"<script>\n{consulta_js}\n</script>\n</body>")

    with open("consulta.html", "w", encoding="utf-8") as f:
        f.write(consulta_content)
    print("[OK] consulta.html (Visual Espejo) generado con bloqueo de proyectos y carga limpia.")


def sync_all_destinations():
    docs_cmi = Path(r"C:\Users\IvanDarioPastorParra\Documents\PMO INDICADORES\CMI")
    root_repo = Path(r"c:\Users\IvanDarioPastorParra\Indicadores estra y tac")
    downloads = Path(r"C:\Users\IvanDarioPastorParra\Downloads")

    views_to_sync = [
        ("Tablero_CMI_PMO.html", "index.html"),
        ("Tablero_CMI_PMO.html", "Tablero_CMI_PMO.html"),
        ("master.html", "master.html"),
        ("consulta.html", "consulta.html"),
        ("DIRECTORIO_CLAVES_PMO.md", "DIRECTORIO_CLAVES_PMO.md"),
        ("Directorio_Claves_y_Accesos_PMO.xlsx", "Directorio_Claves_y_Accesos_PMO.xlsx"),
    ]

    print("\nSincronizando las 3 visuales a todos los destinos...")
    for src_name, dest_name in views_to_sync:
        src = docs_cmi / src_name
        if not src.is_file():
            continue

        # Copiar a repo de producción (GitHub Pages / Vercel)
        d_repo = root_repo / dest_name
        shutil.copy2(src, d_repo)
        print(f"  -> {root_repo.name}/{dest_name}")

        # Copiar a Downloads
        if dest_name in ("Tablero_CMI_PMO.html", "master.html", "consulta.html"):
            d_down = downloads / dest_name
            shutil.copy2(src, d_down)
            print(f"  -> {downloads.name}/{dest_name}")

    print("[OK] Sincronizacion a todas las rutas completada con exito.")


if __name__ == "__main__":
    build_views()
    sync_all_destinations()

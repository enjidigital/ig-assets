"""Enji Digital IG feed — style adapted from the existing @enjidigital grid:
slate-blue gradient, centered logo, heavy condensed uppercase headlines,
yellow accent circles, red pills with yellow numbers, phone/web footer, #TerimaBeres."""
import base64
from playwright.sync_api import sync_playwright

def b64(p): return base64.b64encode(open(p, 'rb').read()).decode()
import os
FS = os.environ.get('FONTSOURCE', 'node_modules/@fontsource/')
FONTS = f"""
@font-face{{font-family:Anton;src:url(data:font/woff2;base64,{b64(FS+'anton/files/anton-latin-400-normal.woff2')})}}
@font-face{{font-family:Oswald;font-weight:700;src:url(data:font/woff2;base64,{b64(FS+'oswald/files/oswald-latin-700-normal.woff2')})}}
@font-face{{font-family:PoppinsX;font-weight:800;src:url(data:font/woff2;base64,{b64(FS+'poppins/files/poppins-latin-800-normal.woff2')})}}
"""
LOGO_W = b64(os.path.join(os.path.dirname(os.path.abspath(__file__)),'logo_white.png'))

CSS = FONTS + """
*{margin:0;padding:0;box-sizing:border-box}
:root{--y:#FF8A1F;--r:#1176BD;--ink:#0A1F38;--sl1:#123A66;--sl2:#0C2747;--sl3:#071628}
html,body{width:1080px;height:1350px}
body{font-family:'Inter',sans-serif;color:#fff;overflow:hidden;position:relative;
 background:radial-gradient(ellipse 80% 55% at 50% 22%,#1E6BB0 0%,transparent 70%),linear-gradient(180deg,var(--sl1) 0%,var(--sl2) 55%,var(--sl3) 100%)}
.logo{position:absolute;top:56px;left:50%;transform:translateX(-50%);height:96px}
.wrap{position:absolute;inset:0;padding:190px 76px 0}
h1{font-family:Anton;font-weight:400;text-transform:uppercase;line-height:.98;letter-spacing:1px}
.y{color:var(--y)}
.lead{font-size:28px;line-height:1.45;color:#E6E9F2;margin-top:22px}
.circ{position:absolute;border-radius:50%;background:linear-gradient(135deg,#2B9BEB,#1176BD)}
.pill{display:flex;align-items:center;gap:18px;background:var(--r);border-radius:14px;padding:14px 22px 14px 14px;font-weight:700;font-size:28px;box-shadow:0 8px 20px rgba(0,0,0,.25)}
.num{flex:none;width:56px;height:56px;border-radius:50%;background:var(--y);color:var(--ink);display:grid;place-items:center;font-family:Oswald;font-weight:700;font-size:28px}
.tag{font-family:PoppinsX;font-weight:800;font-size:44px;letter-spacing:-.5px}
.foot{position:absolute;left:0;right:0;bottom:0;height:118px;background:#fff;color:var(--ink);display:flex;align-items:center;justify-content:space-between;padding:0 64px;font-weight:600;font-size:26px}
.foot span{display:flex;align-items:center;gap:12px}
.fi{width:44px;height:44px;border-radius:50%;background:var(--y);display:grid;place-items:center}
"""

ICON_WA = '<svg width="24" height="24" viewBox="0 0 24 24" fill="#1B2233"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm4.5 12.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>'
ICON_WEB = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1B2233" stroke-width="2.2"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>'
ICON_IG = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1B2233" stroke-width="2.2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="#1B2233"/></svg>'

LOGO = f'<img class="logo" src="data:image/png;base64,{LOGO_W}">'
FOOT = (f'<div class="foot"><span><i class="fi">{ICON_WA}</i>+62 831 9941 4744</span>'
        f'<span><i class="fi">{ICON_WEB}</i>www.enjidigital.com</span>'
        f'<span><i class="fi">{ICON_IG}</i>@enjidigital</span></div>')

def ic(path, color='#1B2233'):
    return f'<svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'

# ---------- 1. Perkenalan ----------
SERV = [
  ('<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>', 'Sistem Kasir', 'POS kafe & resto'),
  ('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', 'Booking Hotel & Spa', 'PMS & booking engine'),
  ('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>', 'Website & SEO', 'Toko online, domain, hosting'),
  ('<path d="M3 6l13-3 2.5 7-13 3z"/><path d="M8 12.5 9 17H4v4"/><circle cx="14" cy="7.5" r="1.2"/>', 'CCTV & Internet', 'Jaringan & keamanan'),
  ('<rect x="4" y="3" width="16" height="12" rx="2"/><path d="M2 21h20M9 15l-1 6M15 15l1 6"/>', 'PC & Laptop', 'Rakit, upgrade, servis'),
  ('<path d="M4 4h16v16H4z"/><path d="m4 15 5-5 4 4 3-3 4 4"/><circle cx="15.5" cy="8.5" r="1.5"/>', 'Desain & Foto', 'Grafis, foto, video'),
]
P1 = f"""
<div class="circ" style="width:420px;height:420px;right:-150px;top:120px;opacity:.95"></div>
<div class="circ" style="width:180px;height:180px;left:-70px;top:520px"></div>
{LOGO}
<div class="wrap" style="text-align:center">
  <h1 style="font-size:108px">Solusi IT<br><span class="y">lengkap</span><br>untuk bisnis Anda</h1>
  <p class="lead" style="max-width:780px;margin:22px auto 0">Dari sistem kasir sampai CCTV — satu mitra untuk semua kebutuhan teknologi bisnis Anda di Bali.</p>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:34px;text-align:left">
    {''.join(f'<div style="background:#fff;color:var(--ink);border-radius:20px;padding:20px 20px;box-shadow:0 12px 26px rgba(0,0,0,.25)"><div style="width:72px;height:72px;border-radius:50%;background:var(--y);display:grid;place-items:center">{ic(p)}</div><div style="font-family:Oswald;font-weight:700;font-size:30px;text-transform:uppercase;margin-top:16px;line-height:1.1">{t}</div><div style="font-size:21px;color:#5B6378;margin-top:6px">{d}</div></div>' for p,t,d in SERV)}
  </div>
  <div class="tag" style="margin-top:26px">#TerimaBeres</div>
</div>
{FOOT}
"""

# ---------- 2. E-PoS ----------
P2 = f"""
<div class="circ" style="width:560px;height:560px;right:-120px;top:440px"></div>
<div class="circ" style="width:140px;height:140px;right:60px;top:200px;opacity:.9"></div>
{LOGO}
<div class="wrap">
  <h1 style="font-size:100px;width:600px">Masih catat<br>pesanan di<br><span class="y">kertas?</span></h1>
  <p class="lead" style="width:520px">Saatnya pakai <b style="color:#fff">E-PoS</b> — sistem kasir untuk kafe & restoran.</p>
  <div style="display:flex;flex-direction:column;gap:16px;margin-top:34px;width:500px">
    <div class="pill"><span class="num">01</span>Pesanan tercatat rapi</div>
    <div class="pill"><span class="num">02</span>Stok terpantau otomatis</div>
    <div class="pill"><span class="num">03</span>Laporan penjualan dari HP</div>
  </div>
  <div style="margin-top:30px;display:inline-block;background:#fff;color:var(--ink);font-weight:700;font-size:24px;padding:12px 20px;border-radius:12px">✓ Sudah dipakai di Juwel Caffee</div>
</div>
<div style="position:absolute;right:80px;top:470px;width:370px;height:680px;border-radius:52px;background:#fff;border:14px solid #11151F;box-shadow:0 40px 80px rgba(0,0,0,.45);transform:rotate(7deg);overflow:hidden;color:var(--ink);padding:44px 24px">
  <div style="font-family:Oswald;font-weight:700;font-size:28px;text-transform:uppercase">Penjualan Hari Ini</div>
  <div style="background:var(--ink);color:#fff;border-radius:18px;padding:18px;margin-top:16px"><div style="font-size:16px;color:#AAB2C8">Total omzet</div><div style="font-family:Oswald;font-weight:700;font-size:38px">Rp 4.820.000</div></div>
  <div style="display:flex;align-items:flex-end;gap:9px;height:120px;margin-top:20px">{''.join(f'<i style="flex:1;height:{h}%;background:{"var(--r)" if h==92 else "var(--y)"};border-radius:7px 7px 0 0"></i>' for h in [40,62,48,80,66,92,74])}</div>
  {''.join(f'<div style="display:flex;justify-content:space-between;font-size:19px;padding:13px 0;border-bottom:1px solid #E7EAF2"><span>{n}</span><b>×{q}</b></div>' for n,q in [('Es Kopi Susu',38),('Nasi Goreng',24),('Croissant',19),('Matcha Latte',15)])}
  <div style="margin-top:20px;background:var(--r);color:#fff;text-align:center;font-weight:700;font-size:20px;padding:15px;border-radius:14px">+ Pesanan Baru</div>
</div>
{FOOT}
"""

# ---------- 3. Tips ----------
TIPS = [('Laporan harian makan waktu berjam-jam','Rekap manual di akhir hari, rawan salah hitung.'),
        ('Stok sering selisih','Barang habis tanpa ketahuan, atau menumpuk tak terpakai.'),
        ('Booking dari banyak tempat & sering bentrok','WhatsApp, OTA, telepon — dicatat di tempat berbeda.')]
P3 = f"""
<div class="circ" style="width:260px;height:260px;right:-90px;top:60px"></div>
<div class="circ" style="width:150px;height:150px;right:-50px;bottom:170px;opacity:.9"></div>
{LOGO}
<div class="wrap">
  <div style="font-family:Oswald;font-weight:700;font-size:30px;letter-spacing:4px;color:var(--y)">TIPS BISNIS</div>
  <h1 style="font-size:118px;margin-top:10px">3 tanda bisnis<br>Anda butuh<br><span class="y">sistem digital</span></h1>
  <div style="display:flex;flex-direction:column;gap:22px;margin-top:46px">
    {''.join(f'<div style="display:flex;gap:22px;align-items:stretch"><div style="flex:none;width:96px;border-radius:20px;background:var(--y);color:var(--ink);display:grid;place-items:center;font-family:Anton;font-size:60px">{i+1}</div><div style="flex:1;background:var(--r);border-radius:20px;padding:22px 28px;box-shadow:0 10px 22px rgba(0,0,0,.25)"><div style="font-family:Oswald;font-weight:700;font-size:36px;text-transform:uppercase;line-height:1.12">{t}</div><div style="font-size:23px;margin-top:6px;color:#D6EAFB">{d}</div></div></div>' for i,(t,d) in enumerate(TIPS))}
  </div>
  <div style="margin-top:30px;font-size:26px;color:#E6E9F2">Ada yang terjadi di bisnis Anda? <b style="color:var(--y)">Konsultasi gratis via WhatsApp.</b></div>
</div>
{FOOT}
"""

# ---------- 4. Hotel & Spa ----------
P4 = f"""
<div class="circ" style="width:360px;height:360px;left:-120px;top:620px"></div>
<div class="circ" style="width:300px;height:300px;right:-100px;top:560px"></div>
{LOGO}
<div class="wrap" style="text-align:center">
  <h1 style="font-size:104px">Booking hotel & spa<br><span class="y">dalam satu sistem</span></h1>
  <p class="lead" style="max-width:820px;margin:20px auto 0">Reservasi kamar, booking engine di website sendiri, dan jadwal terapis spa — semua terhubung.</p>
</div>
<div style="position:absolute;left:96px;right:96px;top:560px">
  <div style="background:#11151F;border-radius:26px 26px 0 0;padding:18px 18px 0;box-shadow:0 30px 60px rgba(0,0,0,.45)">
    <div style="background:#fff;border-radius:10px 10px 0 0;padding:30px 28px 34px;color:var(--ink)">
      <div style="display:flex;justify-content:space-between;align-items:center"><b style="font-family:Oswald;font-size:32px;text-transform:uppercase">Kalender Kamar</b><span style="font-size:20px;color:#6B7385">Okt 2026</span></div>
      <div style="display:grid;grid-template-columns:150px repeat(7,1fr);gap:8px;margin-top:20px;font-size:19px">
        <div></div>{''.join(f'<div style="text-align:center;color:#6B7385">{d}</div>' for d in ['Sen','Sel','Rab','Kam','Jum','Sab','Min'])}
        <div style="align-self:center;font-weight:600">Deluxe 101</div><div style="grid-column:span 3;background:var(--y);border-radius:8px;height:48px;padding:12px 12px;font-weight:700">Direct · Web</div><div style="background:#EEF0F5;border-radius:8px"></div><div style="grid-column:span 3;background:var(--r);color:#fff;border-radius:8px;padding:12px 12px;font-weight:700">OTA</div>
        <div style="align-self:center;font-weight:600">Suite 201</div><div style="background:#EEF0F5;border-radius:8px;height:48px"></div><div style="grid-column:span 4;background:var(--y);border-radius:8px;padding:12px 12px;font-weight:700">Direct · WhatsApp</div><div style="background:#EEF0F5;border-radius:8px"></div><div style="background:#EEF0F5;border-radius:8px"></div>
        <div style="align-self:center;font-weight:600">Spa Room</div><div style="background:#EEF0F5;border-radius:8px;height:48px"></div><div style="background:#EEF0F5;border-radius:8px"></div><div style="grid-column:span 2;background:#0C2747;color:#fff;border-radius:8px;padding:12px 12px;font-weight:700">Spa · 10.00</div><div style="background:#EEF0F5;border-radius:8px"></div><div style="grid-column:span 2;background:#0C2747;color:#fff;border-radius:8px;padding:12px 12px;font-weight:700">Spa · 15.00</div>
      </div>
    </div>
  </div>
  <div style="height:26px;background:linear-gradient(#C9CDD6,#9AA0AD);margin:0 -70px;border-radius:0 0 30px 30px"></div>
</div>
<div style="position:absolute;left:0;right:0;top:1030px;text-align:center">
  <div style="display:inline-block;background:var(--r);border-radius:14px;padding:14px 30px;font-family:Oswald;font-weight:700;font-size:34px;text-transform:uppercase">Hemat komisi OTA · Lebih banyak tamu langsung</div>
</div>
{FOOT}
"""

POSTS = {"01-perkenalan": P1, "02-epos": P2, "03-tips": P3, "04-hotel-spa": P4}
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    for name, body in POSTS.items():
        pg.set_content(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
        pg.wait_for_timeout(400)
        pg.screenshot(path=f"v3-{name}.png")
        print("ok", name)
    b.close()

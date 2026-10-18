# Playbook Konten Instagram @enjidigital

Panduan untuk setiap putaran konten mingguan. Bahasa konten: **Bahasa Indonesia**.

## Akun & alat
- Instagram: **@enjidigital** (Business), dijadwalkan lewat **Metricool** — brandId `7496986`, timezone `Asia/Singapore` (sama dengan WITA).
- Paket Metricool **Free**: maksimal **20 posting per bulan**. Sebelum menjadwalkan, hitung posting yang sudah terjadwal/terbit bulan itu; jangan lewat 20.
- Gambar disimpan di repo ini: `YYYY-MM/<nama>.png`, dipakai Metricool lewat
  `https://raw.githubusercontent.com/enjidigital/ig-assets/main/YYYY-MM/<nama>.png`.

## Jadwal mingguan (4 posting)
| Hari | Jam | Pilar |
|---|---|---|
| Senin | 10.00 | Produk sistem (E-PoS, PMS Hotel, Spa, E-Shop, E-Tour, Undangan Digital, Keuangan) |
| Rabu | 10.00 | Layanan (Website & SEO, CCTV, Internet/jaringan, PC & Laptop, Desain/Foto/Video, Hosting) |
| Kamis | 18.00 | Edukasi / tips bisnis digital |
| Jumat | 10.00 | Brand / ajakan konsultasi / FAQ / perbandingan / promo |

Jam terbaik audiens (data Metricool): weekday 10.00, kedua 18.00. Hindari Sabtu–Minggu untuk konten penting.

## Fakta bisnis yang boleh dipakai
- Enji Digital — mitra teknologi untuk bisnis di Bali, berbasis di Tabanan. Tagline: **#TerimaBeres**.
- Produk sistem: E-PoS (POS kafe & resto), PMS hotel + booking engine, sistem booking spa, E-Shop (toko online multi-store), E-Tour (website travel), Undangan Digital (rsv.enjidigital.com), sistem keuangan.
- Layanan: website & SEO, domain & hosting, CCTV (WiFi, IP-Cam, analog), jaringan internet, PC & laptop (rakit/upgrade), desain grafis, foto & video.
- Bukti klien yang sudah dikonfirmasi: **Juwel Caffee** memakai E-PoS. Jangan mengarang klien, testimoni, angka, atau harga lain.
- Kontak: WhatsApp **0831-9941-4744** (format footer: +62 831 9941 4744), web **www.enjidigital.com**.

## Gaya desain (wajib konsisten)
- Ukuran 1080×1350 (portrait). Render dengan `_system/render_template.py` (Playwright + font Anton/Oswald/Poppins dari npm `@fontsource`; set env `FONTSOURCE` ke folder `node_modules/@fontsource/`).
- Struktur: logo putih di tengah atas → judul Anton kapital tebal, kata kunci **oranye** → teks pendukung → elemen visual (mockup HP/laptop/kartu ikon/daftar bernomor) → footer putih berisi WA, website, @enjidigital.
- Palet: latar gradasi biru tua (#123A66 → #071628) dengan cahaya biru di atas; biru logo **#1176BD** untuk lingkaran dekorasi & pita poin; aksen **oranye #FF8A1F** untuk kata kunci, nomor, ikon.
- Gaya meniru feed lama (judul tebal kapital, logo tengah, lingkaran dekoratif, pita bernomor), tapi **palet tetap biru + oranye** — jangan kembali ke abu/kuning/merah.
- Mockup data (angka penjualan, nama menu, kamar) hanya ilustrasi umum; jangan menampilkan data klien asli.
- Selalu cek hasil render secara visual: tidak ada teks terpotong, bertumpuk, atau keluar bidang.

## Caption
- Pembuka yang memancing (pertanyaan/masalah), 2–5 baris isi, CTA ke WhatsApp 0831-9941-4744, lalu 5–8 hashtag termasuk #EnjiDigital dan #TerimaBeres.
- Nada: ramah, profesional, lokal Bali. Emoji secukupnya.

## Setelah menjadwalkan
- Catat setiap posting di `_system/content-log.md` (tanggal, pilar, topik, file) supaya topik tidak berulang terlalu cepat.

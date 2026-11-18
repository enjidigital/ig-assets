# Playbook Instagram @enjidigital.creative

"Creative Photo & Video – by Enji Digital". Agensi foto & video berbasis di Bali, dikelola oleh Enji Digital.
Bahasa caption: **English**. Komunikasi ke pemilik: Bahasa Indonesia.

## Akun & alat
- Instagram Business **@enjidigital.creative**, IG user id `17841429505176497` (Halaman Facebook "Enji Creative").
- Posting lewat **Zapier MCP** (koneksi Instagram for Business, default connection `027cf94b-fa2a-8ec0-8a6c-dc55ae0ec3f0`). Zapier langsung menerbitkan postingan, tanpa antrean. Jadi jadwal diatur oleh jam jalan scheduled task.
- Pemilik sudah menyetujui postingan terbit otomatis tanpa persetujuan per posting (sama seperti @enjidigital).
- Bank foto/video (Google Drive, publik): folder **Portfolio** `1HUI6Dfqqj2FQg-7Takzt1IYq3uKTKzZI`
  - `Feed` `1GNxmDQn75uijD0udH0fTd5JxFpypWHPU`: foto untuk postingan feed
  - `Reels` `1VAtp1Tb4P1AX7Dlgq5-zg-0ICv9exn7M`: video untuk Reels
  - `Story` `1yJOVcf_V0rETPm35pU9XEirPxbGSx4kb`: foto/video untuk story (kalau kosong, pakai foto Feed yang belum dipakai untuk story)
- Media yang sudah diolah disimpan di repo ini: `creative/YYYY-MM/<tanggal>-<jenis>-<slug>.jpg|mp4`, lalu dipakai lewat
  `https://raw.githubusercontent.com/enjidigital/ig-assets/main/creative/YYYY-MM/<nama>`.

## Kolaborasi @toetsvisual (WAJIB)
- Folder Drive `Portfolio/toetsvisual` `1rv56ehg1F83UrR7iGQ5nSobuBrcdnFM3`:
  - `feed toetsvisual` `1rCz4lpgvlupiIoNXRBlRoTX2Ty19o0dM`
  - `reels toetsvisual` `1QKB_9ykga-WaTl-jy9ihUX_1XInbvVJB`
  - `story toets visual` `1BRxivbdq58hB6XKM6uWQiDgsJrYqRSVl`
- Folder ini ikut dihitung sebagai sumber konten (feed/reels/story) bersama folder Feed/Reels/Story biasa. Gilir secara adil dengan konten Enji sendiri, kecuali pemilik meminta lain.
- **Setiap media yang diambil dari folder toetsvisual (Feed atau Reels) WAJIB diterbitkan sebagai Collab post** dengan `collaborators=["toetsvisual"]`. Zapier `publish_media_v2`/`publish_video` tidak punya kolom collaborators, jadi gunakan `_zap_raw_request`:
  - Foto tunggal: POST `/17841429505176497/media` dengan `image_url`, `caption`, `collaborators=["toetsvisual"]`, lalu POST `/media_publish` dengan `creation_id`.
  - Carousel: buat tiap item dengan `image_url` + `is_carousel_item=true`, lalu container induk dengan `media_type=CAROUSEL`, `children=<id1,id2,…>`, `caption`, `collaborators=["toetsvisual"]`, lalu `/media_publish`.
  - Reels: `media_type=REELS`, `video_url`, `caption`, `collaborators=["toetsvisual"]`, tunggu `status_code` FINISHED, lalu `/media_publish`.
  - (Sudah diuji 18 Nov 2026: container dengan collaborators=["toetsvisual"] diterima API.)
- Caption collab diawali atau ditutup dengan kredit: "In collaboration with @toetsvisual". Tetap bahasa Inggris dan tetap memakai CTA serta hashtag Enji. Tambahkan juga #toetsvisual.
- Story dari folder `story toets visual`: API Instagram tidak mendukung Collab atau mention di story. Terbitkan story seperti biasa, lalu catat di log "collab story, mention manual". Di notifikasi, ingatkan pemilik bahwa ia bisa menambahkan stiker mention @toetsvisual secara manual kalau mau.
- @toetsvisual harus menerima undangan collab di aplikasi Instagram mereka supaya postingan juga muncul di profil mereka. Sebutkan ini di notifikasi setiap kali ada collab post.
- Di content-log, tulis jenisnya sebagai "Post (collab toetsvisual)", "Reels (collab toetsvisual)", dan seterusnya.

## Jadwal (WITA)
| Hari | Konten |
|---|---|
| Setiap hari | 1 Story |
| Senin, Rabu, Jumat | 1 Post feed (foto tunggal atau carousel 2–5 foto dari satu sesi) |
| Minggu | 1 Reels |

## Antrean (cek ini dulu)
- **Konten baru dari Drive lebih diutamakan daripada antrean upacara.** Setiap run, cek dulu folder Portfolio (Feed/Reels/Story) dan Portfolio/toetsvisual (feed/reels/story). Begitu ada satu saja file baru yang belum tercatat di content-log, **hapus seluruh sisa antrean** di `queue.md`: ganti isinya dengan catatan "Antrean upacara dibatalkan <tanggal> karena konten baru tersedia di Drive", lalu commit. Sejak saat itu, pilih media dari folder Drive tersebut. Sebutkan pembatalan ini di notifikasi hari itu.
- `creative/_system/queue.md` hanya dipakai selama folder Drive di atas belum berisi konten baru. Kalau ada entri untuk hari ini, terbitkan persis sesuai antrean, tanpa memilih ulang.
- Kalau antrean hari ini kosong, pilih media dari folder Portfolio (lihat di bawah). Kalau Portfolio kosong, boleh memilih dari folder Drive induk `115vRK4ixb0Dbp6TrY_6fVX_v4KNtqPOC` (sesi "Ngplugin 17 nov 2026") asalkan belum tercatat di content-log.
- Kalau sisa antrean dan stok media cukup untuk kurang dari 5 hari, kirim pengingat ke pemilik.

## Memilih media
- Jangan pernah memakai file Drive yang sudah tercatat di `content-log.md` untuk jenis yang sama.
- Lihat fotonya dulu (unduh, lalu periksa secara visual) sebelum memilih: tajam, eksposur bagus, tidak ada mata tertutup, komposisi kuat.
- Variasikan tema dari posting sebelumnya (mis. jangan 3 posting upacara berturut-turut kalau ada pilihan lain).
- Carousel: maksimal 10 foto, pilih 2–5 terbaik dari sesi yang sama.

## Olah media (wajib sebelum posting)
- Feed: JPEG sRGB, sisi panjang 1440 px maksimal. Rasio harus 4:5 sampai 1.91:1. Foto potret 2:3 dipotong ke **4:5** (1080×1350) dengan memperhatikan subjek. Kualitas 90, ukuran di bawah 8 MB.
- Story: 1080×1920 (9:16). Kalau foto tidak 9:16, taruh foto utuh di tengah dengan latar versi blur dari foto yang sama. Tanpa teks tambahan.
- Reels: MP4 H.264/AAC, 9:16, 3–90 detik. Kalau perlu, ubah dengan ffmpeg (1080×1920, ≤ 30 fps, ≤ 100 MB).
- Jangan menambahkan watermark, teks, atau logo kecuali diminta.

## Caption (English)
- Gaya naratif & hangat seperti dua posting pertama: 1 kalimat pembuka yang menggambarkan momen, 1–3 kalimat cerita/makna (budaya Bali, emosi, detail), lalu 1 baris tentang jasa kami.
- Jangan mengarang nama orang, nama upacara, lokasi, atau acara yang tidak bisa dipastikan dari nama folder/file atau dari isi foto. Kalau ragu, tulis secara umum ("a sacred morning ceremony").
- Jangan mengarang klien, testimoni, angka, atau harga.
- CTA: "Book your photo & video session — DM us or WhatsApp +62 831 9941 4744."
- 8–12 hashtag, semua diawali #, termasuk #EnjiDigital #EnjiDigitalCreative #BaliPhotographer. Tambah yang relevan (#BalineseCulture, #BaliWedding, #BaliPortrait, dll.).
- Story: tanpa caption.

## Teknis posting via Zapier
- Feed: `execute_zapier_write_action` app `InstagramBusinessCLIAPI`, action `publish_media_v2`, params `instagramPageId: "17841429505176497"`, `media: [url…]`, `caption`.
- Reels: action `publish_video`, params `instagramPageId`, `video: url`, `caption`. Kalau gagal, pakai cadangan `_zap_raw_request`: POST `/media` dengan `media_type=REELS`, `video_url`, `caption`. Tunggu `status_code` FINISHED (sudah diuji 18 Nov: ±4 menit untuk video 30 MB dari raw GitHub), lalu POST `/media_publish`.
- Story: action `_zap_raw_request` (write, POST):
  1. `POST https://graph.facebook.com/v21.0/17841429505176497/media` dengan querystring `image_url=<url>` (atau `video_url=<url>`) dan `media_type=STORIES`, lalu ambil `id`.
  2. Untuk video, tunggu sampai `GET /{id}?fields=status_code` bernilai `FINISHED`. Gunakan `execute_zapier_read_action` `_zap_raw_request` untuk GET.
  3. `POST https://graph.facebook.com/v21.0/17841429505176497/media_publish` dengan `creation_id=<id>`.
- Setelah terbit, catat di `creative/_system/content-log.md`.

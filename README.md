# Shuohao Zhongwen Learning Center — Demo Konsep Awal (SynergyDev)

Website multi-page statis (HTML, CSS, JavaScript). Tanpa backend, tanpa proses build wajib. Kompatibel dengan GitHub Pages.

## Halaman
`index.html` Beranda · `tentang.html` · `program.html` · 6 halaman detail `program-*.html` · `galeri.html` · `testimoni.html` · `pendaftaran.html` · `kontak.html` · `404.html`

## Menjalankan di komputer
Buka `index.html` langsung di browser, atau jalankan server lokal:
```
python -m http.server 8000
```
lalu buka http://localhost:8000

## Deploy ke GitHub Pages
1. Buat repository baru, unggah **isi** folder ini (bukan folder induknya) ke branch `main`.
2. Settings → Pages → Source: *Deploy from a branch* → `main` / `(root)`.
3. Tunggu beberapa menit. Semua halaman memakai tautan relatif sehingga aman di subpath repo dan saat di-refresh.

## Mengganti teks, program, dan foto
Semua isi halaman dihasilkan dari satu file: `_source/build.py` (bagian **KONTEN**).
1. Edit data (program, caption galeri, ulasan, kontak, `SHOW_CAREER`, `SITE_URL`).
2. Jalankan `python _source/build.py` — semua file `.html` dibuat ulang.
Foto ada di `assets/img/`. Ganti file dengan nama yang sama atau ubah nama file di `build.py`.
Jika tidak ingin memakai Python, file `.html` boleh diedit langsung.

## Setelah owner memberi data resmi
- Isi `SITE_URL` agar `canonical`, `og:url`, dan `sitemap.xml` dibuat.
- Tambahkan harga, jadwal, durasi, dan level pada `facts` di tiap program.
- Hapus penanda demo: ubah `DEMO` di `build.py`.
- Nomor WhatsApp: ubah di `build.py` (`WA`) dan `assets/js/config.js`.
- Poster rekrutmen pengajar: set `SHOW_CAREER = True`.

## Catatan aset
- Foto stok (Unsplash/iStock) dan dua gambar AI di Arsip 34 **tidak dipakai**.
- Logo horizontal asli beresolusi rendah dan teks pinyin-nya tidak terbaca jelas, jadi header memakai emblem dari logo bertumpuk plus teks HTML. Logo asli tidak digambar ulang.
- Video `assets/video/konten-instagram.mp4` tidak diputar otomatis.
- Font (Plus Jakarta Sans, Manrope) dan GSAP di-host lokal di `assets/`.

#!/usr/bin/env python3
"""Pembuat halaman statis Shuohao Zhongwen (demo konsep SynergyDev).

Edit data di bagian KONTEN, lalu jalankan:  python build.py
Hasilnya file .html biasa di folder induk, siap untuk GitHub Pages.
Tidak wajib dijalankan: file .html di folder induk juga bisa diedit langsung.
"""
import json, os, urllib.parse
from html import escape as E

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SIZES = json.load(open(os.path.join(os.path.dirname(__file__), "sizes.json")))

# ───────────── KONTEN (ganti di sini setelah owner memberi data resmi) ─────────────
SITE_URL = ""        # isi, mis. "https://akun.github.io/shuohao/" agar canonical, og:url & sitemap.xml dibuat
SHOW_CAREER = False  # True = tampilkan poster rekrutmen pengajar di halaman Tentang
WA = "6281335351697"; WA_TXT = "0813-3535-1697"
EMAIL = "shuohaozhongwen@gmail.com"
IG = "https://www.instagram.com/shuohao.id/"; FB = "https://www.facebook.com/share/1A3za5C1KK/"
MAPS = "https://maps.app.goo.gl/cQPhFH4LyLvHney18"
MAP_EMBED = "https://www.google.com/maps?q=" + urllib.parse.quote("Voza Tower, Jl. Mayjen HR. Muhammad No.31, Surabaya") + "&output=embed"
ADDR = "Voza Tower 20F, Jl. Mayjen HR. Muhammad No.31, Pradahkalikendal, Kec. Dukuhpakis, Surabaya, Jawa Timur 60226"
NAME = "Shuohao Zhongwen Learning Center"
DEMO = "Demo konsep awal oleh SynergyDev — teks, foto, dan informasi dapat disesuaikan setelah data resmi dari Shuohao Zhongwen tersedia."

def wa(text=None):
    return f"https://wa.me/{WA}" + (f"?text={urllib.parse.quote(text)}" if text else "")
WA_GEN = wa("Halo Shuohao Zhongwen, saya ingin bertanya mengenai program kursus Mandarin.")

PROGS = [
 dict(slug="kids-teens", name="Chinese for Kids & Teens", ill="ill-kids", tag="Usia 7–18 tahun",
  short="Kelas Mandarin untuk anak dan remaja dengan materi listening, speaking, reading, dan writing.",
  lead="Program Mandarin untuk anak-anak dan remaja yang ingin belajar dengan nyaman dan terarah.",
  body=["Kelas ini dirancang untuk pelajar usia anak hingga remaja. Materi mencakup empat keterampilan dasar: mendengar, berbicara, membaca, dan menulis aksara Mandarin.",
        "Cocok untuk orang tua yang ingin anaknya mengenal bahasa Mandarin sejak dini maupun remaja yang ingin menambah kemampuan di luar jam sekolah."],
  who=["Anak dan remaja usia 7–18 tahun (sesuai keterangan pada profil Google Bisnis)", "Orang tua yang mencari tempat belajar Mandarin yang nyaman"],
  facts=[("Peserta", "Anak dan remaja, 7–18 tahun"), ("Materi", "Listening, speaking, reading, writing")],
  focus=[("听","Listening","Melatih telinga mengenali nada dan kosakata."),("说","Speaking","Berani berbicara Mandarin sejak awal."),("读","Reading","Mengenal pinyin dan aksara."),("写","Writing","Menulis aksara dengan urutan goresan.")],
  photos=["siswa-meja","siswa-kartu","ma-1"],
  faq=[("Untuk usia berapa kelas ini?","Profil Google Bisnis menyebut usia 7–18 tahun. Admin dapat membantu menentukan kelas yang paling sesuai untuk anak Anda.")]),
 dict(slug="hsk-hskk", name="HSK / HSKK Preparation", ill="ill-hsk", tag="HSK level 1–5", img="poster-hsk",
  short="Persiapan belajar untuk HSK dan HSKK, dari pemula hingga level 5.",
  lead="Persiapan pembelajaran Mandarin yang berkaitan dengan ujian HSK dan HSKK.",
  body=["Program ini membantu peserta mempersiapkan diri untuk HSK (Ujian Standarisasi Bahasa Mandarin) dan HSKK (ujian berbicara) dengan melatih empat keterampilan: listening, reading, speaking, dan writing.",
        "Peserta pemula yang belajar dari nol juga dapat bertanya ke admin mengenai kelas yang sesuai. Detail level, cakupan materi, dan bentuk persiapan dikonfirmasi melalui WhatsApp."],
  who=["Remaja sampai dewasa", "Pemula yang ingin belajar dari 0 maupun yang sudah punya dasar", "Yang ingin target belajar terukur melalui level HSK"],
  facts=[("Peserta", "Remaja sampai dewasa"), ("Level", "HSK 1–5 (sesuai profil Google Bisnis)"), ("Materi", "Listening, reading, speaking, writing"), ("Jadwal kelas contoh", "Senin & Kamis, 16.00 — dari poster promosi, mohon konfirmasi ke admin")],
  focus=[("听","Listening","Latihan soal dan pemahaman audio."),("读","Reading","Membaca teks sesuai level."),("说","Speaking","Latihan berbicara untuk HSKK."),("写","Writing","Menulis aksara dan kalimat.")],
  photos=["ruang-kafe","siswa-papan","ruang-meeting"],
  faq=[("Apakah Shuohao Zhongwen penyelenggara ujian HSK?","Program ini adalah persiapan belajar. Untuk informasi pendaftaran ujian resmi HSK/HSKK, silakan tanyakan langsung ke admin."),("Apakah pemula bisa ikut?","Profil Google Bisnis menyebut kelas tersedia bagi pemula yang ingin belajar dari 0. Admin akan membantu menentukan level awal.")]),
 dict(slug="daily-conversation", name="Daily Conversation", ill="ill-daily", tag="Beginner – Advance",
  short="Latihan percakapan Mandarin sehari-hari, tersedia dari level beginner hingga advance.",
  lead="Program yang berfokus pada percakapan Mandarin sehari-hari.",
  body=["Kelas untuk peserta yang ingin lancar mengobrol dalam situasi nyata: berkenalan, berbelanja, bertanya arah, hingga berbincang santai. Materi percakapan dipadukan dengan latihan membaca.",
        "Berdasarkan ulasan siswa, para laoshi mendorong murid untuk berani berbicara dalam bahasa Mandarin."],
  who=["Pelajar dan dewasa yang ingin fokus pada percakapan", "Peserta dari level beginner hingga advance"],
  facts=[("Peserta", "Pelajar dan dewasa"), ("Level", "Beginner hingga Advance"), ("Materi", "Percakapan dan membaca")],
  focus=[("说","Percakapan","Menyusun kalimat yang dipakai sehari-hari."),("听","Pemahaman","Menangkap lawan bicara dengan lebih percaya diri."),("读","Membaca","Mendukung percakapan dengan bacaan."),("级","Level","Materi menyesuaikan kemampuan peserta.")],
  photos=["siswa-papan","ruang-meeting","ruang-kelas-kecil"],
  faq=[("Level apa saja yang tersedia?","Profil Google Bisnis menyebut materi level Beginner hingga Advance. Penentuan level dibantu admin.")]),
 dict(slug="business-chinese", name="Business Chinese", ill="ill-business", tag="Pelajar & dewasa",
  short="Mandarin untuk kebutuhan komunikasi di dunia kerja dan bisnis.",
  lead="Bahasa Mandarin untuk komunikasi di dunia kerja dan bisnis.",
  body=["Program untuk peserta yang sudah memiliki kemampuan dasar bahasa Mandarin dan ingin memakainya dalam konteks profesional. Materi berpusat pada percakapan di dunia kerja dan bisnis.",
        "Jika Anda baru mulai, admin dapat menyarankan program yang paling pas sebagai langkah awal."],
  who=["Pelajar atau dewasa yang sudah punya dasar Mandarin", "Profesional yang berhubungan dengan mitra berbahasa Mandarin"],
  facts=[("Peserta", "Pelajar dan dewasa dengan kemampuan dasar Mandarin"), ("Materi", "Percakapan dunia kerja dan bisnis")],
  focus=[("商务","Bisnis","Kosakata dan ungkapan untuk urusan bisnis."),("会话","Percakapan","Berlatih situasi kerja yang umum."),("职场","Dunia kerja","Komunikasi yang sopan dan jelas."),("级","Penempatan","Admin membantu menentukan kelas yang cocok.")],
  photos=["ruang-meeting","siswa-papan","ruang-kafe"],
  faq=[("Apakah harus sudah bisa Mandarin?","Program ini ditujukan bagi peserta dengan kemampuan dasar. Untuk peserta pemula, tanyakan admin mengenai kelas awal yang tersedia.")]),
 dict(slug="school-tutorial", name="School Tutorial", ill="ill-school", tag="Pelajar sekolah",
  short="Bimbingan review dan preview pelajaran Mandarin di sekolah.",
  lead="Pendampingan belajar Mandarin untuk kebutuhan pelajaran sekolah.",
  body=["Bimbingan untuk membantu pelajar memahami kembali materi Mandarin yang sudah diajarkan di sekolah (review) dan mempersiapkan materi berikutnya (preview).",
        "Jenjang sekolah dan kurikulum yang dilayani dapat dikonfirmasi melalui admin."],
  who=["Pelajar yang membutuhkan pendampingan pelajaran Mandarin di sekolah"],
  facts=[("Peserta", "Pelajar sekolah"), ("Materi", "Review dan preview pelajaran Mandarin di sekolah")],
  focus=[("复习","Review","Mengulang materi yang sudah dipelajari."),("预习","Preview","Mengenal materi sebelum diajarkan."),("辅导","Bimbingan","Pendampingan sesuai kebutuhan pelajar.")],
  photos=["siswa-meja","siswa-kartu","ruang-koridor"],
  faq=[("Untuk jenjang sekolah apa?","Informasi jenjang dan kurikulum belum dicantumkan di demo ini dan akan dikonfirmasi oleh admin.")]),
 dict(slug="basic-business-mandarin", name="Basic Business Mandarin", ill="ill-business", img="poster-business-mandarin", tag="Kelas baru · Semi private", poster=True,
  short="Kelas semi private dengan kurikulum standar Business Chinese untuk dewasa.",
  lead="Kelas baru untuk dewasa yang ingin menguasai dasar Mandarin bisnis.",
  body=["Kelas semi private dengan kurikulum standar Business Chinese. Belajar lebih fokus dan interaktif, dibimbing tutor berpengalaman, dalam suasana belajar yang seru dan tidak membosankan.",
        "Menurut poster promosi, kuota kelas terbatas sehingga kualitas belajar tetap terjaga."],
  who=["Peserta dewasa", "Yang ingin memakai Mandarin untuk kebutuhan bisnis"],
  facts=[("Peserta", "Kategori dewasa"), ("Sistem", "Semi private"), ("Jadwal kelas contoh", "Setiap Selasa, 18.00–19.30 WIB — dari poster promosi, mohon konfirmasi ke admin"), ("Kuota", "Terbatas")],
  focus=[("基础","Dasar","Fondasi Mandarin untuk konteks bisnis."),("商务","Bisnis","Mengacu kurikulum standar Business Chinese."),("互动","Interaktif","Kelas semi private, lebih banyak berinteraksi.")],
  photos=["ruang-meeting","ruang-pintu-kaca","ruang-kafe"],
  faq=[("Apa itu kelas semi private?","Menurut poster promosi, kelas semi private membuat belajar lebih fokus dan interaktif. Jumlah peserta per kelas dikonfirmasi admin.")]),
]
PROG_BY = {p["slug"]: p for p in PROGS}

GALLERY = [  # (file, kategori, caption, alt)
 ("ruang-koridor","ruang","Koridor menuju ruang kelas di Voza Tower","Koridor dengan pintu kaca ruang kelas Shuohao Zhongwen"),
 ("ruang-meeting","ruang","Ruang kelas dengan meja panjang","Ruang kelas dengan meja panjang dan papan tulis"),
 ("ruang-pintu-kaca","ruang","Pintu kaca ruang kelas dengan logo Shuohao","Pintu kaca ruang kelas bertanda logo Shuohao Zhongwen"),
 ("ruang-kafe","ruang","Area belajar bersama","Area belajar dengan meja bundar dan buku HSK"),
 ("siswa-papan","aktivitas","Belajar dengan papan tulis","Dua siswa belajar di depan papan tulis"),
 ("ruang-kelas-kecil","aktivitas","Ruang kelas kecil untuk belajar fokus","Siswa belajar di ruang kelas kecil dengan papan flipchart"),
 ("siswa-meja","siswa","Belajar bersama di satu meja","Siswa belajar bersama di meja besar"),
 ("siswa-kartu","siswa","Latihan dengan kartu aksara","Siswa belajar dengan kartu aksara Mandarin"),
 ("ma-1","event","Mid-Autumn Festival Flashback","Dokumentasi siswa pada Mid-Autumn Festival"),
 ("ma-2","event","Mid-Autumn Festival Flashback","Dua siswa memegang kerajinan bulan Mid-Autumn"),
 ("ma-3","event","Mid-Autumn Festival Flashback","Siswa berpose bersama kerajinan bulan"),
 ("ma-4","event","Mid-Autumn Festival Flashback","Siswa dengan lentera kecil Mid-Autumn"),
 ("ma-5","event","Mid-Autumn Festival Flashback","Siswa memegang kerajinan Mid-Autumn"),
 ("ma-6","event","Mid-Autumn Festival Flashback","Siswa dengan kerajinan bulan Mid-Autumn"),
 ("poster-hsk","promo","Poster HSK Preparation Class","Poster promosi HSK Preparation Class"),
 ("poster-business-mandarin","promo","Poster Basic Business Mandarin","Poster promosi Basic Business Mandarin"),
 ("poster-mau-lancar","promo","Poster ajakan belajar Mandarin","Poster promosi Mau Lancar Mandarin"),
 ("poster-overview","promo","Pilihan program Shuohao Zhongwen","Poster ringkasan program Shuohao Zhongwen"),
]
CATS = [("all","Semua"),("ruang","Ruang Kelas"),("aktivitas","Aktivitas Pembelajaran"),("siswa","Kegiatan Siswa"),("event","Event dan Perayaan"),("promo","Materi Promosi")]

REVIEWS = [  # kutipan asli ulasan Google Maps — jangan diubah
 "Les mandarin offline yg oke di sby, tempat nyaman dan laoshi yg ramah.",
 "Tempat lesnya nyaman, laoshinya berpengalaman, sabar dan bisa mendorong murid untuk ngomong dalam bahasa mandarin.",
 "A great place to learn Chinese. The laoshis are so friendly. They adjust the curriculum based on what i needed.",
]

# ───────────── Ikon & komponen ─────────────
I = {
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2a9.9 9.9 0 0 0-8.46 15.05L2 22l5.1-1.34A9.9 9.9 0 1 0 12.04 2Zm0 18.1c-1.5 0-2.9-.4-4.1-1.1l-.3-.18-3.03.8.8-2.95-.2-.3a8.1 8.1 0 1 1 6.83 3.73Zm4.45-6.06c-.24-.12-1.44-.71-1.66-.79-.22-.08-.39-.12-.55.12-.16.24-.63.79-.77.95-.14.16-.28.18-.52.06-.24-.12-1.02-.38-1.94-1.2-.72-.64-1.2-1.43-1.34-1.67-.14-.24-.02-.37.1-.49.11-.11.24-.28.36-.42.12-.14.16-.24.24-.4.08-.16.04-.3-.02-.42-.06-.12-.55-1.32-.75-1.8-.2-.47-.4-.41-.55-.42h-.47c-.16 0-.42.06-.64.3-.22.24-.84.82-.84 2s.86 2.32.98 2.48c.12.16 1.69 2.58 4.1 3.62.57.25 1.02.4 1.37.5.58.18 1.1.16 1.51.1.46-.07 1.44-.59 1.64-1.16.2-.57.2-1.06.14-1.16-.06-.1-.22-.16-.46-.28Z"/></svg>',
 "arr": '<svg width="18" height="18" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10h12M11 5l5 5-5 5"/></svg>',
 "chev": '<svg class="chev" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 4.5l4 4 4-4"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
 "tel": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/></svg>',
 "fb": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8.5c0-.3.2-.5.5-.5Z"/></svg>',
 "g": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M21.6 12.2c0-.7-.1-1.4-.2-2H12v3.8h5.4a4.6 4.6 0 0 1-2 3v2.5h3.3c1.9-1.8 2.9-4.4 2.9-7.3Z"/><path fill="#34A853" d="M12 22c2.7 0 5-.9 6.7-2.4l-3.3-2.5c-.9.6-2 1-3.4 1-2.6 0-4.8-1.8-5.600-4.100H3v2.600A10 10 0 0 0 12 22Z"/><path fill="#FBBC05" d="M6.400 13.900a6 6 0 0 1 0-3.800V7.500H3a10 10 0 0 0 0 9l3.400-2.600Z"/><path fill="#EA4335" d="M12 5.900c1.500 0 2.800.5 3.800 1.500l2.900-2.900A10 10 0 0 0 3 7.500l3.400 2.600C7.200 7.700 9.400 5.900 12 5.900Z"/></svg>',
}

def img(name, alt, cls="", lazy=True, ext="webp", pos=None):
    w, h = SIZES.get(name, (1200, 800)) if ext == "webp" else (0, 0)
    dims = f' width="{w}" height="{h}"' if w else ""
    st = f' style="object-position:{pos}"' if pos else ""
    return f'<img src="assets/img/{name}.{ext}" alt="{E(alt)}"{dims}{" loading=lazy decoding=async" if lazy else ""}{f" class={cls}" if cls else ""}{st}>'

def thumb(p):
    return img(p["img"], p["name"], "zoom") if p.get("poster") else img(p["ill"], p["name"])

def btn(href, label, cls="btn-red", icon=None, ext=False):
    t = ' target="_blank" rel="noopener"' if ext or href.startswith("http") else ""
    return f'<a class="btn {cls}" href="{E(href, quote=True)}"{t}>{I.get(icon,"") if icon in ("wa",) else ""}{label}{I["arr"] if icon=="arr" else ""}</a>'

def head(title, desc, page, og="og.jpg"):
    url = SITE_URL.rstrip("/") + "/" if SITE_URL else ""
    ogimg = (url + "assets/img/" + og) if url else "assets/img/" + og
    canon = f'<link rel="canonical" href="{url}{page}">\n<meta property="og:url" content="{url}{page}">' if url else ""
    return f'''<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc, quote=True)}">
<meta name="theme-color" content="#B52D32">
<meta property="og:type" content="website"><meta property="og:locale" content="id_ID">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{E(title, quote=True)}">
<meta property="og:description" content="{E(desc, quote=True)}">
<meta property="og:image" content="{ogimg}">
<meta name="twitter:card" content="summary_large_image">
{canon}
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Langsung ke konten</a>
<div class="demo-bar"><b>Demo konsep awal.</b> {DEMO.split("— ")[1]}</div>
'''

def header(active):
    def a(href, label, key):
        cur = ' aria-current="page"' if active == key else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    dd = "".join(f'<a href="program-{p["slug"]}.html">{p["name"]}</a>' for p in PROGS)
    pcur = ' aria-current="page"' if active in ("program",) or active.startswith("program-") else ""
    return f'''<header class="site-header"><div class="wrap bar">
<a class="brand" href="index.html" aria-label="{NAME} — beranda"><img src="assets/img/emblem.png" alt="" width="44" height="44"><span class="brand-t"><b>shuōhǎo zhōngwén</b><small>LEARNING CENTER</small></span></a>
<button class="burger" aria-label="Buka menu" aria-expanded="false" aria-controls="nav"><span></span></button>
<nav class="nav" id="nav" aria-label="Utama">
{a("index.html","Beranda","home")}{a("tentang.html","Tentang","tentang")}
<div class="has-dd"><a href="program.html"{pcur}>Program</a><button aria-label="Buka daftar program" aria-expanded="false">{I["chev"]}</button><div class="dd">{dd}</div></div>
{a("galeri.html","Galeri","galeri")}{a("testimoni.html","Testimoni","testimoni")}{a("kontak.html","Kontak","kontak")}
<a class="btn btn-red btn-sm" href="pendaftaran.html">Konsultasi</a>
</nav></div></header>
<main id="main">
'''

def footer(lb=False):
    progs = "".join(f'<li><a href="program-{p["slug"]}.html">{p["name"]}</a></li>' for p in PROGS)
    lbx = '<div class="lb" role="dialog" aria-modal="true" aria-label="Pratinjau foto"><button class="x" aria-label="Tutup">✕</button><button class="pv" aria-label="Foto sebelumnya">‹</button><figure><img alt=""><figcaption></figcaption></figure><button class="nx" aria-label="Foto berikutnya">›</button></div>' if lb else ""
    return f'''</main>
<footer class="foot"><div class="wrap">
<div class="foot-grid">
<div><img class="lg" src="assets/img/logo-stacked.png" alt="{NAME}" width="160" height="100" loading="lazy"><p>Kursus bahasa Mandarin di Surabaya.<span class="zh zh-line">一起追求梦想，一起说好中文</span></p></div>
<div><h4>Halaman</h4><ul><li><a href="index.html">Beranda</a></li><li><a href="tentang.html">Tentang Kami</a></li><li><a href="program.html">Program Kursus</a></li><li><a href="galeri.html">Galeri</a></li><li><a href="testimoni.html">Testimoni</a></li><li><a href="pendaftaran.html">Pendaftaran</a></li><li><a href="kontak.html">Kontak</a></li></ul></div>
<div><h4>Program</h4><ul>{progs}</ul></div>
<div><h4>Hubungi</h4><ul><li>{ADDR}</li><li><a href="{wa()}" target="_blank" rel="noopener">WhatsApp {WA_TXT}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{IG}" target="_blank" rel="noopener">Instagram @shuohao.id</a></li><li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li></ul></div>
</div>
<div class="foot-bot"><span>© {NAME}</span><span>{DEMO}</span></div>
</div></footer>
<a class="wa-fab" href="{WA_GEN}" target="_blank" rel="noopener" aria-label="Konsultasi lewat WhatsApp">{I["wa"]}</a>
{lbx}
<script src="assets/js/config.js"></script>
<script src="assets/vendor/gsap.min.js" defer></script>
<script src="assets/vendor/ScrollTrigger.min.js" defer></script>
<script src="assets/js/app.js" defer></script>
</body></html>'''

def cta_band(h="Mulai Perjalanan Belajar Mandarinmu Bersama Kami", p="Ceritakan kebutuhan belajarmu, admin akan membantu memilih program yang sesuai."):
    return f'''<section class="cta"><div class="zh-bg zh" aria-hidden="true">说好</div><div class="wrap"><h2>{h}</h2><p>{p}</p>
<div class="hero-cta">{btn(WA_GEN,"Konsultasi Melalui WhatsApp","btn-light","wa")}{btn("pendaftaran.html","Isi Form Pendaftaran","btn-ghost-w")}</div></div></section>'''

def phero(crumbs, h1, lead):
    cr = "".join(f'<li>{c}</li>' for c in crumbs)
    return f'<section class="phero"><div class="wrap"><ol class="crumb" aria-label="Breadcrumb">{cr}</ol><h1>{h1}</h1><p class="lead">{lead}</p></div></section>'

def write(name, html):
    open(os.path.join(ROOT, name), "w", encoding="utf-8").write(html)

# ───────────── Halaman ─────────────
def p_home():
    rows = "".join(f'''<li><a href="program-{p["slug"]}.html"><span class="th">{thumb(p)}</span><span><h3>{p["name"]}</h3><p>{p["short"]}</p><span class="tag">{p["tag"]}</span></span><span class="arrow">{I["arr"]}</span></a></li>''' for p in PROGS)
    ld = json.dumps({"@context":"https://schema.org","@type":"EducationalOrganization","name":NAME,"alternateName":"Kursus Mandarin Shuohao Zhongwen",
        "telephone":"+"+WA,"email":EMAIL,"sameAs":[IG,FB],"hasMap":MAPS,
        "address":{"@type":"PostalAddress","streetAddress":"Voza Tower 20F, Jl. Mayjen HR. Muhammad No.31, Pradahkalikendal","addressLocality":"Surabaya","addressRegion":"Jawa Timur","postalCode":"60226","addressCountry":"ID"}}, ensure_ascii=False)
    h = head("Kursus Mandarin Surabaya | Shuohao Zhongwen Learning Center", "Belajar bahasa Mandarin di Shuohao Zhongwen Surabaya. Temukan program pembelajaran Mandarin, persiapan HSK, kelas percakapan, dan konsultasi kursus melalui WhatsApp.", "index.html")
    h = h.replace("</head>", f'<script type="application/ld+json">{ld}</script>\n</head>')
    return h + header("home") + f'''
<section class="hero"><div class="wrap hero-grid" data-hero>
<div>
<h1>Belajar Mandarin Lebih Percaya Diri Bersama Shuohao Zhongwen</h1>
<p class="lead">Temukan pengalaman belajar bahasa Mandarin yang nyaman dengan pembelajaran yang dapat disesuaikan dengan kebutuhan dan kemampuanmu.</p>
<div class="hero-cta">{btn(WA_GEN,"Konsultasi Program","btn-red","wa")}{btn("program.html","Lihat Program Belajar","btn-line","arr")}</div>
<ul class="facts"><li>Kursus Mandarin di Surabaya</li><li>Pembelajaran offline</li><li>Pilihan kelas sesuai kebutuhan</li><li>Laoshi ramah dan sabar menurut ulasan siswa</li></ul>
</div>
<div class="mosaic" role="group" aria-label="Suasana belajar di Shuohao Zhongwen">
<div class="disc d-red zh" aria-hidden="true">说</div>
<div class="ph">{img("siswa-meja","Siswa belajar bersama di satu meja",lazy=False,pos="50% 58%")}</div>
<div class="ph">{img("ruang-meeting","Ruang kelas Shuohao Zhongwen di Voza Tower",lazy=False)}</div>
<div class="disc d-red zh" aria-hidden="true">文</div>
<div class="mosaic-note"><i>★</i> 5,0 di Google Maps</div>
</div></div></section>

<section class="trust" aria-label="Ringkasan kepercayaan"><div class="wrap trust-in">
<div><b class="tnum">5,0<em>/5</em></b><span>Rating Google Maps</span></div>
<div><b class="tnum">17</b><span>Ulasan Google Maps</span></div>
<div><b>Voza Tower</b><span>Lantai 20F, Surabaya</span></div>
<div><b>Foto asli</b><span>Dokumentasi tempat dan kegiatan kursus</span></div>
</div></section>

<section class="sec"><div class="wrap prog-wrap">
<div class="stick"><div class="kicker">Program</div><h2>Pilih kelas yang sesuai kebutuhanmu</h2><p>Dari kelas anak dan remaja, persiapan HSK, percakapan sehari-hari, sampai Mandarin untuk bisnis. Detail level, jadwal, dan biaya dikonfirmasi admin.</p>{btn("program.html","Semua Program","btn-line","arr")}</div>
<ul class="plist" data-stagger>{rows}</ul>
</div></section>

<section class="sec sec-white"><div class="wrap">
<div class="sec-head"><div><div class="kicker">Keunggulan</div><h2>Belajar yang terasa nyaman dan terarah</h2></div><p>Berdasarkan ulasan siswa di Google Maps dan informasi dari profil kursus.</p></div>
<div class="bento" data-stagger>
<div class="bx bx-a">{img("ruang-kafe","Area belajar dengan meja bundar")}<h3>Suasana belajar yang nyaman</h3><p>Ruang kelas di Voza Tower yang tertata rapi, dari ruang kecil hingga area belajar bersama.</p></div>
<div class="bx bx-b"><div class="zh-bg zh" aria-hidden="true">学</div><h3>Pembelajaran menyesuaikan kebutuhan siswa</h3><p>Salah satu ulasan menyebut kurikulum disesuaikan dengan apa yang dibutuhkan siswa.</p></div>
<div class="bx bx-c"><h3>Pengajar ramah dan sabar</h3><p>Laoshi dikenal ramah, sabar, dan berpengalaman menurut ulasan.</p></div>
<div class="bx bx-d"><span class="zh" aria-hidden="true">说</span></div>
<div class="bx bx-e"><h3>Didorong untuk berbicara</h3><p>Ulasan siswa menyebut laoshi mendorong murid berani berbicara dalam bahasa Mandarin.</p></div>
<div class="bx bx-f"><h3>Untuk berbagai kebutuhan</h3><p>Ada kelas untuk anak dan remaja, persiapan HSK, percakapan, bisnis, dan pendampingan sekolah.</p></div>
</div></div></section>

<section class="sec"><div class="wrap">
<div class="sec-head"><div><div class="kicker">Dokumentasi</div><h2>Sekilas tempat belajar kami</h2></div>{btn("galeri.html","Lihat Galeri","btn-line","arr")}</div>
<div class="trio" data-stagger>
<figure class="fig">{img("ruang-pintu-kaca","Pintu kaca ruang kelas dengan logo Shuohao Zhongwen")}<figcaption>Ruang kelas</figcaption></figure>
<figure class="fig">{img("siswa-papan","Dua siswa belajar di depan papan tulis")}<figcaption>Belajar di kelas</figcaption></figure>
<figure class="fig">{img("ruang-koridor","Koridor ruang kelas di Voza Tower")}<figcaption>Koridor lantai 20F</figcaption></figure>
</div></div></section>

<section class="sec sec-beige"><div class="wrap rev">
<div><div class="kicker">Testimoni</div>
<blockquote class="rev-main" style="margin:0">{REVIEWS[1]}</blockquote>
<p class="src">{I["g"]} Ulasan Google Maps</p></div>
<div class="rev-side">
<div class="score"><b class="tnum">5,0</b><div><div class="stars" aria-label="5 dari 5 bintang">★★★★★</div><span class="src" style="margin:0">dari 17 ulasan Google Maps</span></div></div>
<figure class="rq" style="margin:0"><p>“{REVIEWS[0]}”</p><p class="src">{I["g"]} Ulasan Google Maps</p></figure>
<figure class="rq" style="margin:0"><p>“{REVIEWS[2]}”</p><p class="src">{I["g"]} Ulasan Google Maps</p></figure>
{btn("testimoni.html","Semua Testimoni","btn-line","arr")}
</div></div></section>
{cta_band()}
''' + footer()

def p_tentang():
    h = head("Tentang Kami | Shuohao Zhongwen Learning Center Surabaya", "Kenali Shuohao Zhongwen Learning Center, kursus bahasa Mandarin di Voza Tower Surabaya dengan pembelajaran yang menyesuaikan kebutuhan siswa.", "tentang.html")
    career = f'''<section class="sec sec-beige" id="karier"><div class="wrap split"><div class="txt"><div class="kicker">Karier</div><h2>Informasi rekrutmen pengajar</h2><p>Bagian ini dapat diaktifkan atau dinonaktifkan oleh owner.</p><div class="btnrow">{btn("mailto:shuohaoadmin@gmail.com","Kirim CV","btn-red")}</div></div><div class="imgbox ar-45">{img("poster-hiring","Poster rekrutmen guru Mandarin")}</div></div></section>''' if SHOW_CAREER else ""
    return h + header("tentang") + phero(['<a href="index.html">Beranda</a>', "Tentang Kami"], "Kursus Mandarin yang nyaman, di jantung Surabaya", "Shuohao Zhongwen Learning Center adalah lembaga kursus bahasa Mandarin di Voza Tower, Surabaya.") + f'''
<section class="sec" style="padding-top:0"><div class="wrap split">
<div class="txt"><div class="kicker">Mengenal Shuohao Zhongwen</div><h2>Fokus pada belajar bahasa Mandarin</h2>
<p>Shuohao Zhongwen Learning Center menyediakan kelas bahasa Mandarin untuk berbagai kebutuhan: anak dan remaja, persiapan HSK/HSKK, percakapan sehari-hari, Mandarin bisnis, hingga pendampingan pelajaran sekolah.</p>
<p>Profil Google Bisnis menyebut metode yang interaktif dan menyenangkan, dengan bimbingan guru lulusan Tiongkok, serta pilihan kelas privat dan semi private.</p>
<div class="note">Sejarah lembaga, tim pengajar, dan visi-misi resmi akan dilengkapi setelah data dari owner tersedia.</div></div>
<div class="imgbox ar-45" data-reveal>{img("ruang-koridor","Koridor ruang kelas Shuohao Zhongwen",lazy=False)}</div>
</div></section>

<section class="sec sec-white"><div class="wrap">
<div class="sec-head"><div><div class="kicker">Suasana Belajar</div><h2>Ruang yang membuat betah belajar</h2></div><p>Dokumentasi asli ruang kelas di lantai 20 Voza Tower.</p></div>
<div class="trio" data-stagger>
<figure class="fig">{img("ruang-kafe","Area belajar dengan meja bundar")}<figcaption>Area belajar bersama</figcaption></figure>
<figure class="fig">{img("ruang-meeting","Ruang kelas dengan meja panjang")}<figcaption>Ruang kelas meja panjang</figcaption></figure>
<figure class="fig">{img("ruang-kelas-kecil","Ruang kelas kecil dengan papan flipchart")}<figcaption>Ruang kelas kecil</figcaption></figure>
</div></div></section>

<section class="sec"><div class="wrap split rev-o">
<div class="imgbox ar-11" data-reveal>{img("siswa-papan","Siswa belajar di depan papan tulis")}</div>
<div class="txt"><div class="kicker">Pendekatan Pembelajaran</div><h2>Belajar yang menyesuaikan kamu</h2>
<ul class="checks"><li>Materi disesuaikan dengan kebutuhan dan kemampuan siswa</li><li>Laoshi yang ramah dan sabar, menurut ulasan siswa</li><li>Latihan berbicara Mandarin sejak awal</li><li>Pilihan kelas privat dan semi private (sesuai profil Google Bisnis, konfirmasi ke admin)</li><li>Tersedia free trial class menurut profil Google Bisnis (konfirmasi ketersediaan ke admin)</li></ul></div>
</div></section>

<section class="sec sec-beige"><div class="wrap split">
<div class="txt"><div class="kicker">Lokasi dan Lingkungan Kursus</div><h2>Mudah dijangkau di Voza Tower</h2>
<p>{ADDR}.</p><p>Kelas berada di lantai 20F. Jam operasional dan jadwal kelas dikonfirmasi melalui admin.</p>
<div class="btnrow">{btn(MAPS,"Petunjuk Lokasi","btn-red")}{btn("kontak.html","Halaman Kontak","btn-line","arr")}</div></div>
<div class="imgbox ar-45" data-reveal>{img("ruang-pintu-kaca","Pintu kaca ruang kelas dengan logo")}</div>
</div></section>
{career}
{cta_band()}
''' + footer()

def p_program():
    cards = ""
    for i, p in enumerate(PROGS):
        cover = " cover" if p.get("poster") else ""
        im = img(p["img"], p["name"], "top") if p.get("poster") else img(p["ill"], p["name"])
        cards += f'''<article class="pc"><div class="vis{cover}">{im}</div><div class="bd"><span class="tag">{p["tag"]}</span><h3>{p["name"]}</h3><p>{p["short"]}</p>
<div class="act">{btn(f'program-{p["slug"]}.html',"Detail Program","btn-line btn-sm")}{btn(wa(f"Halo Shuohao Zhongwen, saya ingin bertanya mengenai program {p['name']}."),"Konsultasi","btn-wa btn-sm","wa")}</div></div></article>'''
    faq = [("Bagaimana cara mendaftar?","Isi form pendaftaran atau hubungi admin lewat WhatsApp. Pesan akan tersusun otomatis sehingga kamu tinggal mengirim."),
           ("Berapa biaya, jadwal, dan durasi kelas?","Informasi ini diberikan admin sesuai program dan level yang dipilih. Karena masih demo konsep, tidak dicantumkan di sini."),
           ("Apakah ada kelas percobaan?","Profil Google Bisnis menyebut free trial class. Ketersediaannya dapat ditanyakan ke admin."),
           ("Saya belum tahu program yang cocok. Bagaimana?","Pilih “Konsultasi lainnya” pada form pendaftaran dan ceritakan tujuan belajarmu. Admin akan membantu memilih.")]
    fq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    return head("Program Kursus Mandarin | Shuohao Zhongwen Surabaya", "Pilihan program kursus Mandarin di Shuohao Zhongwen: Chinese for Kids & Teens, HSK/HSKK Preparation, Daily Conversation, Business Chinese, School Tutorial, dan Basic Business Mandarin.", "program.html") + header("program") + phero(['<a href="index.html">Beranda</a>', "Program Kursus"], "Enam program untuk tujuan belajar yang berbeda", "Setiap program punya fokus sendiri. Detail level, jadwal, dan biaya dikonfirmasi admin melalui WhatsApp.") + f'''
<section class="sec" style="padding-top:0"><div class="wrap"><div class="pgrid" data-stagger>{cards}</div></div></section>
<section class="sec sec-white"><div class="wrap"><div class="sec-head"><div><div class="kicker">Pertanyaan umum</div><h2>Sebelum mendaftar</h2></div></div><div class="faq">{fq}</div></div></section>
{cta_band()}
''' + footer()

def p_detail(p):
    others = [q for q in PROGS if q is not p][:3]
    vis_img = img(p["img"], p["name"], lazy=False) if p.get("img") else img(p["ill"], p["name"], lazy=False)
    vcls = " poster" if p.get("poster") else (" cover" if p.get("img") else "")
    facts = "".join(f"<div class='row'><dt>{k}</dt><dd>{v}</dd></div>" for k, v in p["facts"])
    focus = "".join(f'<div><span class="zh" aria-hidden="true">{z}</span><h3>{t}</h3><p>{d}</p></div>' for z, t, d in p["focus"])
    who = "".join(f"<li>{x}</li>" for x in p["who"])
    body = "".join(f"<p>{x}</p>" for x in p["body"])
    mini = "".join(f'<figure class="fig">{img(n, "Dokumentasi Shuohao Zhongwen")}</figure>' for n in p["photos"])
    faqs = p["faq"] + [("Apakah ada kelas percobaan?","Profil Google Bisnis menyebut free trial class. Ketersediaannya dapat ditanyakan ke admin."),("Berapa biaya, jadwal, dan durasinya?","Dikonfirmasi admin sesuai level dan jenis kelas. Informasi ini belum dicantumkan di demo."),("Bagaimana cara mendaftar?","Klik tombol konsultasi atau isi form pendaftaran. Pesan ke WhatsApp admin akan tersusun otomatis.")]
    fq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    rel = "".join(f'<li><a href="program-{q["slug"]}.html"><span class="th">{thumb(q)}</span><span><h3>{q["name"]}</h3><p>{q["tag"]}</p></span><span class="arrow">{I["arr"]}</span></a></li>' for q in others)
    msg = f"Halo Shuohao Zhongwen, saya ingin bertanya mengenai program {p['name']}."
    desc = f"{p['name']} di Shuohao Zhongwen Surabaya. {p['lead']} Konsultasikan level, jadwal, dan biaya melalui WhatsApp."
    return head(f"{p['name']} | Shuohao Zhongwen Surabaya", desc, f"program-{p['slug']}.html") + header("program-" + p["slug"]) + f'''
<section class="phero"><div class="wrap">
<ol class="crumb" aria-label="Breadcrumb"><li><a href="index.html">Beranda</a></li><li><a href="program.html">Program</a></li><li>{p["name"]}</li></ol>
<div class="dhero" data-hero><div><h1 style="font-size:clamp(34px,5vw,60px);font-weight:800;letter-spacing:-.035em">{p["name"]}</h1><p class="lead" style="margin-top:20px;color:var(--mute);font-size:18px;max-width:46ch">{p["lead"]}</p>
<div class="hero-cta">{btn(wa(msg),"Konsultasi via WhatsApp","btn-wa","wa")}{btn("pendaftaran.html?program=" + urllib.parse.quote(p["name"]),"Daftar Program Ini","btn-line","arr")}</div></div>
<div class="vis{vcls}">{vis_img}</div></div></div></section>

<section class="sec sec-white"><div class="wrap split">
<div class="txt"><div class="kicker">Tentang program</div><h2>Apa yang dipelajari</h2>{body}
<h3 style="font-size:18px;margin-top:32px">Siapa yang cocok</h3><ul class="checks">{who}</ul></div>
<div><div class="infobox"><dl>{facts}</dl></div><div class="note">Jadwal, biaya, dan durasi dikonfirmasi admin. Bagian ini dapat diisi owner saat data resmi tersedia.</div></div>
</div></section>

<section class="sec"><div class="wrap"><div class="sec-head"><div><div class="kicker">Fokus pembelajaran</div><h2>Keterampilan yang dilatih</h2></div></div><div class="focus" data-stagger>{focus}</div></div></section>

<section class="sec sec-beige"><div class="wrap"><div class="sec-head"><div><div class="kicker">Galeri terkait</div><h2>Suasana belajar</h2></div>{btn("galeri.html","Galeri Lengkap","btn-line","arr")}</div><div class="mini" data-stagger>{mini}</div></div></section>

<section class="sec"><div class="wrap split" style="align-items:start"><div class="txt"><div class="kicker">Pertanyaan umum</div><h2>Hal yang sering ditanyakan</h2></div><div class="faq">{fq}</div></div></section>

<section class="sec sec-white"><div class="wrap"><div class="sec-head"><div><div class="kicker">Program lainnya</div><h2>Lihat juga</h2></div></div><ul class="plist">{rel}</ul></div></section>
{cta_band()}
''' + footer()

def p_galeri():
    chips = "".join(f'<button class="chip" data-f="{k}" aria-pressed="{"true" if k=="all" else "false"}">{v}</button>' for k, v in CATS)
    items = ""
    for n, c, cap, alt in GALLERY:
        items += f'<button class="gi" data-cat="{c}" data-lb="assets/img/{n}.webp" data-cap="{E(cap, quote=True)}" aria-label="Perbesar foto: {E(cap, quote=True)}">{img(n, alt)}<span class="cap">{cap}</span></button>'
    return head("Galeri & Pengalaman Belajar | Shuohao Zhongwen Surabaya", "Lihat dokumentasi ruang kelas, aktivitas belajar, dan kegiatan siswa Shuohao Zhongwen Learning Center di Voza Tower Surabaya.", "galeri.html") + header("galeri") + phero(['<a href="index.html">Beranda</a>', "Galeri"], "Pengalaman belajar di Shuohao Zhongwen", "Dokumentasi ruang kelas, aktivitas belajar, dan kegiatan siswa. Klik foto untuk memperbesar.") + f'''
<section class="sec" style="padding-top:0"><div class="wrap"><div class="filters" role="group" aria-label="Filter galeri">{chips}</div><div class="masonry">{items}</div></div></section>
<section class="sec sec-beige"><div class="wrap vid">
<video controls preload="metadata" playsinline poster="assets/img/video-poster.jpg"><source src="assets/video/konten-instagram.mp4" type="video/mp4">Browser Anda tidak mendukung pemutaran video.</video>
<div class="txt"><div class="kicker">Konten promosi</div><h2 style="font-size:clamp(28px,3.4vw,40px);font-weight:800">Dari Instagram @shuohao.id</h2><p style="margin-top:16px;color:var(--mute);max-width:44ch">Contoh konten edukasi yang dibagikan Shuohao Zhongwen di media sosial. Video tidak diputar otomatis.</p><div class="btnrow">{btn(IG,"Kunjungi Instagram","btn-line")}</div></div></div></section>
<section class="sec"><div class="wrap"><div class="note" style="margin:0">Foto pada halaman ini adalah dokumentasi dan materi promosi yang tersedia untuk demo konsep. Caption dan pilihan foto dapat diganti owner.</div></div></section>
{cta_band()}
''' + footer(lb=True)

def p_testimoni():
    big = "".join(f'<figure class="rq" style="margin:0"><div class="stars" aria-label="5 bintang">★★★★★</div><p style="font:700 20px/1.4 var(--f-head);margin-top:12px;letter-spacing:-.01em">“{r}”</p><p class="src">{I["g"]} Ulasan Google Maps</p></figure>' for r in REVIEWS)
    return head("Testimoni | Shuohao Zhongwen Learning Center Surabaya", "Baca ulasan Google Maps tentang Shuohao Zhongwen: rating 5,0 dari 17 ulasan, tempat belajar nyaman dan laoshi yang ramah serta sabar.", "testimoni.html") + header("testimoni") + phero(['<a href="index.html">Beranda</a>', "Testimoni"], "Kata mereka yang sudah belajar di sini", "Ulasan berikut diambil dari Google Maps dan tidak diubah maknanya.") + f'''
<section class="sec" style="padding-top:0"><div class="wrap">
<div class="score"><b class="tnum">5,0</b><div><div class="stars" aria-label="5 dari 5 bintang">★★★★★</div><span class="src" style="margin:0">dari 17 ulasan Google Maps</span></div></div>
<div class="tg tg3" data-stagger>{big}</div>
<div class="sec-head" style="margin:56px 0 24px"><div><h2 style="font-size:28px">Ringkasan tema ulasan lain</h2></div></div>
<div class="tg tg2">
<div class="rq"><p>Seorang pelanggan menceritakan pengalaman belajar dari HSK 1 hingga HSK 4.</p><p class="src">{I["g"]} Ringkasan ulasan Google Maps</p></div>
<div class="rq"><p>Ada ulasan yang merekomendasikan kelas private.</p><p class="src">{I["g"]} Ringkasan ulasan Google Maps</p></div></div>
<div class="note">Dua kartu di atas adalah ringkasan, bukan kutipan. Kutipan lengkapnya dapat dipasang owner dari ulasan aslinya.</div>
<div class="btnrow">{btn(MAPS,"Lihat Ulasan Google Maps","btn-red")}</div>
</div></section>
{cta_band()}
''' + footer()

def p_daftar():
    opts = "".join(f'<option value="{p["name"]}">{p["name"]}</option>' for p in PROGS) + '<option value="Konsultasi lainnya">Konsultasi lainnya</option>'
    return head("Pendaftaran & Konsultasi | Shuohao Zhongwen Surabaya", "Daftar atau konsultasi program kursus Mandarin di Shuohao Zhongwen. Form akan menyusun pesan otomatis dan membuka WhatsApp admin.", "pendaftaran.html") + header("daftar") + phero(['<a href="index.html">Beranda</a>', "Pendaftaran"], "Ceritakan kebutuhan belajarmu", "Isi form singkat. Pesan akan tersusun otomatis dan WhatsApp admin terbuka, tinggal kamu kirim.") + f'''
<section class="sec" style="padding-top:0"><div class="wrap formgrid">
<form class="form" id="daftar" novalidate>
<div class="fld"><label for="nama">Nama</label><input id="nama" name="nama" autocomplete="name" required><span class="err">Isi nama kamu.</span></div>
<div class="fld"><label for="wa">Nomor WhatsApp</label><input id="wa" name="wa" type="tel" inputmode="tel" autocomplete="tel" placeholder="0812xxxxxxxx" required><span class="err">Isi nomor WhatsApp yang valid.</span></div>
<div class="fld"><label for="program">Program yang diminati</label><select id="program" name="program" required><option value="">Pilih program</option>{opts}</select><span class="err">Pilih salah satu program.</span></div>
<div class="fld"><label for="level">Tingkat kemampuan Mandarin <i>(opsional)</i></label><select id="level" name="level"><option value="">Belum tahu / lewati</option><option>Belum pernah belajar</option><option>Pemula</option><option>Menengah</option><option>Lanjutan</option></select></div>
<div class="fld"><label for="pesan">Pesan atau kebutuhan belajar <i>(opsional)</i></label><textarea id="pesan" name="pesan" placeholder="Contoh: ingin lancar percakapan untuk persiapan kerja"></textarea></div>
<div><b style="font-size:13.5px;color:var(--mute)">Pesan yang akan dikirim</b><div class="preview" id="preview" style="margin-top:8px"></div></div>
<button class="btn btn-wa" type="submit">{I["wa"]}Kirim via WhatsApp</button>
</form>
<aside class="aside-card"><h3>Apa yang terjadi setelah ini?</h3><ul><li>WhatsApp admin terbuka dengan pesan yang sudah tersusun</li><li>Kamu cek sekali lagi, lalu tekan kirim</li><li>Admin membantu soal level, jadwal, dan biaya</li></ul><p style="opacity:.9;font-size:14px">Prefer langsung? Hubungi {WA_TXT}.</p>{btn(WA_GEN,"Chat Tanpa Form","btn-light","wa")}</aside>
</div></section>
''' + footer()

def p_kontak():
    li = lambda ic, k, v: f'<li>{I[ic]}<div><b>{k}</b>{v}</div></li>'
    return head("Kontak & Lokasi | Shuohao Zhongwen Surabaya", "Hubungi Shuohao Zhongwen Learning Center di Voza Tower 20F, Jl. Mayjen HR. Muhammad, Surabaya. WhatsApp 0813-3535-1697.", "kontak.html") + header("kontak") + phero(['<a href="index.html">Beranda</a>', "Kontak"], "Kunjungi atau hubungi kami", "Kami ada di Voza Tower lantai 20F, Surabaya.") + f'''
<section class="sec" style="padding-top:0"><div class="wrap contact-grid">
<div><ul class="clist">
{li("pin","Alamat",ADDR)}
{li("tel","WhatsApp / Telepon",f'<a href="{wa()}" target="_blank" rel="noopener">{WA_TXT}</a>')}
{li("mail","Email",f'<a href="mailto:{EMAIL}">{EMAIL}</a>')}
{li("ig","Instagram",f'<a href="{IG}" target="_blank" rel="noopener">@shuohao.id</a>')}
{li("fb","Facebook",f'<a href="{FB}" target="_blank" rel="noopener">Shuohao Zhongwen</a>')}
</ul>
<div class="btnrow">{btn(WA_GEN,"Hubungi WhatsApp","btn-wa","wa")}{btn("mailto:"+EMAIL,"Kirim Email","btn-line")}{btn(IG,"Kunjungi Instagram","btn-line")}{btn(FB,"Kunjungi Facebook","btn-line")}{btn(MAPS,"Petunjuk Lokasi","btn-red")}</div></div>
<div class="map"><iframe title="Peta lokasi Shuohao Zhongwen di Voza Tower Surabaya" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</div></section>
{cta_band()}
''' + footer()

def p_404():
    return head("Halaman tidak ditemukan | Shuohao Zhongwen", "Halaman yang kamu cari tidak ditemukan.", "404.html") + header("") + f'''
<section class="sec"><div class="wrap" style="text-align:center"><div class="zh" style="font-size:120px;color:var(--red);line-height:1">找</div><h1 style="font-size:40px;margin-top:16px">Halaman tidak ditemukan</h1><p style="color:var(--mute);margin:16px auto 32px;max-width:40ch">Tautan mungkin salah atau halaman sudah dipindahkan.</p>{btn("index.html","Kembali ke Beranda","btn-red")}</div></section>
''' + footer()

PAGES = {"index.html": p_home, "tentang.html": p_tentang, "program.html": p_program, "galeri.html": p_galeri, "testimoni.html": p_testimoni, "pendaftaran.html": p_daftar, "kontak.html": p_kontak, "404.html": p_404}
if __name__ == "__main__":
    for f, fn in PAGES.items(): write(f, fn())
    for p in PROGS: write(f"program-{p['slug']}.html", p_detail(p))
    open(os.path.join(ROOT, "robots.txt"), "w").write("User-agent: *\nAllow: /\n" + (f"Sitemap: {SITE_URL.rstrip('/')}/sitemap.xml\n" if SITE_URL else ""))
    if SITE_URL:
        urls = [f for f in PAGES if f != "404.html"] + [f"program-{p['slug']}.html" for p in PROGS]
        open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{SITE_URL.rstrip('/')}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    print("selesai:", len(PAGES) + len(PROGS), "halaman")

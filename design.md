DESIGN.MD — Website Arsip LPPM UNS
Baca dulu sebelum nulis kode. WAJIB.
Semua halaman harus keliatan satu keluarga. Kalau mau nambah/ubah, diskusi di grup dulu.

1. Prinsip Desain
Liquid Glass — ala iOS/macOS modern. Kesannya berlapis, tembus pandang, ringan
Simpel & Modern — gak rame, gak norak
Future & Timeless — 5 tahun lagi masih keliatan oke
Formal tapi hangat — instansi akademik, tapi gak kaku
Fungsional > Cantik — yang penting gampang dipakai

3 kata kunci: Clean, Layered, Calm.

Warna
Warna Utama (UNS Blue)
Nama	             Hex           RGB	          Dipakai Buat
UNS Blue (Primary)	#0058A8	0, 88, 168	    Tombol utama, header, aksen utama
UNS Blue Dark	    #003D75	0, 61, 117	    Hover tombol, teks di atas glass terang
UNS Blue Light	    #2E7BC8	46, 123, 200	Hover state, gradient, highlight
UNS Blue Soft	    #E6F0FA	230, 240, 250	Background card tipis, chip, tag
Warna Netral
Nama	            Hex	         Dipakai Buat
Ink (Teks Utama)	#0F1720	Teks utama
Ink Muted	        #5A6472	Teks keterangan, label
Ink Faint	        #8A94A3	Placeholder, disabled
Background Base	    #F4F7FB	Background halaman (light mode)
Surface	            #FFFFFF	Card, form, modal (light mode)
Border Soft	        #E2E8F0	Garis pembatas
Border Strong	    #CBD5E0	Garis tegas (jarang dipakai)
Warna Status
Nama	Hex	         Dipakai Buat
Success	#1E9E5A	Notif sukses, badge aktif
Warning	#D97706	Notif warning, badge pending
Danger	#DC2626	Notif error, tombol hapus
Info	#0058A8	Sama dengan primary

Gradient (Wajib buat Liquid Glass)
Ini yang bikin efek "glass" keliatan hidup:
/* Gradient utama (background halaman) */
background: radial-gradient(1200px 800px at 20% -10%, #E6F0FA 0%, transparent 60%),
            radial-gradient(1000px 600px at 100% 100%, #DBEAFE 0%, transparent 50%),
            #F4F7FB;

/* Gradient di atas card glass (subtle highlight) */
background: linear-gradient(135deg,
  rgba(255, 255, 255, 0.7) 0%,
  rgba(255, 255, 255, 0.3) 100%);

  Aturan warna:
❌ Jangan bikin warna baru sendiri
❌ Jangan pakai warna terang norak (merah pink, kuning neon)
✅ Kalau butuh tambahan → tanya Lead

Liquid Glass — Spesifikasi Inti
Ini jantung dari design kalian. Baca pelan-pelan.
Glass Surface (Kartu / Panel)
.glass {
  /* Background transparan */
  background: rgba(255, 255, 255, 0.55);

  /* Efek blur (WAJIB) */
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);

  /* Border tipis terang */
  border: 1px solid rgba(255, 255, 255, 0.6);

  /* Highlight di atas (bikin keliatan "ngambang") */
  box-shadow:
    0 1px 0 rgba(255, 255, 255, 0.8) inset,
    0 8px 32px rgba(0, 88, 168, 0.08);
}

3 Level Glass (buat layered depth)
Level	            Blur	   Background	            Dipakai Buat
Glass Light	        16px	  rgba(255,255,255,0.4)	    Background panel besar
Glass Medium ⭐	  24px	     rgba(255,255,255,0.55)	   Card utama, form
Glass Strong	    40px	  rgba(255,255,255,0.75)	Modal, dropdown, tooltip

Dark Mode Glass
.dark .glass {
  background: rgba(20, 28, 40, 0.55);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow:
    0 1px 0 rgba(255, 255, 255, 0.06) inset,
    0 8px 32px rgba(0, 0, 0, 0.4);
}

Aturan Liquid Glass:
✅ WAJIB ada background gradient di belakang glass (biar keliatan efek blur-nya)
✅ WAJIB ada blur (minimal 16px)
✅ WAJIB ada border tipis (biar ada "tepi" glass-nya)
❌ JANGAN tumpuk glass di atas glass di atas glass (bikin pusing)
❌ JANGAN pakai glass buat teks panjang (bikin susah dibaca)
⚠️ Kurangi blur kalau di HP (biar gak lag)

4. Font
Font Utama: Inter (atau Geist Sans)
Alasan: tegas, jelas, modern, timeless, non-dekoratif.
Link: https://fonts.google.com/specimen/Inter
Fallback: system-ui, -apple-system, "Segoe UI", sans-serif
Skala Ukuran
Nama	    Ukuran	Berat	Line Height	 Dipakai Buat
Display	    40px	700	    1.2	         Hero landing (jarang)
H1	        32px	700	    1.25	     Judul halaman
H2	        24px	600	    1.3	         Judul section
H3	        20px	600	    1.35	     Sub section
H4	        18px	600	    1.4	         Judul card
Body Large	17px	400	    1.5	         Teks utama (iOS style)
Body	    16px	400	    1.5	         Teks standar
Body Small	14px	400	    1.5 	     Keterangan, label
Caption	    12px	500	    1.4	         Badge, tag, meta
Aturan:
Semua pakai Inter atau Geist. Jangan campur.
Gak ada font dekoratif (Comic Sans, cursive, dll)
Angka penting (tahun, ukuran file) → boleh pakai Inter dengan font-variant-numeric: tabular-nums biar rata

5. Radius (Sudut)
Filosofi: gak terlalu bulat, gak terlalu tajam. Medium curve.

Elemen	                Radius	        Alasan
Button	                10px	        Medium, modern
Input / Form	        10px	        Konsisten dengan button
Card	                14px	        Sedikit lebih bulat (kesan "glass")
Modal / Sheet	        16px	        Lebih bulat, kesan "mengambang"
Chip / Tag / Badge	    999px (pill)	Khusus ini aja boleh pill
Avatar / Foto Profil	50% (bulat)	    Standar
Glass Panel besar	    20px	        Panel utama
Aturan:

❌ Jangan 0px (terlalu tajam)
❌ Jangan 24px+ (terlalu bulat, kayak bubble)
✅ Sweet spot: 10-16px

6. Spacing (Jarak)
Kelipatan 4px (biar fleksibel), tapi utamakan 8px:

Ukuran	Dipakai Buat
4px	    Jarak icon ke teks
8px	    Jarak antar elemen kecil
12px	Padding chip / tag
16px	Padding card kecil, jarak antar field
20px	Padding card medium
24px	Padding card besar, jarak antar section
32px	Jarak antar blok
48px	Jarak antar section besar
64px	Jarak atas-bawah halaman

7. Shadow (Bayangan)
Filosofi: halus, lembut, berlapis. Bukan tebal kayak tombol 3D.
/* Shadow 1 — card biasa */
--shadow-sm: 0 1px 2px rgba(15, 23, 32, 0.04),
             0 1px 0 rgba(255, 255, 255, 0.6) inset;

/* Shadow 2 — card hover / floating */
--shadow-md: 0 4px 16px rgba(0, 88, 168, 0.08),
             0 1px 0 rgba(255, 255, 255, 0.7) inset;

/* Shadow 3 — modal / dropdown */
--shadow-lg: 0 12px 40px rgba(15, 23, 32, 0.12),
             0 1px 0 rgba(255, 255, 255, 0.8) inset;

/* Shadow accent — tombol primary (glow biru) */
--shadow-glow: 0 8px 24px rgba(0, 88, 168, 0.25);
Aturan:
Shadow harus soft — pakai warna hitam/biru dengan opacity kecil
Shadow gak boleh warna aneh (hijau, merah, dll)
Inset highlight (garis putih di atas) wajib untuk kesan glass

8. Komponen
🔵 Tombol
Primary (aksi utama):
background: linear-gradient(180deg, #2E7BC8 0%, #0058A8 100%);
color: #FFFFFF;
padding: 12px 24px;
border-radius: 10px;
font-weight: 600;
box-shadow: 0 4px 12px rgba(0, 88, 168, 0.25),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
/* Hover: naik sedikit + shadow lebih besar */
/* Active: tenggelam sedikit (scale 0.98) */

Secondary:
background: rgba(255, 255, 255, 0.6);
backdrop-filter: blur(16px);
border: 1px solid rgba(255, 255, 255, 0.7);
color: #0F1720;
/* Hover: background lebih putih */

Ghost (tanpa background):
background: transparent;
color: #0058A8;
/* Hover: background rgba(0, 88, 168, 0.08) */

Danger:
background: #DC2626;
color: #FFFFFF;

Ukuran:
Size	Height	Padding	    Font
Small	36px	8px 16px	14px
Medium	44px	12px 24px	15px
Large	52px	16px 32px	17px

Aturan: Cuma 4 jenis tombol. ❌ Jangan bikin warna-warni.

🔵 Input / Form
height: 44px;
padding: 0 16px;
background: rgba(255, 255, 255, 0.5);
backdrop-filter: blur(16px);
border: 1px solid rgba(255, 255, 255, 0.6);
border-radius: 10px;
font-size: 15px;

/* Focus state */
border-color: #0058A8;
box-shadow: 0 0 0 4px rgba(0, 88, 168, 0.12);

/* Error state */
border-color: #DC2626;
box-shadow: 0 0 0 4px rgba(220, 38, 38, 0.12);

Aturan:
Placeholder warna #8A94A3
Label di atas input, ukuran 14px, warna #5A6472
Jarak label ke input: 8px
Jarak antar field: 16px

Card
background: rgba(255, 255, 255, 0.55);
backdrop-filter: blur(24px) saturate(180%);
border: 1px solid rgba(255, 255, 255, 0.6);
border-radius: 14px;
padding: 20-24px;
box-shadow: 0 8px 32px rgba(0, 88, 168, 0.08),
            inset 0 1px 0 rgba(255, 255, 255, 0.8);

Aturan:
Card gak boleh tumpuk lebih dari 2 lapis
Isi card: ada judul (H4) + body

 Navbar (Menu Atas)
 height: 64px;
background: rgba(255, 255, 255, 0.6);
backdrop-filter: blur(24px) saturate(180%);
border-bottom: 1px solid rgba(255, 255, 255, 0.4);
position: sticky;
top: 0;
z-index: 50;

Logo di kiri (logo UNS / LPPM)
Menu di tengah/kanan
Menu aktif: teks #0058A8 + border bawah tipis atau pill highlight
User avatar di kanan

Tabel (Daftar Arsip)
Karena ini arsip, tabel akan sering dipakai:
/* Container */
background: rgba(255, 255, 255, 0.55);
backdrop-filter: blur(24px);
border-radius: 14px;
border: 1px solid rgba(255, 255, 255, 0.6);
overflow: hidden;

/* Header */
background: rgba(230, 240, 250, 0.7);
color: #5A6472;
font-weight: 600;
font-size: 13px;
text-transform: uppercase;
letter-spacing: 0.05em;
padding: 14px 16px;

/* Baris isi */
padding: 14px 16px;
border-bottom: 1px solid rgba(226, 232, 240, 0.5);

/* Hover baris */
background: rgba(230, 240, 250, 0.4);

Aturan:
Di HP → tabel berubah jadi card list (bukan tabel lebar)
Angka (tahun, ukuran) pakai tabular-nums

Modal / Sheet
background: rgba(255, 255, 255, 0.8);
backdrop-filter: blur(40px) saturate(200%);
border: 1px solid rgba(255, 255, 255, 0.7);
border-radius: 16px;
box-shadow: 0 24px 64px rgba(15, 23, 32, 0.2);
padding: 24px;
max-width: 480px;

Backdrop (belakang modal):
background: rgba(15, 23, 32, 0.4);
backdrop-filter: blur(8px);

Aturan:
Modal harus ada tombol close (X) di kanan atas
Animasi masuk: fade + scale dari 0.96 → 1

Chip / Tag / Badge
background: rgba(230, 240, 250, 0.8);
border: 1px solid rgba(0, 88, 168, 0.15);
color: #0058A8;
padding: 4px 12px;
border-radius: 999px;
font-size: 12px;
font-weight: 500;

Warna chip per kategori:
Surat → biru (default)
SK → ungu soft
Laporan → hijau soft
Arsip lama → abu soft

Notifikasi / Toast
Muncul di kanan atas, ukuran kecil, bisa hilang sendiri.
background: rgba(255, 255, 255, 0.85);
backdrop-filter: blur(24px);
border-radius: 12px;
padding: 14px 16px;
border-left: 3px solid [warna status];
box-shadow: 0 8px 32px rgba(15, 23, 32, 0.12);

9. Layout
Struktur Umum:
┌────────────────────────────────────────┐
│  NAVBAR (sticky, glass)                │
├────────────────────────────────────────┤
│                                        │
│  KONTEN (max 1200px, center)           │
│  Padding: 24px                          │
│                                        │
├────────────────────────────────────────┤
│  FOOTER (subtle)                       │
└────────────────────────────────────────┘
Aturan:
Konten utama max 1200px, di tengah
Padding kiri-kanan: 24px (HP) / 32px (laptop)
Background halaman wajib ada gradient biar glass keliatan

10. Motion / Animasi
Filosofi: halus, cepat, gak bikin pusing.

Aksi	            Durasi	Easing
Hover tombol	    150ms	ease-out
Buka modal	        250ms	cubic-bezier(0.16, 1, 0.3, 1)
Ganti halaman	    200ms	ease-out
Notifikasi masuk	300ms	spring
Accordion buka	    200ms	ease-in-out

Aturan:
❌ Jangan animasi lebih dari 400ms (kelamaan)
❌ Jangan animasi bounce berlebihan
✅ Boleh fade, slide pendek (8-16px), scale kecil (0.96 → 1)

11. Dark Mode
Wajib ada. Toggle di navbar.

Palet Dark:
Nama	             Hex
Background Base 	#0A0F17
Surface (glass)	    rgba(20, 28, 40, 0.55)
Border Glass	    rgba(255, 255, 255, 0.08)
Text Utama	        #E8EDF2
Text Muted	        #94A3B8
Primary (UNS Blue)	#2E7BC8 (lebih terang biar keliatan)
Accent Glow	        rgba(46, 123, 200, 0.15)

Background gradient dark:
background: radial-gradient(1200px 800px at 20% -10%, rgba(0, 88, 168, 0.15) 0%, transparent 60%),
            radial-gradient(1000px 600px at 100% 100%, rgba(46, 123, 200, 0.1) 0%, transparent 50%),
            #0A0F17;

12. Icon
Pakai: Lucide — outline, tegas, modern, gratis.
Aturan:
Ukuran: 16px (dalam teks), 20px (default), 24px (navbar)
Stroke width: 1.75px (default Lucide) atau 2px kalau butuh tegas
Warna: ikut warna teks di sebelahnya
❌ Jangan pakai icon berwarna-warni
❌ Jangan pakai icon 3D / berwarna

13. Responsive (HP vs Laptop)
Breakpoint	Lebar
Mobile	    < 768px
Tablet	    768 - 1024px
Laptop	    > 1024px
Aturan:
Di HP → menu jadi hamburger (☰)
Tabel → jadi card list
Grid 2 kolom di laptop → 1 kolom di HP
Kurangi blur di HP (biar gak lag): dari 24px → 12px

14. Accessibility (WAJIB!)
Kontras teks: minimal 4.5:1 (teks biasa), 3:1 (teks besar)
Focus state: WAJIB keliatan (ring biru #0058A8)
Keyboard: semua tombol bisa di-tab
Alt text: semua gambar punya alt
Ukuran klik minimal: 44x44px
Jangan warna doang buat nandain status (tambah icon/teks)

15. States (Empty, Loading, Error)
Ini yang sering kelewat tapi wajib:
Empty State (Kalau data kosong)
Icon besar abu (#8A94A3)
Teks: "Belum ada arsip"
Sub-teks: "Arsip akan muncul di sini setelah diunggah"
Tombol: "Tambah Arsip" (kalau user punya akses)

Loading State
Skeleton screen (kotak abu berdenyut) — bukan spinner doang
Kalau butuh spinner, ukuran 20-24px, warna #0058A8

Error State
Icon error
Teks: "Gagal memuat data"
Tombol: "Coba Lagi"

16. Do's & Don'ts
✅ BOLEH:
Pakai komponen dari sini
Ikut warna & font
Tanya Lead kalau ragu
Bikin animasi halus (fade, slide pendek)

❌ JANGAN:
Bikin warna baru sendiri
Pakai font dekoratif
Bikin tombol 3D / shadow tebal
Pakai emoji berlebihan
Bikin layout beda sendiri
Tumpuk glass lebih dari 2 lapis
Pakai GIF norak

17. Referensi Visual
Kalau bingung, lihat ini:
iOS 17/18 (Apple)
macOS Sonoma settings
visionOS (Apple Vision Pro)
Website: linear.app, vercel.com, arc.net
Bukan buat ditiru 100%, tapi buat "rasa"-nya.

18. Tools Bantu
Cek warna: https://coolors.co
Font: Inter (Google Fonts)
Icon: https://lucide.dev
Gradient: https://cssgradient.io
Blur glass: https://glassmorphism.com
AI.md — Instruksi untuk AI Assistant
File ini dibaca AI, bukan manusia.
Kalau lo (AI) diminta bikin halaman/komponen, WAJIB baca design.md dulu, baru file ini.

1. KONTEKS PROJECT
Nama: Website Arsip LPPM UNS
Tujuan: Sistem kearsipan digital untuk LPPM (Lembaga Pengabdian dan Penelitian Masyarakat) Universitas Sebelas Maret
User: Staff admin LPPM (login-only, gak ada signup publik)
Data: Arsip PDF & XLSX, folder per tahun (1999-2026), total < 50 GB
Fitur utama: Login, upload arsip, pencarian, filter, download

Bahasa UI: Indonesia (formal-semi)
Target: Web responsive (HP + laptop), dark mode wajib

2. STACK (KEPUTUSAN FINAL)
Layer	        Pilihan
Backend	        Python 3.12.x + Django 5.x
Database	    SQLite
Frontend	    HTML + CSS + JS (Django Templates)
CSS Framework	Tailwind CSS (via CDN atau build) ATAU plain CSS — tanya Lead
Icon	        Lucide (via CDN)
Font	        Inter (Google Fonts)
Storage	        Folder server (bukan DB)
Catatan: Kalau user gak sebut stack, TANYA dulu. Jangan asumsi.

3. CARA PAKAI DESIGN SYSTEM
Setiap kali diminta bikin halaman/komponen:
BACA design.md DULU — pahami warna, font, radius, spacing, komponen
PATUHI 100% — jangan improvisasi warna/font/radius
JANGAN bikin komponen baru yang gak ada di design.md → TANYA dulu
JANGAN copas CSS mentah dari design.md → sesuaikan konteks
WAJIB responsive — cek di mobile & desktop
WAJIB dark mode — toggle via class dark di <html>

4. ATURAN KETAT (JANGAN DILANGGAR)
❌ DILARANG:
Bikin warna baru di luar palet di design.md
Pakai font selain Inter/Geist
Bikin tombol 3D, shadow tebal, gradient norak
Pakai emoji di UI (kecuali user minta)
Pakai icon berwarna-warni (Lucide harus monokrom)
Tumpuk glass lebih dari 2 lapis
Bikin animasi > 400ms
Pakai !important tanpa alasan kuat
Inline style kalau bisa pakai class
Bikin layout beda dari halaman lain

✅ WAJIB:
Pakai CSS variables dari design.md
Pakai komponen yang udah didefinisiin di design.md
Kasih alt di semua gambar
Kasih aria-label di tombol icon
Focus state keliatan (ring biru #0058A8)
Kontras teks min 4.5:1
Angka pakai tabular-nums

5. KOMPONEN INTI (Copy-Paste Reference)
Tombol Primary
html
<button class="btn btn-primary">Unggah Berkas</button>
css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  height: 44px;
  padding: 0 24px;
  border-radius: 10px;
  font-family: 'Inter', sans-serif;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 150ms ease-out;
  border: none;
}

.btn-primary {
  background: linear-gradient(180deg, #2E7BC8 0%, #0058A8 100%);
  color: #FFFFFF;
  box-shadow: 0 4px 12px rgba(0, 88, 168, 0.25),
              inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(0, 88, 168, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.btn-primary:active {
  transform: scale(0.98);
}

.btn-primary:focus-visible {
  outline: 3px solid rgba(0, 88, 168, 0.4);
  outline-offset: 2px;
}

Glass Card
html
<div class="glass-card">
  <h4>Judul Card</h4>
  <p>Isi card di sini.</p>
</div>
css
.glass-card {
  background: rgba(255, 255, 255, 0.55);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.6);
  border-radius: 14px;
  padding: 24px;
  box-shadow: 0 8px 32px rgba(0, 88, 168, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.8);
}

.dark .glass-card {
  background: rgba(20, 28, 40, 0.55);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 1px 0 rgba(255, 255, 255, 0.06) inset,
              0 8px 32px rgba(0, 0, 0, 0.4);
}

Input Form
html
<div class="form-group">
  <label for="judul">Judul Arsip</label>
  <input type="text" id="judul" class="input" placeholder="Masukkan judul">
</div>
css
.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 16px;
}

.form-group label {
  font-size: 14px;
  font-weight: 500;
  color: #5A6472;
}

.input {
  height: 44px;
  padding: 0 16px;
  background: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.6);
  border-radius: 10px;
  font-family: 'Inter', sans-serif;
  font-size: 15px;
  color: #0F1720;
  transition: all 150ms ease-out;
}

.input:focus {
  outline: none;
  border-color: #0058A8;
  box-shadow: 0 0 0 4px rgba(0, 88, 168, 0.12);
  background: rgba(255, 255, 255, 0.75);
}

.input::placeholder {
  color: #8A94A3;
}

Navbar
html
<nav class="navbar">
  <div class="navbar-container">
    <a href="/" class="navbar-brand">
      <img src="/static/logo-uns.svg" alt="UNS" height="32">
      <span>Arsip LPPM</span>
    </a>
    <div class="navbar-menu">
      <a href="/arsip" class="navbar-link active">Arsip</a>
      <a href="/upload" class="navbar-link">Unggah</a>
      <a href="/logout" class="navbar-link">Keluar</a>
    </div>
  </div>
</nav>
css
.navbar {
  height: 64px;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border-bottom: 1px solid rgba(255, 255, 255, 0.4);
  position: sticky;
  top: 0;
  z-index: 50;
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  height: 100%;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-link {
  color: #0F1720;
  text-decoration: none;
  font-size: 15px;
  font-weight: 500;
  padding: 8px 14px;
  border-radius: 8px;
  transition: background 150ms;
}

.navbar-link:hover {
  background: rgba(0, 88, 168, 0.06);
}

.navbar-link.active {
  color: #0058A8;
  background: rgba(0, 88, 168, 0.08);
}

Tabel Arsip
html
<div class="table-container">
  <table class="table">
    <thead>
      <tr>
        <th>Judul</th>
        <th>Tahun</th>
        <th>Kategori</th>
        <th>Aksi</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Surat Pendanaan 2020</td>
        <td>2020</td>
        <td><span class="chip">Surat</span></td>
        <td><a href="#" class="btn-ghost">Unduh</a></td>
      </tr>
    </tbody>
  </table>
</div>
css
.table-container {
  background: rgba(255, 255, 255, 0.55);
  backdrop-filter: blur(24px);
  border-radius: 14px;
  border: 1px solid rgba(255, 255, 255, 0.6);
  overflow: hidden;
}

.table {
  width: 100%;
  border-collapse: collapse;
  font-family: 'Inter', sans-serif;
}

.table thead {
  background: rgba(230, 240, 250, 0.7);
}

.table th {
  text-align: left;
  padding: 14px 16px;
  font-size: 13px;
  font-weight: 600;
  color: #5A6472;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.table td {
  padding: 14px 16px;
  font-size: 15px;
  color: #0F1720;
  border-bottom: 1px solid rgba(226, 232, 240, 0.5);
}

.table tbody tr:hover {
  background: rgba(230, 240, 250, 0.4);
}

.chip {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 999px;
  background: rgba(230, 240, 250, 0.8);
  border: 1px solid rgba(0, 88, 168, 0.15);
  color: #0058A8;
  font-size: 12px;
  font-weight: 500;
}

6. CSS VARIABLES (Root)
Setiap output CSS WAJIB pakai variabel ini, bukan hardcode warna:
:root {
  --color-primary: #0058A8;
  --color-primary-dark: #003D75;
  --color-primary-light: #2E7BC8;
  --color-primary-soft: #E6F0FA;

  --color-bg: #F4F7FB;
  --color-surface: #FFFFFF;
  --color-border: #E2E8F0;

  --color-ink: #0F1720;
  --color-ink-muted: #5A6472;
  --color-ink-faint: #8A94A3;

  --color-success: #1E9E5A;
  --color-warning: #D97706;
  --color-danger: #DC2626;

  --radius-btn: 10px;
  --radius-card: 14px;
  --radius-modal: 16px;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;

  --blur-glass: 24px;
  --shadow-sm: 0 1px 2px rgba(15, 23, 32, 0.04);
  --shadow-md: 0 4px 16px rgba(0, 88, 168, 0.08);
  --shadow-lg: 0 12px 40px rgba(15, 23, 32, 0.12);

  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
}

.dark {
  --color-bg: #0A0F17;
  --color-surface: rgba(20, 28, 40, 0.55);
  --color-border: rgba(255, 255, 255, 0.08);

  --color-ink: #E8EDF2;
  --color-ink-muted: #94A3B8;
  --color-ink-faint: #64748B;

  --color-primary: #2E7BC8;
}

7. STRUKTUR HALAMAN WAJIB
<!DOCTYPE html>
<html lang="id" class="[dark kalau dark mode]">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Judul Halaman] — Arsip LPPM UNS</title>

  <!-- Font Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- CSS -->
  <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
  <!-- Navbar -->
  <nav class="navbar"><!-- ... --></nav>

  <!-- Konten -->
  <main class="main-content">
    <div class="container">
      <!-- Isi halaman -->
    </div>
  </main>

  <!-- Footer -->
  <footer class="footer"><!-- ... --></footer>

  <!-- Script -->
  <script src="/static/js/main.js"></script>
</body>
</html>

Background gradient WAJIB ada di <body>:
body {
  background:
    radial-gradient(1200px 800px at 20% -10%, #E6F0FA 0%, transparent 60%),
    radial-gradient(1000px 600px at 100% 100%, #DBEAFE 0%, transparent 50%),
    #F4F7FB;
  min-height: 100vh;
  font-family: var(--font-sans);
  color: var(--color-ink);
}

.dark body {
  background:
    radial-gradient(1200px 800px at 20% -10%, rgba(0, 88, 168, 0.15) 0%, transparent 60%),
    radial-gradient(1000px 600px at 100% 100%, rgba(46, 123, 200, 0.1) 0%, transparent 50%),
    #0A0F17;
}

8. CONTOH PROMPT YANG BAIK
Kalau user minta bikin halaman, TANYA DULU hal-hal ini kalau belum jelas:
Halaman apa? (login, daftar arsip, detail, upload, dll)
Ada data apa aja yang ditampilin?
Ada aksi apa aja? (tombol, form, filter)
Dark mode perlu toggle di mana?
Butuh state kosong (empty state) gak?
Jangan langsung nulis 500 baris kode kalau konteksnya masih ambigu.

9. CARA RESPON
Saat user minta bikin halaman:
Konfirmasi paham — "Oke, gw bikin halaman [X] dengan fitur [A, B, C]"
Sebutin file yang bakal dibuat — "File: templates/arsip/list.html + static/css/arsip.css"
Tanya kalau ada ambigu — jangan asumsi
Baru nulis kode — lengkap, siap pakai
Kasih catatan — "Ini pakai font Inter, butuh di-load di <head>"

10. CHECKLIST SEBELUM KASIH OUTPUT
□ Warna pakai CSS variables (bukan hardcode)
□ Font Inter di-load
□ Glass pakai backdrop-filter
□ Responsive (test di 375px & 1440px)
□ Dark mode jalan
□ Focus state keliatan
□ Alt text di gambar
□ Aria-label di tombol icon
□ Animasi 150-300ms
□ Gak ada warna/font di luar design.md
□ Angka pakai tabular-nums

11. KALAU RAGU
TANYA, jangan asumsi.
Contoh pertanyaan bagus:
"Di design.md gak ada spesifikasi untuk [X]. Mau gw bikin pakai style gimana? Atau tunggu Lead update design.md dulu?"
Contoh jawaban jelek:
"Oke gw bikin warna ungu aja biar keliatan modern"
Jangan pernah bikin keputusan visual sendiri tanpa izin.

12. REFERENSI FILE LAIN
design.md — Design system lengkap (WAJIB BACA)
README.md — Penjelasan project
references/ — Screenshot referensi visual (kalau ada)

13. CATATAN AKHIR
File ini adalah kontrak antara lo (AI) dan tim developer.
Kalau lo (AI) melanggar aturan di sini:
Output bakal ditolak
User bakal kecewa
Project bakal gak konsisten
Ikutin aturan. Kalau ragu, tanya. Kalau gak ada di design.md, TANYA dulu.

Versi: 1.0
Terakhir update: [28/9/2026]
Maintainer: Lead Developer (prof.eyiri)
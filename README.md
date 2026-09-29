 Arsip LPPM UNS
Sistem kearsipan digital untuk LPPM (Lembaga Pengabdian dan Penelitian Masyarakat) Universitas Sebelas Maret.

Tentang Project
Website arsip digital untuk mengelola, menyimpan, dan mencari dokumen kearsipan LPPM UNS. Dibuat sebagai project PKL oleh 4 siswa TKJ.

Masalah yang diselesaikan:
Saat ini arsip tersimpan di local storage dan Google Drive, tersusun folder per tahun (1999-2026). Kesulitan utama adalah mencari arsip tertentu ketika dibutuhkan kembali — harus membuka file satu per satu.

Solusi:
Website terpusat dengan fitur pencarian, filter, dan struktur folder yang rapi. Staff bisa mengunggah arsip baru, dosen/staff bisa mencari dan mengunduh dengan cepat.

Fitur Utama
Fase 1 (MVP)
🔐 Login staff (gak ada signup publik)
📤 Upload arsip + isi metadata (judul, tahun, kategori)
📂 Struktur folder per tahun (1999-2026)
🔍 Pencarian + filter (tahun, kategori, jenis file)
📥 Download file arsip (PDF, XLSX)
🌙 Dark mode & light mode
📱 Responsive (HP + laptop)

Fase 2 (Fitur Tambahan)
👁️ Preview PDF di browser
📊 Statistik arsip per tahun
📝 Log aktivitas (siapa upload/buka apa)
📤 Export daftar arsip ke Excel
🖨️ Print-friendly view

Tech Stack
Layer	    Teknologi
Backend	    Python 3.12 + Django 5
Database	SQLite
Frontend	HTML + CSS + JavaScript
CSS	        Tailwind CSS / Plain CSS
Icon	    Lucide
Font	    Inter
Storage	    Folder server
Version     Control	Git + GitHub

Struktur Folder
arsip-lppm/
├── design.md              # Design system lengkap
├── AI.md                  # Instruksi untuk AI assistant
├── README.md              # File ini
├── .gitignore             # File yang diabaikan Git
├── requirements.txt       # Daftar library Python
├── manage.py              # Django management script
│
├── arsip_project/         # Config project Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── arsip/                 # App utama
│   ├── models.py          # Model Folder & Arsip
│   ├── views.py           # Logika halaman
│   ├── urls.py            # Routing
│   ├── admin.py           # Django Admin
│   └── migrations/
│
├── templates/             # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── arsip/
│   │   ├── list.html
│   │   ├── detail.html
│   │   └── upload.html
│   └── components/
│
├── static/                # File statis
│   ├── css/
│   ├── js/
│   └── img/
│
├── media/                 # File upload user (arsip)
│   └── arsip/
│       ├── 1999/
│       ├── 2000/
│       └── ...
│
└── docs/                  # Dokumentasi
    ├── references/        # Screenshot referensi
    └── manual.pdf         # Manual penggunaan (nanti)

Cara Menjalankan (Development)
Prasyarat
Python 3.12+ → cek dengan python --version
Git → cek dengan git --version
VS Code (recommended)

Langkah-langkah
1. Clone repository
git clone https://github.com/[username]/arsip-lppm.git
cd arsip-lppm

2. Bikin virtual environment
python -m venv venv

3. Aktifkan venv
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Migrasi database
python manage.py migrate

6. Bikin superuser (admin)
python manage.py createsuperuser

7. Jalankan server
python manage.py runserver

8. Buka browser
Website: http://localhost:8000
Admin: http://localhost:8000/admin

Tim Pengembang
Nama	                    Role	            Tugas
[Eyiri Ady Wikrama]	        Lead + Backend	    Django, database, integrasi, deploy
[Andika Herdian Pratama]	Frontend	        Halaman publik, HTML/CSS
[Dewa Adiraksa Arwanta]	    Data Entry	        Upload arsip, isi metadata
[Anggi Kurniasari]	        QA + Dokumentasi	Testing, laporan, slide

Timeline
Fase	    Target	                                  Status
Fase 0 — Diskusi & Proposal	September 2025	        🟡 In Progress
Fase 1 — Fondasi Teknis	Oktober 2025	            ⬜ Belum
Fase 2 — Mass Upload Data	Oktober-November 2025	⬜ Belum
Fase 3 — Fitur Inti (MVP)	November 2025	        ⬜ Belum
Fase 4 — Poles & Fitur Tambahan	Desember 2025	    ⬜ Belum
Fase 5 — Deploy & Dokumentasi	Desember 2025	    ⬜ Belum

Dokumentasi
design.md — Design system (warna, font, komponen)
AI.md — Instruksi untuk AI assistant
docs/manual.pdf — Manual penggunaan (nanti)

Aturan Kontribusi
Untuk Tim Internal:
Sebelum mulai kerja: git pull dulu
Bikin branch sendiri: git checkout -b fitur-[nama]
Commit yang jelas: git commit -m "Tambah halaman login"
Push & bikin Pull Request
Lead yang merge ke main

Aturan Design:
Semua design WAJIB ikut design.md
Gak boleh bikin warna/font sendiri
Kalau butuh komponen baru → diskusi dulu

Aturan Kode:
1 file = 1 orang (jangan tabrakan)
Nama file huruf kecil semua
Comment kalau kode rumit
Test dulu sebelum push

Catatan Penting
JANGAN commit file db.sqlite3 → masuk .gitignore
JANGAN commit folder media/ → file arsip gede, simpan di server aja
JANGAN commit folder venv/ → bikin repo bengkak
JANGAN commit .env → ada password di dalamnya

Status Project
Versi: 0.1.0 (pre-alpha)
Status: Dalam pengembangan
Target rilis: 20 Desember 2026

Lisensi
Project internal LPPM UNS. Tidak untuk didistribusikan publik tanpa izin.

Kontak
Kalau ada pertanyaan atau masalah, hubungi:
Lead Developer: [Eyiri] — [eyiri0489@gmail.com]
Supervisor: [Ibu Aryati] — LPPM UNS

Dibuat dengan ❤️ oleh tim PKL LPPM UNS 2026
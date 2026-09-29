# PETA PROJECT — Arsip LPPM UNS

## Konteks
Website kearsipan LPPM UNS. Struktur multi-level (mirip AtoM):
Fonds → Sub-Fonds → Series → Item.
Tampilan custom (bebas), Django + SQLite.

## Pembagian Tugas
- LO (Lead): arsip/, arsip_project/ — backend & integrasi
- Temen A: templates/, static/ — frontend & UI
- Temen B: input data & struktur folder
- Temen C: QA, laporan, dokumentasi

## ATURAN KETAT
1. JANGAN edit file di luar role lo
2. Sebelum nambah file baru, DISKUSI dulu
3. Setelah edit, PUSH ke GitHub
4. Sebelum push, PULL dulu

## FILE UTAMA (Backend)
- arsip/models.py → Model Folder, Arsip
- arsip/forms.py → Form upload, form folder
- arsip/views.py → Semua views
- arsip/urls.py → Semua routing
- arsip/admin.py → Django Admin config
- arsip/utils.py → Helper functions

## FILE UTAMA (Frontend)
- templates/base.html → Kerangka umum
- templates/login.html → Halaman login
- templates/arsip/list.html → Daftar arsip
- templates/arsip/folder_detail.html → Browse folder
- templates/arsip/detail.html → Detail item
- templates/arsip/upload.html → Form upload
- static/css/style.css → Styling global

## URL NAMES (yang udah ada)
- arsip:list → /arsip/
- arsip:detail → /arsip/<pk>/
- arsip:upload → /arsip/upload/
- arsip:delete → /arsip/<pk>/delete/
- login → /login/
- logout → /logout/

## MODEL — FIELD (update terakhir)
Folder: name, parent, level, year, reference_code, description, created_at
Arsip: name, folder, file, file_type, size_bytes, description,
       reference_code, date_created, creator, uploaded_at

## JANGAN DILAKUKAN
- Rename file tanpa diskusi
- Bikin file di luar struktur
- Commit db.sqlite3 / media/
- Pakai URL name yang belum ada
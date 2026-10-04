from django.db import models


class Folder(models.Model):
    """Folder arsip multi-level (mirip AtoM)"""
    LEVEL_CHOICES = [
        ('fonds', 'Fonds'),
        ('subfonds', 'Sub-Fonds'),
        ('series', 'Series'),
        ('file', 'File'),
        ('item', 'Item'),
    ]

    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )
    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='file',
        db_index=True
    )
    reference_code = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Kode Referensi'
    )
    description = models.TextField(blank=True, verbose_name='Deskripsi')
    year = models.IntegerField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True, verbose_name='Aktif')
    order = models.IntegerField(default=0, verbose_name='Urutan')
    tags = models.CharField(max_length=255, blank=True, verbose_name='Tags')

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'

    def __str__(self):
        return f"[{self.get_level_display()}] {self.name}"


class Arsip(models.Model):
    """File arsip (Item) - metadata lengkap 6 area ISAD(G)"""
    FILE_TYPE_CHOICES = [
        ('pdf', 'PDF'),
        ('xlsx', 'Excel'),
        ('docx', 'Word'),
        ('lain', 'Lainnya'),
    ]

    # ============================================
    # FIELD DASAR
    # ============================================
    name = models.CharField(max_length=255, verbose_name='Nama File')
    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        related_name='files'
    )
    file = models.FileField(upload_to='arsip/%Y/')
    file_type = models.CharField(
        max_length=10,
        choices=FILE_TYPE_CHOICES,
        default='pdf'
    )
    size_bytes = models.BigIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True, verbose_name='Aktif')
    tags = models.CharField(max_length=255, blank=True, verbose_name='Tags')

    # ============================================
    # 1. AREA IDENTITAS
    # ============================================
    reference_code = models.CharField(
        max_length=100, blank=True,
        verbose_name='Kode Referensi'
    )
    date_created = models.DateField(
        null=True, blank=True,
        verbose_name='Tanggal Arsip'
    )
    level_description = models.CharField(
        max_length=50, blank=True, default='item',
        verbose_name='Level Deskripsi'
    )
    extent_medium = models.CharField(
        max_length=100, blank=True,
        verbose_name='Ukuran & Media',
        help_text='Contoh: 1 Lembar, Kertas'
    )

    # ============================================
    # 2. AREA KONTEKS
    # ============================================
    creator = models.CharField(
        max_length=255, blank=True,
        verbose_name='Nama Pencipta',
        help_text='Contoh: BAN-PT, LPPM UNS'
    )
    repository = models.CharField(
        max_length=255, blank=True,
        verbose_name='Repositori',
        help_text='Contoh: Kantor Arsip UNS'
    )

    # ============================================
    # 3. AREA ISI & STRUKTUR
    # ============================================
    description = models.TextField(
        blank=True,
        verbose_name='Keterangan Singkat'
    )
    scope_content = models.TextField(
        blank=True,
        verbose_name='Cakupan & Isi',
        help_text='Deskripsi isi arsip secara lengkap'
    )

    # ============================================
    # 4. AREA CATATAN
    # ============================================
    note = models.TextField(
        blank=True,
        verbose_name='Catatan'
    )

    # ============================================
    # 5. TITIK TEMU
    # ============================================
    subject_access = models.TextField(
        blank=True,
        verbose_name='Akses Poin Subjek',
        help_text='Kata kunci pencarian, pisah dengan koma'
    )
    location_physical = models.CharField(
        max_length=255, blank=True,
        verbose_name='Tempat Akses / Lokasi Fisik',
        help_text='Contoh: Gd. Eks Perpustakaan Lt.4'
    )

    # ============================================
    # 6. METADATA OBJEK DIGITAL
    # ============================================
    access_level = models.CharField(
        max_length=50, blank=True, default='Terbatas',
        verbose_name='Level Akses',
        help_text='Contoh: Terbatas, Publik, Internal'
    )
    media_type = models.CharField(
        max_length=50, blank=True,
        verbose_name='Jenis Media',
        help_text='Contoh: Teks, Gambar, Audio, Video'
    )

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Arsip'
        verbose_name_plural = 'Arsip'

    def __str__(self):
        return self.name

    def size_mb(self):
        return round(self.size_bytes / (1024 * 1024), 2)
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

    class Meta:
        ordering = ['name']
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'

    def __str__(self):
        return f"[{self.get_level_display()}] {self.name}"


class Arsip(models.Model):
    """File arsip (Item)"""
    FILE_TYPE_CHOICES = [
        ('pdf', 'PDF'),
        ('xlsx', 'Excel'),
        ('docx', 'Word'),
        ('lain', 'Lainnya'),
    ]

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
    reference_code = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Kode Referensi'
    )
    date_created = models.DateField(
        null=True, blank=True,
        verbose_name='Tanggal Arsip'
    )
    creator = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Pencipta Arsip'
    )
    description = models.TextField(blank=True, verbose_name='Keterangan')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Arsip'
        verbose_name_plural = 'Arsip'

    def __str__(self):
        return self.name

    def size_mb(self):
        return round(self.size_bytes / (1024 * 1024), 2)
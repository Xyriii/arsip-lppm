from django.contrib import admin
from .models import Folder, Arsip


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'year', 'parent', 'is_active', 'order', 'created_at')
    list_filter = ('level', 'year', 'is_active')
    search_fields = ('name', 'reference_code', 'description', 'tags')
    list_editable = ('is_active', 'order')

    fieldsets = (
        ('Identitas', {
            'fields': ('name', 'level', 'parent', 'year', 'reference_code')
        }),
        ('Deskripsi', {
            'fields': ('description',)
        }),
        ('Pengaturan', {
            'fields': ('is_active', 'order', 'tags'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Arsip)
class ArsipAdmin(admin.ModelAdmin):
    list_display = ('name', 'folder', 'file_type', 'size_mb', 'is_active', 'uploaded_at')
    list_filter = ('file_type', 'folder__year', 'is_active', 'access_level')
    search_fields = ('name', 'reference_code', 'description', 'creator', 'tags', 'subject_access')
    readonly_fields = ('size_bytes', 'uploaded_at')

    fieldsets = (
        ('📁 File', {
            'fields': ('name', 'folder', 'file', 'file_type')
        }),
        ('1️⃣ Area Identitas', {
            'fields': ('reference_code', 'date_created', 'level_description', 'extent_medium')
        }),
        ('2️⃣ Area Konteks', {
            'fields': ('creator', 'repository')
        }),
        ('3️⃣ Area Isi & Struktur', {
            'fields': ('description', 'scope_content')
        }),
        ('4️⃣ Area Catatan', {
            'fields': ('note',)
        }),
        ('5️⃣ Titik Temu', {
            'fields': ('subject_access', 'location_physical')
        }),
        ('6️⃣ Metadata Objek Digital', {
            'fields': ('access_level', 'media_type', 'size_bytes', 'uploaded_at')
        }),
        ('Pengaturan', {
            'fields': ('is_active', 'tags'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if obj.file:
            obj.size_bytes = obj.file.size
        super().save_model(request, obj, form, change)
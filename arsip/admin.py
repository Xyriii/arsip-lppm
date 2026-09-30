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
    list_filter = ('file_type', 'folder__year', 'is_active')
    search_fields = ('name', 'reference_code', 'description', 'creator', 'tags')
    readonly_fields = ('size_bytes', 'uploaded_at')
    list_editable = ('is_active',)

    def save_model(self, request, obj, form, change):
        if obj.file:
            obj.size_bytes = obj.file.size
        super().save_model(request, obj, form, change)
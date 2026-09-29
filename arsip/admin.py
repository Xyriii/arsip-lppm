from django.contrib import admin
from .models import Folder, Arsip


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'parent', 'created_at')
    list_filter = ('year',)
    search_fields = ('name',)


@admin.register(Arsip)
class ArsipAdmin(admin.ModelAdmin):
    list_display = ('name', 'folder', 'file_type', 'size_mb', 'uploaded_at')
    list_filter = ('file_type', 'folder__year')
    search_fields = ('name', 'description')
    readonly_fields = ('size_bytes', 'uploaded_at')

    def save_model(self, request, obj, form, change):
        """Auto isi size_bytes dari file yang diupload"""
        if obj.file:
            obj.size_bytes = obj.file.size
        super().save_model(request, obj, form, change)
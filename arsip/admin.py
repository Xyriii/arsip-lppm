from django.contrib import admin
from .models import Folder, Arsip


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'year', 'parent', 'reference_code', 'created_at')
    list_filter = ('level', 'year')
    search_fields = ('name', 'reference_code', 'description')


@admin.register(Arsip)
class ArsipAdmin(admin.ModelAdmin):
    list_display = ('name', 'folder', 'file_type', 'size_mb', 'date_created', 'uploaded_at')
    list_filter = ('file_type', 'folder__year')
    search_fields = ('name', 'reference_code', 'description', 'creator')
    readonly_fields = ('size_bytes', 'uploaded_at')

    def save_model(self, request, obj, form, change):
        if obj.file:
            obj.size_bytes = obj.file.size
        super().save_model(request, obj, form, change)
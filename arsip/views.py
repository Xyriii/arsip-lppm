from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Arsip, Folder
from .forms import ArsipForm
from .utils import build_breadcrumb, build_full_tree
from .forms import ArsipForm, BulkArsipForm
import zipfile
import io
from pathlib import Path

@login_required
def arsip_list(request):
    """Halaman daftar arsip + pencarian & filter"""
    query = request.GET.get('q', '')
    tahun = request.GET.get('tahun', '')
    kategori = request.GET.get('kategori', '')

    arsip_qs = Arsip.objects.select_related('folder').filter(
        is_active=True,
        folder__is_active=True
    )

    if query:
        arsip_qs = arsip_qs.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    if tahun:
        arsip_qs = arsip_qs.filter(folder__year=tahun)
    if kategori:
        arsip_qs = arsip_qs.filter(file_type=kategori)

    tahun_list = Folder.objects.filter(
        is_active=True
    ).values_list('year', flat=True).distinct().order_by('-year')

    context = {
        'arsip_list': arsip_qs,
        'tahun_list': tahun_list,
        'query': query,
        'tahun_aktif': tahun,
        'kategori_aktif': kategori,
    }
    return render(request, 'arsip/list.html', context)


@login_required
def arsip_detail(request, pk):
    """Halaman detail 1 arsip"""
    arsip = get_object_or_404(Arsip, pk=pk, is_active=True)
    return render(request, 'arsip/detail.html', {'arsip': arsip})


@login_required
def arsip_upload(request):
    """Halaman upload arsip baru"""
    if request.method == 'POST':
        form = ArsipForm(request.POST, request.FILES)
        if form.is_valid():
            arsip = form.save(commit=False)
            arsip.size_bytes = request.FILES['file'].size
            arsip.save()
            messages.success(request, f'Arsip "{arsip.name}" berhasil diunggah.')
            return redirect('arsip:list')
    else:
        form = ArsipForm()

    return render(request, 'arsip/upload.html', {'form': form})


@login_required
def arsip_delete(request, pk):
    """Hapus arsip"""
    arsip = get_object_or_404(Arsip, pk=pk)

    if request.method == 'POST':
        nama = arsip.name
        arsip.delete()
        messages.success(request, f'Arsip "{nama}" berhasil dihapus.')
        return redirect('arsip:list')

    return render(request, 'arsip/delete.html', {'arsip': arsip})


@login_required
def folder_browse(request, pk=None):
    """Browse folder (tree view)"""
    if pk:
        current_folder = get_object_or_404(Folder, pk=pk, is_active=True)
    else:
        current_folder = None

    if current_folder:
        subfolders = Folder.objects.filter(
            parent=current_folder, is_active=True
        ).order_by('order', 'name')
        arsip_list = Arsip.objects.filter(
            folder=current_folder, is_active=True
        ).order_by('-uploaded_at')
    else:
        subfolders = Folder.objects.filter(
            parent__isnull=True, is_active=True
        ).order_by('order', 'name')
        arsip_list = Arsip.objects.none()

    breadcrumb = build_breadcrumb(current_folder) if current_folder else []
    full_tree = build_full_tree()

    context = {
        'current_folder': current_folder,
        'subfolders': subfolders,
        'arsip_list': arsip_list,
        'breadcrumb': breadcrumb,
        'full_tree': full_tree,
        'current_folder_id': current_folder.id if current_folder else None,
    }
    return render(request, 'arsip/folder_browse.html', context)
@login_required
def bulk_upload(request):
    """Bulk upload: banyak file ke 1 folder"""
    
    if request.method == 'POST':
        form = BulkArsipForm(request.POST, request.FILES)
        if form.is_valid():
            folder = form.cleaned_data['folder']
            files = form.cleaned_data['files']   # ← INI
            file_type = form.cleaned_data['file_type']
            creator = form.cleaned_data['creator']
            access_level = form.cleaned_data['access_level']
            
            success = 0
            errors = []
            
            for f in files:
                try:
                    arsip = Arsip(
                        name=f.name.rsplit('.', 1)[0],  # nama tanpa extension
                        folder=folder,
                        file_type=file_type,
                        size_bytes=f.size,
                        creator=creator,
                        access_level=access_level,
                    )
                    arsip.file.save(f.name, f, save=True)
                    success += 1
                except Exception as e:
                    errors.append(f"{f.name}: {e}")
            
            if success:
                messages.success(request, f'{success} file berhasil diupload ke "{folder.name}".')
            
            if errors:
                messages.error(request, f'{len(errors)} file gagal: ' + ', '.join(errors[:5]))
            
            return redirect('arsip:folder', pk=folder.pk)
    else:
        # Pre-select folder kalau ada ?folder=ID
        initial = {}
        folder_id = request.GET.get('folder')
        if folder_id:
            initial['folder'] = folder_id
        form = BulkArsipForm(initial=initial)
    
    return render(request, 'arsip/bulk_upload.html', {'form': form})
@login_required
def folder_upload(request):
    """Upload ZIP, auto-extract struktur folder"""
    from .forms import FolderUploadForm
    
    if request.method == 'POST':
        form = FolderUploadForm(request.POST, request.FILES)
        if form.is_valid():
            zip_file = request.FILES['zip_file']
            root_name = form.cleaned_data['root_fonds']
            year = form.cleaned_data['year']
            
            # Bikin fonds root
            fonds, _ = Folder.objects.get_or_create(
                name=root_name,
                parent=None,
                defaults={'level': 'fonds', 'year': year}
            )
            
            success_files = 0
            success_folders = 0
            errors = []
            
            try:
                with zipfile.ZipFile(zip_file, 'r') as z:
                    for member in z.namelist():
                        # Skip folder entry
                        if member.endswith('/'):
                            continue
                        
                        # Skip file system sampah
                        if member.startswith('__MACOSX') or '/.' in member:
                            continue
                        
                        parts = Path(member).parts
                        if len(parts) < 2:
                            continue
                        
                        # Bikin folder bertingkat
                        parent = fonds
                        level_map = ['subfonds', 'series', 'file']
                        
                        for i, part in enumerate(parts[:-1]):
                            level = level_map[min(i, len(level_map)-1)]
                            parent, created = Folder.objects.get_or_create(
                                name=part,
                                parent=parent,
                                defaults={'level': level, 'year': year}
                            )
                            if created:
                                success_folders += 1
                        
                        # Upload file
                        try:
                            file_data = z.read(member)
                            file_name = parts[-1]
                            ext = file_name.rsplit('.', 1)[-1].lower() if '.' in file_name else ''
                            
                            if ext in ('xlsx', 'xls'):
                                file_type = 'xlsx'
                            elif ext in ('docx', 'doc'):
                                file_type = 'docx'
                            elif ext == 'pdf':
                                file_type = 'pdf'
                            else:
                                file_type = 'lain'
                            
                            arsip = Arsip(
                                name=file_name.rsplit('.', 1)[0] if '.' in file_name else file_name,
                                folder=parent,
                                file_type=file_type,
                                size_bytes=len(file_data),
                            )
                            arsip.file.save(file_name, io.BytesIO(file_data), save=True)
                            success_files += 1
                        except Exception as e:
                            errors.append(f"{member}: {e}")
            
            except zipfile.BadZipFile:
                messages.error(request, 'File bukan ZIP yang valid.')
                return render(request, 'arsip/folder_upload.html', {'form': form})
            
            messages.success(request, 
                f'Berhasil! {success_folders} folder + {success_files} file diupload.')
            
            if errors:
                messages.error(request, f'{len(errors)} error: ' + ', '.join(errors[:5]))
            
            return redirect('arsip:folder', pk=fonds.pk)
    else:
        form = FolderUploadForm()
    
    return render(request, 'arsip/folder_upload.html', {'form': form})
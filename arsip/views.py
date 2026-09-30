from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Arsip, Folder
from .forms import ArsipForm
from .utils import build_breadcrumb, build_full_tree


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
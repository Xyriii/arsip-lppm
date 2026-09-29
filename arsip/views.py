from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Arsip, Folder


@login_required
def arsip_list(request):
    """Halaman daftar arsip + pencarian & filter"""
    query = request.GET.get('q', '')
    tahun = request.GET.get('tahun', '')
    kategori = request.GET.get('kategori', '')

    arsip_qs = Arsip.objects.select_related('folder').all()

    if query:
        arsip_qs = arsip_qs.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    if tahun:
        arsip_qs = arsip_qs.filter(folder__year=tahun)
    if kategori:
        arsip_qs = arsip_qs.filter(file_type=kategori)

    tahun_list = Folder.objects.values_list('year', flat=True).distinct().order_by('-year')

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
    arsip = get_object_or_404(Arsip, pk=pk)
    return render(request, 'arsip/detail.html', {'arsip': arsip})
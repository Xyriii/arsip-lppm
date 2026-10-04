from django.urls import path
from . import views

app_name = 'arsip'

urlpatterns = [
    path('', views.arsip_list, name='list'),
    path('browse/', views.folder_browse, name='browse'),
    path('browse/<int:pk>/', views.folder_browse, name='folder'),
    path('upload/', views.arsip_upload, name='upload'),
    path('<int:pk>/', views.arsip_detail, name='detail'),
    path('<int:pk>/delete/', views.arsip_delete, name='delete'),
    path('bulk-upload/', views.bulk_upload, name='bulk_upload'),
    path('folder-upload/', views.folder_upload, name='folder_upload'),
]
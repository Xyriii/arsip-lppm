from django.urls import path
from . import views

app_name = 'arsip'

urlpatterns = [
    path('', views.arsip_list, name='list'),
    path('<int:pk>/', views.arsip_detail, name='detail'),
    path('<int:pk>/edit/', views.arsip_edit, name='arsip_edit'),
    path('<int:pk>/delete/', views.arsip_delete, name='delete'),
    
    path('upload/', views.arsip_upload, name='upload'),
    path('bulk-upload/', views.bulk_upload, name='bulk_upload'),
    path('folder-upload/', views.folder_upload, name='folder_upload'),
    
    path('browse/', views.folder_browse, name='browse'),
    path('browse/<int:pk>/', views.folder_browse, name='folder'),
    path('folder/<int:pk>/edit/', views.folder_edit, name='folder_edit'),
    
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/toggle/', views.user_toggle_active, name='user_toggle'),
    path('users/<int:pk>/reset/', views.user_reset_password, name='user_reset'),
    
    path('public/', views.public_home, name='public_home'),
    path('export/excel/', views.export_excel, name='export_excel'),
]
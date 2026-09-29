from django.urls import path
from . import views

app_name = 'arsip'

urlpatterns = [
    path('', views.arsip_list, name='list'),
    path('<int:pk>/', views.arsip_detail, name='detail'),
]
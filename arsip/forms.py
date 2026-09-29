from django import forms
from .models import Arsip


class ArsipForm(forms.ModelForm):
    class Meta:
        model = Arsip
        fields = ['name', 'file_type', 'folder', 'description', 'file']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Masukkan nama arsip',
            }),
            'file_type': forms.Select(attrs={'class': 'select'}),
            'folder': forms.Select(attrs={'class': 'select'}),
            'description': forms.Textarea(attrs={
                'class': 'textarea',
                'placeholder': 'Keterangan singkat tentang arsip ini...',
                'rows': 4,
            }),
            'file': forms.ClearableFileInput(attrs={'class': 'input'}),
        }
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Arsip, Folder

# ============================================
# CUSTOM WIDGET UNTUK MULTIPLE FILE UPLOAD
# ============================================
class MultipleFileInput(forms.FileInput):
    """Custom widget yang ngizinin multiple file"""
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    """Custom field yang handle multiple file"""
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)
    
    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class ArsipForm(forms.ModelForm):
    """Form upload arsip tunggal"""
    
    class Meta:
        model = Arsip
        fields = ['name', 'folder', 'file', 'file_type', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nama file arsip'}),
            'folder': forms.Select(attrs={'class': 'input'}),
            'file': forms.FileInput(attrs={'class': 'input', 'accept': '.pdf,.xlsx,.xls,.docx,.doc'}),
            'file_type': forms.Select(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'input', 'rows': 4}),
        }
        labels = {
            'name': 'Nama File',
            'folder': 'Folder',
            'file': 'File',
            'file_type': 'Kategori',
            'description': 'Keterangan',
        }


class StaffCreationForm(UserCreationForm):
    """Form bikin akun staff baru"""
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'
        
        self.fields['username'].label = 'Username'
        self.fields['first_name'].label = 'Nama Depan'
        self.fields['last_name'].label = 'Nama Belakang'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Konfirmasi Password'


class BulkArsipForm(forms.Form):
    """Form bulk upload ke folder tertentu"""
    
    folder = forms.ModelChoiceField(
        queryset=Folder.objects.filter(is_active=True),
        label='Folder Tujuan',
        widget=forms.Select(attrs={'class': 'input'})
    )
    files = MultipleFileField(  # <-- pakai custom field
        label='File (bisa pilih banyak)',
        widget=MultipleFileInput(attrs={
            'class': 'input',
            'multiple': True,
            'accept': '.pdf,.xlsx,.xls,.docx,.doc,.jpg,.jpeg,.png'
        })
    )
    file_type = forms.ChoiceField(
        choices=Arsip.FILE_TYPE_CHOICES,
        label='Tipe File (default)',
        widget=forms.Select(attrs={'class': 'input'}),
        initial='pdf'
    )
    creator = forms.CharField(
        max_length=255,
        required=False,
        label='Pencipta (opsional)',
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Contoh: LPPM UNS'})
    )
    access_level = forms.CharField(
        max_length=50,
        required=False,
        initial='Terbatas',
        label='Level Akses',
        widget=forms.TextInput(attrs={'class': 'input'})
    )


class FolderUploadForm(forms.Form):
    """Form upload folder ZIP dengan auto-organize"""
    
    zip_file = forms.FileField(
        label='File ZIP',
        widget=forms.ClearableFileInput(attrs={'class': 'input', 'accept': '.zip'}),
        help_text='Upload file .zip yang isinya folder arsip. Struktur folder akan otomatis dibuat.'
    )
    root_fonds = forms.CharField(
        max_length=255,
        label='Nama Fonds (level tertinggi)',
        initial='Arsip LPPM UNS',
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    year = forms.IntegerField(
        label='Tahun',
        initial=2026,
        widget=forms.NumberInput(attrs={'class': 'input'})
    )
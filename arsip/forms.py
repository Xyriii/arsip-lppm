from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Arsip, Folder


# ============================================
# CUSTOM WIDGET UNTUK MULTIPLE FILE
# ============================================
class MultipleFileInput(forms.FileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
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


# ============================================
# FORM ARSIP TUNGGAL
# ============================================
class ArsipForm(forms.ModelForm):
    class Meta:
        model = Arsip
        fields = ['name', 'file_type', 'folder', 'description', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Masukkan nama arsip'}),
            'file_type': forms.Select(attrs={'class': 'select'}),
            'folder': forms.Select(attrs={'class': 'select'}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Keterangan singkat...', 'rows': 4}),
            'file': forms.ClearableFileInput(attrs={'class': 'input'}),
        }


# ============================================
# FORM BULK UPLOAD (BANYAK FILE)
# ============================================
class BulkArsipForm(forms.Form):
    folder = forms.ModelChoiceField(
        queryset=Folder.objects.filter(is_active=True),
        label='Folder Tujuan',
        widget=forms.Select(attrs={'class': 'input'})
    )
    files = MultipleFileField(
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
        max_length=255, required=False,
        label='Pencipta (opsional)',
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    access_level = forms.CharField(
        max_length=50, required=False,
        initial='Terbatas',
        label='Level Akses',
        widget=forms.TextInput(attrs={'class': 'input'})
    )


# ============================================
# FORM UPLOAD FOLDER ZIP
# ============================================
class FolderUploadForm(forms.Form):
    zip_file = forms.FileField(
        label='File ZIP',
        widget=forms.FileInput(attrs={'class': 'input', 'accept': '.zip'}),
        help_text='Upload file .zip yang isinya folder arsip.'
    )
    root_fonds = forms.CharField(
        max_length=255,
        label='Nama Fonds',
        initial='Arsip LPPM UNS',
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    year = forms.IntegerField(
        label='Tahun',
        initial=2026,
        widget=forms.NumberInput(attrs={'class': 'input'})
    )


# ============================================
# FORM USER MANAGEMENT
# ============================================
class StaffCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('user', 'User (read-only)'),
        ('admin', 'Admin (full access)'),
    ]
    
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        label='Role',
        initial='user',
        widget=forms.Select(attrs={'class': 'input'})
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'role')
    
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
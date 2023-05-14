from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku

class FormBuku(ModelForm):
  class Meta:
    model = Buku
    exclude = ['encpath']

    widgets = {
      'judul'    : forms.TextInput({'class':'form-control'}),
      'penulis'  : forms.TextInput({'class':'form-control'}),
      'penerbit' : forms.TextInput({'class':'form-control'}),
      #'jumlah'   : forms.NumberInput({'class':'form-control'}),
    }
  
class FileUploadForm(forms.Form):
  file1 = forms.FileField(label='File Terenkripsi')
  file2 = forms.FileField(label='File Key Enc')


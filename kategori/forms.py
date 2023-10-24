from django import forms

class TambahKategori(forms.Form):
    nama_kategori = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'Masukkan Nama Kategori'}))


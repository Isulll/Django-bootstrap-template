from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . forms import TambahKategori
from kategori.models import Kategori
from django.urls import reverse

# Create your views here.
def kategori(request):
    current_user = request.user
    kategori = Kategori.objects.all()
    return render(request, 'kategori.html', {'user' : current_user,'kategori' : kategori})

def create(request):
    form = TambahKategori
    return render(request, 'tambah_kategori.html', {'form' : form})

def store(request):
    if request.method == 'POST':
        form = TambahKategori(request.POST)
        if form.is_valid():
            nama_kategori = form.cleaned_data['nama_kategori']
            Kategori.objects.create(nama_kategori = nama_kategori)
            messages.success(request, 'Tambah Kategori Berhasil')
            return redirect('kategori.create')

        else:
            return render(request, 'tambah_kategori.html', {'form' : form})
        
def delete(request, id):
    kategori = get_object_or_404(Kategori, id=id)
    kategori.delete()
    return redirect('kategori')

def edit(request, id):
    kategori = get_object_or_404(Kategori, id=id)
    form = TambahKategori(initial = {'nama_kategori' : kategori.nama_kategori})
    return render(request, 'edit_kategori.html', {'kategori' : kategori, 'form' : form})

def update(request,id):
    if request.method == 'POST':
        kategori = get_object_or_404(Kategori, id=id)
        form = TambahKategori(request.POST, initial={'nama_kategori' : kategori.nama_kategori})
        if form.is_valid():
            nama_kategori = form.cleaned_data['nama_kategori']
            kategori.nama_kategori = nama_kategori
            kategori.save()
            messages.success(request, 'Update Kategori Berhasil')
            url = reverse('kategori.edit', kwargs={'id': kategori.id})
            return redirect(url)
        else:
            return render('kategori.edit', {'form': form, 'kategori': kategori})

            
    




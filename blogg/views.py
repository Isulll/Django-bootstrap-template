from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import BlogForm
from blogg.models import Blog

# Create your views here.
def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog' : blog})

def create(request):
    instance = Blog(author=request.user.username)
    form = BlogForm(instance=instance)
    return render(request, 'blog_create.html', {'form' : form})

def store(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            nama_kategori = form.cleaned_data['nama_kategori']
            Blog.objects.create(nama_kategori = nama_kategori)
            messages.success(request, 'Tambah Kategori Berhasil')
            return redirect('blog.create')

        else:
            return render(request, 'blog_create.html', {'form' : form})

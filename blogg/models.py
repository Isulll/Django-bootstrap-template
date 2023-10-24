from django.db import models
from kategori.models import Kategori

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    nama_kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title


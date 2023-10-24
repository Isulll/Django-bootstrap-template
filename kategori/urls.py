from django.urls import path
from . import views

urlpatterns = [
    path('kategori', views.kategori, name = 'kategori'),
    path('create', views.create, name = 'kategori.create'),
    path('store', views.store, name = 'kategori.store'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('edit/<int:id>', views.edit, name = 'kategori.edit'),
    path('update/<int:id>', views.update, name = 'kategori.update'),
    
]
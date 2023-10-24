from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog , name = 'blog'),
    path('create', views.create, name = 'blog.create'),
    path('store', views.store, name = 'blog.store'),
    # path('edit/<int:id>', views.edit, name = 'kategori.edit'),
    # path('update/<int:id>', views.update, name = 'kategori.update'),  
]
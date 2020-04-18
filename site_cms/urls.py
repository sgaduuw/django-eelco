from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('tags/', views.taxonomy_list_all, { 'taxonomy_type': 'tags' }),
    path('tag/<slug:taxonomy_name>/', views.taxonomy_list_single, { 'taxonomy_type': 'tag' }),

    path('categories/', views.taxonomy_list_all, { 'taxonomy_type': 'categories' }),
    path('category/<slug:taxonomy_name>/', views.taxonomy_list_single, { 'taxonomy_type': 'category' }),

    path('author/<slug:author>', views.author, name='author'),
    path('<int:year>/<slug:slug>/', views.blog, name='blog'),
    path('<slug:slug>/', views.page, name='page'),
]
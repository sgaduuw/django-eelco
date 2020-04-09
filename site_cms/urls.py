from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('tags/', views.tag_list, name='tag_list'),
    path('tag/<slug:taxonomy>/', views.taxonomy_detail, { 'taxonomy_type': 'tag' }),

    path('categories/', views.category_list, name='category_list'),
    path('category/<slug:taxonomy>/', views.taxonomy_detail, { 'taxonomy_type': 'category' }),

    path('author/<slug:author>', views.author, name='author'),
    path('<int:year>/<slug:slug>/', views.blog, name='blog'),
    path('<slug:slug>/', views.page, name='page'),
]
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('author/<slug:author>', views.author, name='author'),
    path('<int:year>/<slug:slug>/', views.blog, name='blog'),
    path('<slug:slug>/', views.page, name='page'),
    #path('<int:year>/', views.page, name='page'),
    #re_path(r'^(?P<year>[0-9]{4})/<slug:content.slug>/$', views.page, name='page'),
]
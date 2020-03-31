from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.BlogPostView.as_view(), name='page'),
    #path('<int:year>/', views.page, name='page'),
    #re_path(r'^(?P<year>[0-9]{4})/<slug:content.slug>/$', views.page, name='page'),
]
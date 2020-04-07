from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from site_cms.models import Content, Author, Tag, Category

def index(request):
    """ Front page listing """
    blog_post_list = Content.objects.filter(ctype='1', contentstatus='2')
    page_post_list = Content.objects.filter(ctype='2', contentstatus='2')
    content = Content.objects.all()
    
    context = {
        'blog_post_list': blog_post_list,
        'page_post_list': page_post_list,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def author(request, author):
    """ Author page """
    author = Content.objects.filter(author__name__iexact=author)
    context = {
        'author': author,
    }
    return render(request, 'author.html', context=context)

def page(request, slug):
    """ 'static' page """
    context = {
        'slug': slug,
    }
    return render(request, 'page.html', context=context)

def blog(request, year, slug):
    """ Blog page """
    content = Content.objects.get(slug=slug, publishdate__year=str(year))

    context = {
        'year': year,
        'slug': slug,
        'content': content,
    }

    return render(request, 'blog.html', context=context)

def tag_list(request):
    """ Tag listing """
    tags = Tag.objects.all()
    
    context = {
        'tags': tags,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'tags.html', context=context)

def tag_detail(request, tag):
    """ Single tag page """
    tag = Tag.objects.filter(name=tag)

    context = {
        'tag': tag,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'tag_detail.html', context=context)
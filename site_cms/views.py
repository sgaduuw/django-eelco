from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from site_cms.models import Content, Author

def index(request):
    """ Front page placeholder """
    num_blog_posts = Content.objects.filter(ctype='1').count()
    num_page_posts = Content.objects.filter(ctype='2').count()
    blog_post_list = Content.objects.filter(ctype='1', contentstatus='2')
    page_post_list = Content.objects.filter(ctype='2', contentstatus='2')
    num_authors = Author.objects.count()

    context = {
        'num_blog_posts': num_blog_posts,
        'num_page_posts': num_page_posts,
        'num_authors': num_authors,
        'blog_post_list': blog_post_list,
        'page_post_list': page_post_list,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def author(request, author):
    author = Content.objects.filter(author__name__iexact=author)
    context = {
        'author': author,
    }
    return render(request, 'author.html', context=context)

def page(request, slug):

    context = {
        'slug': slug,
    }
    return render(request, 'page.html', context=context)

def blog(request, year, slug):

    content = Content.objects.get(slug=slug, publishdate__year=str(year))

    context = {
        'year': year,
        'slug': slug,
        'content': content,
    }

    return render(request, 'blog.html', context=context)
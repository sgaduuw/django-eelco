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
        'listingheader': 'Blog',
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
    def get_tag_postcount(tagname):
        postcount = Content.objects.filter(tags__name__iexact=tagname).count()
        return postcount

    tags = {}
    for tag in Tag.objects.all():
        tags[tag.name] = {}
        tags[tag.name]['description'] = tag.description
        tags[tag.name]['count'] = get_tag_postcount(tagname=tag)

    context = {
        'listingheader': 'Tags',
        'tags': tags,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'tags.html', context=context)

def category_list(request):
    """ Category listing """
    def get_cat_postcount(category):
        postcount = Content.objects.filter(categories__name__iexact=category).count()
        return postcount

    categories = {}
    for cat in Tag.objects.all():
        categories[cat.name] = {}
        categories[cat.name]['description'] = cat.description
        categories[cat.name]['count'] = get_cat_postcount(category)

    context = {
        'listingheader': 'Categories',
        'tags': tags,
    }

def taxonomy_detail(request, taxonomy, taxonomy_type):
    """ Single taxonomy page """
    taxonomy = Tag.objects.filter(name=taxonomy)

    context = {
        'taxonomy_type': taxonomy_type,
        'taxonomy': taxonomy,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'taxonomy_detail.html', context=context)
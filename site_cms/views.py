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
        'listingheader': 'blog',
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

def taxonomy_list_all(request, taxonomy_type):
    """ Taxonomy listing """
    if taxonomy_type == 'tags':
        q = Tag.objects.all()
    elif taxonomy_type == 'categories':
        q = Category.objects.all()

    def get_cat_postcount(taxonomy):
        if taxonomy_type == 'tags':
            postcount = Content.objects.filter(tags__name__iexact=taxonomy).count()
        elif taxonomy_type == 'categories':
            postcount = Content.objects.filter(categories__name__iexact=taxonomy).count()
        return postcount

    taxonomy = {}
    for tax in q:
        taxonomy[tax.name] = {}
        taxonomy[tax.name]['description'] = tax.description
        taxonomy[tax.name]['count'] = get_cat_postcount(tax.name)

    context = {
        'listingheader': taxonomy_type,
        'taxonomy': taxonomy,
    }

    return render(request, 'taxonomy_list_all.html', context=context)

def taxonomy_list_single(request, taxonomy_name, taxonomy_type):
    """ Single taxonomy page """
    if taxonomy_type == 'tag':
        content = Content.objects.filter(ctype='1', tags__name__iexact=taxonomy_name)
    elif taxonomy_type == 'category':
        content = Content.objects.filter(ctype='1', categories__name__iexact=taxonomy_name)

    context = {
        'listingheader': taxonomy_type + ": " + taxonomy_name,
        'taxonomy_type': taxonomy_type,
        'content': content,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'taxonomy_list_single.html', context=context)
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from site_cms.models import Content, Author, Tag, Category

def index(request):
    """ Front page listing """
    blog_post_list = Content.objects.filter(ctype='1', contentstatus='2', siteinfo__domains=request.site)
    page_post_list = Content.objects.filter(ctype='2', contentstatus='2', siteinfo__domains=request.site)
    content = Content.objects.filter(siteinfo__domains=request.site)
    
    context = {
        'listingheader': 'blog: ' + str(request.site),
        'blog_post_list': blog_post_list,
        'page_post_list': page_post_list,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def author(request, author):
    """ Author page """
    author = Content.objects.filter(author__name__iexact=author, siteinfo__domains=request.site)
    context = {
        'author': author,
    }
    return render(request, 'author.html', context=context)

def page(request, slug):
    """ 'static' page """
    content = Content.objects.get(slug=slug, ctype='2', siteinfo__domains=request.site)

    context = {
        'slug': slug,
        'content': content,
        'full_canonical_url': request.build_absolute_uri
    }
    
    return render(request, 'page.html', context=context)

def blog(request, year, slug):
    """ Blog page """
    content = Content.objects.get(slug=slug, publishdate__year=str(year), ctype='1', siteinfo__domains=request.site)

    context = {
        'year': year,
        'slug': slug,
        'content': content,
        'full_canonical_url': request.build_absolute_uri
    }

    return render(request, 'blog.html', context=context)

def taxonomy_list_all(request, taxonomy_type):
    """ Taxonomy listing """
    if taxonomy_type == 'tag':
        q = Tag.objects.filter(site=request.site)
    elif taxonomy_type == 'category':
        q = Category.objects.filter(site=request.site)

    def get_cat_postcount(taxonomy):
        if taxonomy_type == 'tag':
            postcount = Content.objects.filter(tags__name__iexact=taxonomy, siteinfo__domains=request.site).count()
        elif taxonomy_type == 'category':
            postcount = Content.objects.filter(categories__name__iexact=taxonomy, siteinfo__domains=request.site).count()
        return postcount

    def get_listing_header():
        return 'tags' if taxonomy_type == 'tag' else 'categories'

    taxonomy = {}
    for tax in q:
        taxonomy[tax.name] = {}
        taxonomy[tax.name]['description'] = tax.description
        taxonomy[tax.name]['count'] = get_cat_postcount(tax.name)

    context = {
        'listingheader': get_listing_header(),
        'taxonomy_type': taxonomy_type,
        'taxonomy': taxonomy,
    }

    return render(request, 'taxonomy_list_all.html', context=context)

def taxonomy_list_single(request, taxonomy_name, taxonomy_type):
    """ Single taxonomy page """
    if taxonomy_type == 'tag':
        content = Content.objects.filter(ctype='1', tags__name__iexact=taxonomy_name, siteinfo__domains=request.site)
    elif taxonomy_type == 'category':
        content = Content.objects.filter(ctype='1', categories__name__iexact=taxonomy_name, siteinfo__domains=request.site)

    context = {
        'listingheader': taxonomy_type + ": " + taxonomy_name,
        'taxonomy_type': taxonomy_type,
        'content': content,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'taxonomy_list_single.html', context=context)
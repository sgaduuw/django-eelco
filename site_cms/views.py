from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from site_cms.models import Content, Author

def index(request):
    """ Front page placeholder """
    num_blog_posts = Content.objects.count()
    post_list = Content.objects.all()
    num_authors = Author.objects.count()

    context = {
        'num_blog_posts': num_blog_posts,
        'num_authors': num_authors,
        'post_list': post_list,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BlogPostView(generic.DetailView):
    model = Content
    template_name = 'page.html'
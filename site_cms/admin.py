from django.contrib import admin
from .models import Site, Sitedomain, Author, Tag, Category, Attachment, Content, ContentMeta


# Register your models here.
admin.site.register(Site)
admin.site.register(Sitedomain)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Attachment)
admin.site.register(Content)
admin.site.register(ContentMeta)
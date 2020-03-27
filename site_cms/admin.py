from django.contrib import admin
from .models import Siteinfo, Author, Tag, Category, Attachment, Content, ContentMeta

class AuthorDisplay(admin.ModelAdmin):
    list_display = ('name', 'email', 'bio')

class TagDisplay(admin.ModelAdmin):
    list_display = ('name', 'description')

class CategoryDisplay(admin.ModelAdmin):
    list_display = ('name', 'description')

# Register your models here.
admin.site.register(Siteinfo)
admin.site.register(Author, AuthorDisplay)
admin.site.register(Tag, TagDisplay)
admin.site.register(Category, CategoryDisplay)
admin.site.register(Attachment)
admin.site.register(Content)
admin.site.register(ContentMeta)
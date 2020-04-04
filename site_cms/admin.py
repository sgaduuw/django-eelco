from django.contrib import admin
from .models import Siteinfo, Author, Tag, Category, Attachment, Content

class AuthorDisplay(admin.ModelAdmin):
    list_display = ('name', 'email', 'bio')

class TagDisplay(admin.ModelAdmin):
    list_display = ('name', 'description')

class CategoryDisplay(admin.ModelAdmin):
    list_display = ('name', 'description')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'contentstatus', 'publishdate', 'author', 'ctype', 'description', 'body'[:20])
    fields = [
        ('siteinfo'),
        ('title', 'slug'), 
        ('description', 'author'),
        ('image'),
        ('contentstatus', 'publishdate'),
        ('body'),
        ('ctype', 'attachments'),
        ('categories', 'tags')
    ]
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Siteinfo)
admin.site.register(Author, AuthorDisplay)
admin.site.register(Tag, TagDisplay)
admin.site.register(Category, CategoryDisplay)
admin.site.register(Attachment)
admin.site.register(Content,ContentAdmin)
from django.db import models
from django.urls import reverse
from django.contrib.sites.models import Site

import uuid

# Create your models here.
class Siteinfo(models.Model):
    name = models.CharField(max_length=200, help_text='Enter site name')
    title = models.CharField(max_length=200, help_text='Enter site title')
    owner = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    tagline = models.CharField(max_length=200, help_text='Enter site tagline')
    domains = models.ManyToManyField(Site)
    description = models.CharField(max_length=200, help_text='Enter site description')
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200, help_text='Enter author name')
    email = models.EmailField(max_length=200, help_text='Enter author email')
    bio = models.CharField(max_length=200, help_text='Enter author bio')
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Contenttype(models.IntegerChoices):
    BLOG = 1
    PAGE = 2

class ContentStatus(models.IntegerChoices):
    DRAFT = 1
    PUBLISHED = 2

class Attachment(models.Model):
    name = models.CharField(max_length=200, help_text='Enter file name')
    fpath = models.FileField(upload_to='uploads/%Y/%m/%d/')
    date = models.DateTimeField('date published')
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for post')
    siteinfo = models.ForeignKey('Siteinfo', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, help_text='Enter taxonomy name')
    ctype = models.IntegerField(choices=Contenttype.choices, verbose_name='Content type')
    body = models.TextField(help_text='Enter content here')
    attachments = models.ManyToManyField('Attachment', blank=True)
    contentstatus = models.IntegerField(choices=ContentStatus.choices, verbose_name='Content status')
    slug = models.SlugField(max_length=250, help_text='Enter slug', blank=True)
    publishdate = models.DateTimeField('Publish date', auto_now_add=True, blank=True)
    description = models.CharField(max_length=200, help_text='Enter taxonomy name')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    image = models.ImageField(upload_to='pageimage/%Y/%m/%d/', null=True, blank=True)

    def get_year(self):
        return self.publishdate.year

    def get_absolute_url(self):
        if self.ctype == 1:
            return reverse('blog', kwargs={'year': self.get_year(), 'slug': self.slug})
        elif self.ctype == 2:
            return reverse('page', kwargs={'slug': self.slug})

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=200, help_text='Enter Tag name')
    description = models.CharField(max_length=200, help_text='Enter Tag description')
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Enter Category name')
    description = models.CharField(max_length=200, help_text='Enter Category description')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        """String for representing the Model object."""
        return self.name
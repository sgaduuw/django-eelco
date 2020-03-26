from django.db import models
from django.urls import reverse

import uuid

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=200, help_text='Enter site name')
    title = models.CharField(max_length=200, help_text='Enter site title')
    owner = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    tagline = models.CharField(max_length=200, help_text='Enter site tagline')
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

class Attachment(models.Model):
    name = models.CharField(max_length=200, help_text='Enter file name')
    fpath = models.FileField(upload_to='uploads/%Y/%m/%d/')
    date = models.DateTimeField('date published')
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for post')
    site = models.ForeignKey('Site', on_delete=models.SET_NULL, null=True)
    ctype = models.IntegerField(choices=Contenttype.choices)
    body = models.TextField(help_text='Enter content here')
    attachments = models.ManyToManyField('Attachment', blank=True)
    metadata = models.ForeignKey('ContentMeta', on_delete=models.SET_NULL, null=True)
    pub_notbefore = models.DateTimeField('Not before')
    pub_notafter = models.DateTimeField('Not after')
    def __str__(self):
        """String for representing the Model object."""
        return self.body

class ContentMeta(models.Model):
    title = models.CharField(max_length=200, help_text='Enter taxonomy name')
    description = models.CharField(max_length=200, help_text='Enter taxonomy name')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=50, help_text='Enter slug', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    image = models.ImageField(upload_to='pageimage/%Y/%m/%d/', null=True, blank=True)
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
    def __str__(self):
        """String for representing the Model object."""
        return self.name
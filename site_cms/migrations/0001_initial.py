# Generated by Django 3.0.4 on 2020-04-07 18:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter file name', max_length=200)),
                ('fpath', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter author name', max_length=200)),
                ('email', models.EmailField(help_text='Enter author email', max_length=200)),
                ('bio', models.CharField(help_text='Enter author bio', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Category name', max_length=200)),
                ('description', models.CharField(help_text='Enter Category description', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Tag name', max_length=200)),
                ('description', models.CharField(help_text='Enter Tag description', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Siteinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter site name', max_length=200)),
                ('title', models.CharField(help_text='Enter site title', max_length=200)),
                ('tagline', models.CharField(help_text='Enter site tagline', max_length=200)),
                ('description', models.CharField(help_text='Enter site description', max_length=200)),
                ('copyright', models.CharField(blank=True, help_text='Enter site copyright', max_length=200, null=True)),
                ('footer', models.CharField(blank=True, help_text='Enter site copyright footer', max_length=200, null=True)),
                ('domains', models.ManyToManyField(to='sites.Site')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_cms.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for post', primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Enter taxonomy name', max_length=200)),
                ('ctype', models.IntegerField(choices=[(1, 'Blog'), (2, 'Page')], verbose_name='Content type')),
                ('body', models.TextField(help_text='Enter content here')),
                ('contentstatus', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], verbose_name='Content status')),
                ('slug', models.SlugField(blank=True, help_text='Enter slug', max_length=250)),
                ('publishdate', models.DateTimeField(verbose_name='Publish date')),
                ('description', models.CharField(help_text='Enter taxonomy name', max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pageimage/%Y/%m/%d/')),
                ('attachments', models.ManyToManyField(blank=True, to='site_cms.Attachment')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_cms.Author')),
                ('categories', models.ManyToManyField(blank=True, to='site_cms.Category')),
                ('siteinfo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_cms.Siteinfo')),
                ('tags', models.ManyToManyField(blank=True, to='site_cms.Tag')),
            ],
            options={
                'ordering': ['-publishdate'],
            },
        ),
    ]
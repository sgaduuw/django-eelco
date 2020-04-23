# Generated by Django 3.0.5 on 2020-04-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('site_cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='site',
            field=models.ManyToManyField(to='sites.Site'),
        ),
        migrations.AddField(
            model_name='tag',
            name='site',
            field=models.ManyToManyField(to='sites.Site'),
        ),
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.CharField(help_text='Enter description', max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(help_text='Enter title', max_length=200),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='copyright',
            field=models.CharField(blank=True, help_text='Enter site copyright line 1', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='footer',
            field=models.CharField(blank=True, help_text='Enter site copyright line 2', max_length=200, null=True),
        ),
    ]
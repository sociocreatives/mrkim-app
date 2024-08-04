# Generated by Django 4.2.14 on 2024-08-01 15:14

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='main_categories')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main_categories')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Main Categories',
            },
        ),
        migrations.CreateModel(
            name='ExpertTips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/blog/')),
            ],
            options={
                'verbose_name_plural': 'Expert Tips',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='website.category')),
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
            },
        ),
    ]

# Generated by Django 5.0.2 on 2025-01-03 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='title')),
                ('message', models.TextField(blank=True, null=True, verbose_name='message')),
                ('image', models.ImageField(blank=True, null=True, upload_to='data/about-us', verbose_name='image')),
                ('link', models.CharField(blank=True, max_length=500, null=True, verbose_name='link')),
                ('address', models.CharField(blank=True, max_length=300, null=True, verbose_name='address')),
                ('coordinates', models.CharField(blank=True, max_length=100, null=True, verbose_name='coordinates')),
                ('additional_text', models.TextField(blank=True, null=True, verbose_name='additional text')),
            ],
            options={
                'verbose_name': 'about us',
                'verbose_name_plural': 'about us page',
            },
        ),
    ]

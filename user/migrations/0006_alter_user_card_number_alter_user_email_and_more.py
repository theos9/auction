# Generated by Django 5.0.2 on 2025-01-04 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auctionspermission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='card_number',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='card number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='family',
            field=models.CharField(max_length=20, null=True, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='national_id',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='national id'),
        ),
    ]

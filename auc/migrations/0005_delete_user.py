# Generated by Django 5.0.2 on 2025-01-07 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auc', '0004_category_auctionmodel_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
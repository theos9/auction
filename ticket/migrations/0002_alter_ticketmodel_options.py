# Generated by Django 5.0.2 on 2025-01-01 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketmodel',
            options={'verbose_name': 'Ticket', 'verbose_name_plural': 'Tickets'},
        ),
    ]

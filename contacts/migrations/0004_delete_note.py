# Generated by Django 3.2.6 on 2021-08-11 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_note'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
    ]

# Generated by Django 2.2.16 on 2022-05-11 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='genres',
            new_name='genre',
        ),
    ]
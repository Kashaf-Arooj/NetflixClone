# Generated by Django 4.2 on 2024-05-28 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_movie_cast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
    ]

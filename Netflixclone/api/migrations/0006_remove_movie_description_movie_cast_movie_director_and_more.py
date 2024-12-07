# Generated by Django 4.2 on 2024-05-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_image_movie_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='description',
        ),
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_story',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=None),
        ),
    ]

# Generated by Django 4.2 on 2024-05-30 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_rename_video_link_movie_movie_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='trailer_video',
            field=models.ImageField(null=True, upload_to='movies'),
        ),
    ]

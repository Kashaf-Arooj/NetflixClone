from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


MOVIE_CHOICES = (
    ('comedy', 'Comedy'),
    ('action', 'Action'),
    ('fantasy', 'Fantasy'),
    ('adventure', 'Adventure'),
)

# class CustomUser(AbstractUser):
#     profiles = models.ManyToManyField('Profile', blank=True)


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(default=None)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    trailer_video =  models.FileField(upload_to='movies', null=True)
    movie_link = models.CharField(max_length=1000, default="")
    cover_image = models.ImageField(upload_to='covers')
    director=models.CharField(max_length=100, default="")
    release_date=models.DateField(auto_now_add=False, null=True)
    movie_story = models.TextField(default="")
    cast = models.TextField(default="")


    def __str__(self):
        return self.title
    
class ProImage(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name = "images")
    image = models.ImageField(upload_to="img", default="", null=True, blank=True)

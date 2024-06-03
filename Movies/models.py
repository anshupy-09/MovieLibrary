from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    plot = models.TextField()
    poster_url = models.URLField(max_length=200, blank=True, null=True)  # Added field for storing poster URL

    def __str__(self):
        return f"{self.title} ({self.year})"

class MovieList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    privacy = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')], default='private')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie, related_name='movie_lists')

    def __str__(self):
        return self.title

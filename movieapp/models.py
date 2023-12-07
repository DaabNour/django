from django.db import models
#from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_date = models.DateField()
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('romantic', 'Romantic'),
        ('comedy', 'Comedy'),
        ('horror', 'Horror'),
        ('drama', 'Drama'),
        ('science', 'Science'),
     
    ]
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    description=models.TextField(default="",blank=True)

    class Meta:
        ordering = ['release_date']

    def __str__(self):
        return self.title
        
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
     

    def __str__(self):
        return f"Review for {self.movie.title} on {self.review_date}"

    class Meta:
        ordering = ['review_date']
    
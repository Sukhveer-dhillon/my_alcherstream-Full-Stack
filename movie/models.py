from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    # to add to favourites
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter()
    newmanager=NewManager()
    objects=models.Manager()

    title=models.CharField(max_length=500)
    vote_average=models.CharField(max_length=100)
    overview=models.TextField()
    # image=models.ImageField(default='default.jpg', upload_to='movie_pics')
    poster_path=models.CharField(max_length=200,default=None)
    # to add movie to favourite
    favourites=models.ManyToManyField(User,related_name="favourite",default=None,blank=True)
    
    def __str__(self):
        return self.title
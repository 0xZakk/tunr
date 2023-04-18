from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=120)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')

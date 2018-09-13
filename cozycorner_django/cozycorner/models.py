from django.db import models

# Create your models here.

class Bouquet(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    cost = models.CharField(max_length=100)
    season = models.CharField(default="season", max_length=100)
    flowers = models.CharField(default="flowers", max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey('auth.User', related_name = 'favorites', on_delete=models.CASCADE)

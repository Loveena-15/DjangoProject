from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Artwork(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    description = models.TextField()
    image_url = models.URLField()
    fallback_color = models.CharField(max_length=7, default='#000000')
    width = models.FloatField(default=3.0)
    height = models.FloatField(default=4.0)
    position_x = models.FloatField(default=0)
    position_y = models.FloatField(default=3)
    position_z = models.FloatField(default=0)
    rotation_y = models.FloatField(default=0)

    def __str__(self):
        return f"{self.title} by {self.artist}"  
    
    def __str__(self):
        return self.user.username
    
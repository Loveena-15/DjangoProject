from django.db import models
from django.contrib.auth.models import User

# You can create additional user profile models if needed
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you want to store
    
    def __str__(self):
        return self.user.username
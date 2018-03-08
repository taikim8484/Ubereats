from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Restaurant(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, related_name = 'restaurant')
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 200)
    logo = models.ImageField(upload_to = 'restaurant_logo/',blank=False)

    def __str__(self):
        return self.name
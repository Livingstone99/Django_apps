from django.db import models

# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to= 'img/')
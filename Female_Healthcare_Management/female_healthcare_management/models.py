from django.db import models
import requests
# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    description =models.TextField(null=True)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(null=True,upload_to='doctor_images/') 

    def __str__(self):
        return self.name


    
    

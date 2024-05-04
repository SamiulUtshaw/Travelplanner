from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Plantrip(models.Model):
    departure = models.CharField(max_length=20)
    destination = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()
    starttime = models.TimeField(auto_now=False, auto_now_add=False)
    endtime = models.TimeField(auto_now=False, auto_now_add=False)
    grouptrip = models.BooleanField(default=False)
    solotrip = models.BooleanField(default=False)

    def __str__(self):
        return self.departure


class  Tourguide(models.Model):

    name = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/default.jpg')

    def __str__(self):
        return self.name
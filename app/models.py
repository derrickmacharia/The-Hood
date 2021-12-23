from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import related


# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save_location(self):
        self.save()

    def _str_(self):
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = CloudinaryField('image')
    description = models.CharField(max_length=250)
    mobile_number = models.IntegerField(blank=True)
    email =  models.CharField(max_length=60) 


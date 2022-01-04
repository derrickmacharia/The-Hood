from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import related


# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # save location
    def save_location(self):
        self.save()

    def __str__(self):
        return self.name


class Neighborhood(models.Model):
    hood_image =  CloudinaryField('hood_image', null=True)
    name = models.CharField(max_length=100)
    hood_description = models.TextField(max_length=1000, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def create_neighborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_neighborhood(cls, id):
        cls.objects.filter(id=id).update()
    

    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    # find neighbourhood by id
    @classmethod
    def find_neigborhood(cls, id):
        hood = cls.objects.get(id=id)
        return hood

    def __str__(self):
        return self.name

    

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username =  models.CharField(max_length=100)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=250)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    mobile_number = models.IntegerField(blank=True)
    email =  models.CharField(max_length=60) 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)    


    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def create_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)  
    title = models.CharField(max_length=100)
    post_image = CloudinaryField('post_image', null=True)
    post_description = models.TextField(max_length=1000)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    

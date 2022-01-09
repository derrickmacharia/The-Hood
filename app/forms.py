from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        fields=['first_name', 'last_name', 'profile_pic', 'username', 'bio', 'location', 'mobile_number', 'email']
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        fields=['first_name', 'last_name', 'profile_pic', 'username', 'bio', 'location', 'mobile_number', 'email']

class CreateHoodForm(forms.ModelForm):
    class Meta:
        model=Neighborhood
        fields = ['hood_image','name','hood_description','location']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['title','post_image','post_description','hood', 'category']


class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields = ['name','business_photo','description','location', 'hood']
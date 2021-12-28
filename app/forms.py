from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        fields=['first_name','last_name','profile_pic','bio','mobile_number','email']
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        fields=['profile_pic','bio','mobile_number']


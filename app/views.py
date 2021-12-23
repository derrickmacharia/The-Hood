from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .forms import *
from .models import *
# Create your views here.

def home(request):


    return render(request, 'home.html')



@login_required(login_url='/accounts/login/')
def profile(request,pk):
    
    user = User.objects.get(pk = pk)
    profiles = Profile.objects.filter(user = user).all()
    current_user = request.user
    
    return render(request,'profile.html',{"current_user":current_user, "user":user, "profiles":profiles})
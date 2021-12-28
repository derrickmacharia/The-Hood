from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .forms import *
from .models import *
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile =Profile.objects.get(user=current_user)
        
    except ObjectDoesNotExist:
        return redirect('create_profile')
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    return render(request, 'home.html',{'profiles':profiles,})

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':  
        
        
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect ('index')
        
        else:
            form = ProfileForm()
    return render(request, 'profile_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request,pk):
    current_user = request.user
    user = User.objects.get(pk = pk)
    profiles = Profile.objects.filter(user = user).all()
    prof = Profile.objects.filter(user_id=current_user.id).first()
    
    return render(request,'profile.html',{"current_user":current_user, "user":user, "profiles":profiles, "prof":prof})


@login_required(login_url="/accounts/login/")
def update_profile(request,pk):
    user = User.objects.get(pk = pk)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    ctx = {"form":form}
    return render(request, 'update_profile.html', ctx)

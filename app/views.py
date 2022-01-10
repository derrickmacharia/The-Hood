from django.http.response import HttpResponse, HttpResponseRedirect
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
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    post =  Post.objects.all().order_by('-id')


    return render(request, 'home.html',{'profiles':profiles, 'post':post})

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



@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    profiles = Profile.objects.filter(user_id = current_user.id).all()

    ctx = {"profile": profile, 'profiles':profiles}
    return render(request, "profile.html", ctx)

@login_required(login_url="/accounts/login/")
def update_profile(request,id):
    user = User.objects.get(id=id)
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


@login_required(login_url="/accounts/login/")
def create_hood(request):
    current_user = request.user
    if request.method == 'POST':
        hood_form = CreateHoodForm(request.POST, request.FILES)
        if hood_form.is_valid():

            hood = hood_form.save(commit=False)
            hood.user = current_user
            hood.save()
        
        return HttpResponseRedirect('/')

    else:
        hood_form = CreateHoodForm()


    context = {'hood_form':hood_form}
    return render(request, 'hood/create_hood.html',context)

@login_required(login_url="/accounts/login/")
def hoods(request):
    current_user = request.user
    hood = Neighborhood.objects.all().order_by('-id')
    profiles = Profile.objects.filter(user_id = current_user.id).all()

    context ={'hood':hood, 'profiles':profiles}
    return render(request, 'hood/hood.html', context)


@login_required(login_url="/accounts/login/")
def single_hood(request,name):
    current_user = request.user
    hood = Neighborhood.objects.get(name=name)
    profiles = Profile.objects.filter(neighbourhood=hood)
    post = Post.objects.filter(hood=hood)
    businesses = Business.objects.filter(neighborhood=hood)

    ctx = {"hood":hood, 'profiles':profiles, 'post':post, 'businesses':businesses}
    return render(request, 'hood/single_hood.html', ctx)

def hood_members(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    members = Profile.objects.filter(neighbourhood=hood)
    return render(request, 'members.html', {'members': members})

def join_hood(request, name):
    neighbourhood = get_object_or_404(Neighborhood, name=name)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')

def leave_hood(request, id):
    hood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')


@login_required(login_url="/accounts/login/")
def create_post(request):
    

    current_user = request.user
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():

            post = post_form.save(commit=False)
            post.user = current_user
            post.save()
        
        return HttpResponseRedirect('hood')

    else:
        post_form = PostForm()

    context = {'post_form':post_form}

    return render(request, 'post/create_post.html',context)

@login_required(login_url="/accounts/login/")
def create_business(request):
    current_user = request.user
    if request.method == "POST":
        form=BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business=form.save(commit=False)
            business.user=current_user
            business.hood = hoods
            business.save()
        return HttpResponseRedirect('/businesses')
    else:
        form=BusinessForm()
    return render (request,'business/business_form.html', {'form': form, 'profile': profile})

@login_required(login_url="/accounts/login/")
def businesses(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    businesses = Business.objects.filter(user_id=current_user.id)
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()
        businesses = Business.objects.filter(user_id=current_user.id)
        locations = Location.objects.all()
        neighborhood = Neighborhood.objects.all()
        return render(request, "profile.html", {"danger": "Update Profile", "locations": locations, "neighborhood": neighborhood, "businesses": businesses})
    else:
        neighborhood = profile.neighbourhood
        businesses = Business.objects.filter(user_id=current_user.id)
        return render(request, "business/business.html", {"businesses": businesses})

@login_required(login_url="/accounts/login/")
def search_business(request):
    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_businesses = Business.objects.filter(name__icontains=search_term)
        message = f"Search For: {search_term}"

        return render(request, "search.html", {"message": message, "businesses": searched_businesses})
    else:
        message = "You haven't searched for any term"
        return render(request, "search.html", {"message": message})
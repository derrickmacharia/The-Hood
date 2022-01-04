from django.contrib import admin
from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from app import views

urlpatterns=[
    path('',views.home, name='index'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html')),
    path('create_profile',views.create_profile, name='create_profile'),   
    path('profile/',views.profile,name = 'profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_hood',views.create_hood, name= 'create_hood'),
    path('hood/', views.hood, name = 'hood')
]

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views 
from django.contrib.auth.views import LoginView, logout_then_login, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout'),
]

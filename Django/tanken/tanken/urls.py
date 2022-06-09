"""tanken URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from django.conf import settings

from tankenapp import views

# hier werden pfade angegeben und welche View(.py) verwendet werden soll
# in View.py wird Methode angegegeben, welche ein bestimmtes html template rendert

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home',),    
    path('fare/', views.fare, name= 'fare',),
    path('car/', views.car, name= 'car',),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_User, name="logout"),
    path('login/', views.login_User, name= 'login',),
    path('register/', views.register_User, name='register'),
    path('about_us/', views.about_us, name='about_us'),
    #path('logout/', auth_view.logout_User.as_view(template_name='tankenapp/logout.html'), name="logout"),
    #path('login/', auth_view.login_User.as_view(template_name='tankenapp/login.html'), name="login"),
    
]

from multiprocessing import context
from django.shortcuts import render,redirect

from tankenapp.forms import CustomUserCreationForm 
from .models import geolocation_test, Mycar,User,CarData
from django.conf import settings


#from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# in View.py wird Funktion/ Methode angegegeben, welche ein bestimmtes html template rendert

def index(request):
        return render(request, 'tankenapp/index.html' )

def home(request):
        return render(request, 'tankenapp/home.html' )

def car(request):
        values = {
            "test_variable": "Irgendeine Verlinkung aus Views.py"
        }
        return render(request, 'tankenapp/car.html', context=values )

def about_us(request):
        return render(request, 'tankenapp/about_us.html' )

@login_required()    
def fare(request):
        values = {

            "test_variable": "Irgendeine Verlinkung aus Views.py",
                 }
        return render(request, 'tankenapp/fare.html', context=values )

def login_User(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        #print ('USER', user)
        # print ('USER', password)

        # wenn User existiert, dann einloggen und weiterleiten zu fare/
        if user is not None:
                login(request, user)
                return redirect('fare')

    return render(request, 'tankenapp/login.html')


def logout_User(request):
        logout(request)
        return redirect('login')


def register_User(request):
        form = CustomUserCreationForm()
        context ={'form': form}

        if request.method == 'POST':
                # Custom User Creation form wird aufgerufen per Request 
                form = CustomUserCreationForm(request.POST)

                # wenn keine Fehler in Form, dann neuen User Speichern 
                if form.is_valid():
                        user = form.save(commit=False)
                        user.save()

                #user = authenticate (request, username=user.username, password = request.POST['password1'])

                        if user is not None:
                                login(request, user)
                                return redirect('fare')

        return render(request,'tankenapp/register.html', context)

#@login_required()      vielleicht später einfügen
def profile(request):
        return render(request, 'tankenapp/profile.html')
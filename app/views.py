from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
  return render(request, "index.html")

def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(email=email).exists():
        messages.info(request, 'This email is being used by a user already.')
        return redirect('signup')
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'The username is already taken.')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        #Log user in and redirect to settings page.
        ...

        #Create a profile object for the new user.
        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        return redirect('signup')
    else:
      messages.info(request, 'Password does not match.')
      return redirect('signup')
  else:
    return render(request, "signup.html")
  
def signin(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    ########### TEMPORARY ############
    # if user.is_authenticated:
    #   print(user)
    ##################################
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.info(request, "Input does not match user's information on file. Please try again.")
      redirect('signin')
  return render(request, "signin.html")

def signout(request):
  logout(request)
  messages.success(request, 'You have successfully signed out.')
  return redirect('signin')
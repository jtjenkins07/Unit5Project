from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
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
    pass
  else:
    
  return render(request, "signin.html")
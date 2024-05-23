from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, LikePost

# Create your views here.
@login_required(login_url='signin')
def home(request):
  user_object = User.objects.get(username=request.user.username)
  user_profile = Profile.objects.get(user=user_object)

  posts = Post.objects.all()
  return render(request, "index.html", {"user_profile":user_profile, "posts":posts})

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
        user_login = authenticate(username=username, password=password)
        login(request, user_login)

        #Create a profile object for the new user.
        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        return redirect('settings')
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

@login_required(login_url='signin')
def signout(request):
  logout(request)
  messages.success(request, 'You have successfully signed out.')
  return redirect('signin')

@login_required(login_url='signin')
def settings(request):
  user_profile = Profile.objects.get(user=request.user)

  if request.method == "POST":

    if request.FILES.get('image') == None:
      image = user_profile.profile_img
      bio = request.POST['bio']
      location = request.POST['location']

      user_profile.profile_img = image
      user_profile.bio = bio
      user_profile.location = location
      user_profile.save()
  
    if request.FILES.get('image') != None:
      image = request.FILES.get('image')
      bio = request.POST['bio']
      location = request.POST['location']

      user_profile.profile_img = image
      user_profile.bio = bio
      user_profile.location = location
      user_profile.save()
    
    return redirect('settings')
  return render(request, 'settings.html', {'user_profile': user_profile})

@login_required(login_url='signin')
def upload(request):
  if request.method == "POST":
    user = request.user.username
    image = request.FILES.get('image_upload')
    caption = request.POST['caption']

    new_post = Post.objects.create(user=user, image=image, caption=caption)
    new_post.save()

    return redirect('/')
  else:
    return redirect('/')
  
@login_required(login_url='signin')
def like_post(request):
  username = request.user.username
  post_id = request.GET.get('post_id')

  post = Post.objects.get(id=post_id)

  like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

  if like_filter == None:
    new_like = LikePost.objects.create(post_id=post_id, username=username)
    new_like.save()
    post.no_of_likes = post.no_of_likes+1
    post.save()
    return redirect('/')
  else:
    like_filter.delete()
    post.no_of_likes = post.no_of_likes-1
    post.save()
    return redirect('/')
  
@login_required(login_url='signin')
def profile(request, pk):
  user_object = User.objects.get(username=pk)
  user_profile = Profile.objects.get(user=user_object)
  user_posts = Post.objects.filter(user=pk)
  user_post_length = len(user_posts)

  context = {
    "user_object": user_object,
    "user_profile": user_profile,
    "user_posts": user_posts,
    "user_post_length": user_post_length,
  }
  return render(request, 'profile.html', context)
  
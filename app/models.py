from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
import uuid

User = get_user_model()

# Create your models here.
class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  id_user = models.IntegerField()
  bio = models.TextField(blank=True)
  profile_img = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
  location = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return self.user.username
  
class Post(models.Model):
  # Replaces initial ID created by Django and creates a unique ID.
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  user = models.CharField(max_length=100)
  image = models.ImageField(upload_to='post_images')
  caption = models.TextField()
  create_at = models.DateTimeField(default=datetime.now)
  no_of_likes = models.IntegerField(default = 0)
  user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):
    return self.user
  
class LikePost(models.Model):
  post_id = models.CharField(max_length=500)
  username = models.CharField(max_length=500)

  def __str__(self):
    return self.username
  
class FollowersCount(models.Model):
  follower = models.CharField(max_length=100)
  user = models.CharField(max_length=100)

  def __str__(self):
    return self.user
  
def DeletePost(my_id):
  print("Model:", Post.objects.get(id=my_id))
  Post.objects.get(id=my_id).delete()
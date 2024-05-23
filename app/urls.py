from django.urls import path
from app.views import *

urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup, name="signup"),
    path('signin/', signin, name="signin"),
    path('signout/', signout, name="signout"),
    path('settings/', settings, name="settings"),
    path('upload/', upload, name="upload"),
    path('profile/<str:pk>', profile, name="profile"),
    path('like-post/', like_post, name="like-post"),
]

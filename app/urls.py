from django.urls import path, register_converter
from app.views import *
import uuid

class UUIDConverter:
    regex = '[0-9a-f-]{36}'

    def to_python(self, value):
        return uuid.UUID(value)

    def to_url(self, value):
        return str(value)

register_converter(UUIDConverter, 'uuid')

urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup, name="signup"),
    path('signin/', signin, name="signin"),
    path('signout/', signout, name="signout"),
    path('settings/', settings, name="settings"),
    path('upload/', upload, name="upload"),
    path('follow/', follow, name="follow"),
    path('profile/<str:pk>', profile, name="profile"),
    path('like-post/', like_post, name="like-post"),
    path('search/', search, name="search"),
    path('delete_post/<uuid:post_id>', delete_post, name="delete_post"),
    path('admin-only/', admin_only, name="admin_only"),

]

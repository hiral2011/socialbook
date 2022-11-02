from importlib.resources import path
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('settings', views.Settings, name="settings"),
    path('upload', views.Upload, name="upload"),
    path('signup', views.Signup, name="signup"),
    path('signin', views.Signin, name="signin"),
    path('logout', views.Logout, name="logout"),
]
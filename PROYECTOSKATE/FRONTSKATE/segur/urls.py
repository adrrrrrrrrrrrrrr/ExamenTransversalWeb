from django.urls import path
from . import views

urlpatterns = [
    path('hola', views.hola, name='post_list'),
    path('login', views.login, name='post_list'),
]
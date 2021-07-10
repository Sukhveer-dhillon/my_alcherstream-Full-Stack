from django.contrib import admin
from django.urls import path
#import this( . means current directory)
from . import views

urlpatterns = [
    path('', views.register,name='register'),

]
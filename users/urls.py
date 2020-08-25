'''
Urls for users navigation
'''
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
]

# users urls

from django.urls import path
from .views import MyProfile

urlpatterns = [
    path('', MyProfile, name='my_profile')
]

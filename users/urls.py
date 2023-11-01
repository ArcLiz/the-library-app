# users urls
from . import views
from django.urls import path
from django.views.generic.base import TemplateView
from .views import Profiles, EditProfile, UserSearchView

urlpatterns = [
    path('<slug:pk>', Profiles.as_view(), name='profile'),
    path('edit/<slug:pk>/', EditProfile.as_view(), name='edit_profile'),
    path('search/', views.UserSearchView.as_view(), name='search_users'),
]

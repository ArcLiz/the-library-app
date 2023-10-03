from django.shortcuts import render

# Create your views here.


def MyProfile(request):
    return render(request, 'users/profile.html')

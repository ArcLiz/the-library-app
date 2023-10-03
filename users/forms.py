from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """ Form to create a profile """
    class Meta:
        model = Profile
        fields = ["name", "image", "bio"]

        labels = {
            "name": "Display Name",
            "image": "Profile Picture",
            "bio": "Bio",
        }

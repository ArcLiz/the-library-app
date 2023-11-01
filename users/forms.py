from django import forms
from djrichtextfield.widgets import RichTextWidget

from .models import Profile


class ProfileForm(forms.ModelForm):
    """ Form to create a profile """
    class Meta:
        model = Profile
        fields = ["privacy", "name", "image", "bio",
                  "goodreads", "storygraph", "amazon_wl", "wishlist"]
        privacy = forms.RadioSelect()
        bio = forms.CharField(widget=RichTextWidget())
        wishlist = forms.CharField(widget=RichTextWidget())
        goodreads = forms.URLField(max_length=100)
        storygraph = forms.URLField(max_length=100)
        amazon_wl = forms.URLField(max_length=100)

        widget = {
            "bio": forms.Textarea(attrs={"rows": 5}),
            "wishlist": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "privacy": "Is your profile and library public to other users?",
            "name": "Display Name",
            "image": "Profile Picture",
            "bio": "Bio",
            "goodreads": "Goodreads (url)",
            "storygraph": "Storygraph (url)",
            "amazon_wl": "Amazon Wishlist (url)",
            "wishlist": "Wishlist",
        }


class UserSearchForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search Users...'}),
        label='',
    )

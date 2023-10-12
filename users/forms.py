from django import forms
from djrichtextfield.widgets import RichTextWidget

from .models import Profile


class ProfileForm(forms.ModelForm):
    """ Form to create a profile """
    class Meta:
        model = Profile
        fields = ["name", "image", "bio",
                  "goodreads", "storygraph", "amazon_wl", "wishlist"]

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
            "name": "Display Name",
            "image": "Profile Picture",
            "bio": "Bio",
            "goodreads": "Goodreads (url)",
            "storygraph": "Storygraph (url)",
            "amazon_wl": "Amazon Wishlist (url)",
            "wishlist": "Wishlist",
        }
from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField
from django.db.models.signals import post_save
from django.dispatch import receiver

from djrichtextfield.models import RichTextField


class Profile(models.Model):
    """ User Profile """
    user = models.ForeignKey(
        User, related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = ResizedImageField(
        size=[300, 300], quality=75, upload_to="profiles/", force_format="WEBP", blank=False)
    bio = RichTextField(max_length=1000, null=True, blank=True)
    goodreads = models.URLField(max_length=200, blank=True, null=True)
    storygraph = models.URLField(max_length=200, blank=True, null=True)
    amazon_wl = models.URLField(max_length=200, blank=True, null=True)
    wishlist = RichTextField(max_length=2000, null=True, blank=True)

    # Privacy Settings
    privacy = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """ Create or update user profiles """
    if created:
        Profile.objects.create(user=instance)

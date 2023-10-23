from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import redirect

from .models import Profile
from .forms import ProfileForm

# Create your views here.


class Profiles(TemplateView):
    """ User Profile View """
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        context = {
            'profile': profile,
            'form': ProfileForm(instance=profile),
        }

        return context


class EditProfile(UpdateView):
    """ Edit a profile"""
    form_class = ProfileForm
    model = Profile

    def form_valid(self, form):
        self.success_url = f'/users/{self.kwargs["pk"]}'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


def profile_redirect(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        profile_url = reverse('profile', args=[user_id])
        return redirect(profile_url)

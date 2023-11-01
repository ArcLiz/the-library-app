from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm, UserSearchForm

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


class UserSearchView(TemplateView):
    template_name = 'users/search_users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = UserSearchForm()

        # Handle GET request for searching users
        if self.request.method == 'GET':
            # Use 'username' instead of 'name'
            username = self.request.GET.get('username')
            if username:
                results = User.objects.filter(username__icontains=username)
                context['results'] = results

        context['form'] = form  # Add the form to the context
        return context

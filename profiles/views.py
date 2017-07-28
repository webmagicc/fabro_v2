from django.shortcuts import render
from .models import User
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.views.generic import DetailView





class ProfileView(DetailView):
    model = get_user_model()
    context_object_name = 'user_object'
    template_name = 'profiles/profile.html'
    def get_object(self):
        pass







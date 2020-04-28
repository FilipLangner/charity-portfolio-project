from django.shortcuts import render
from django.views import generic


class LandingPageView(generic.TemplateView):
    template_name = "good_hands/index.html"

class LoginView(generic.TemplateView):
    template_name = "good_hands/login.html"

class RegisterView(generic.TemplateView):
    template_name = "good_hands/register.html"

class MakeDonationView(generic.TemplateView):
    template_name = "good_hands/form.html"
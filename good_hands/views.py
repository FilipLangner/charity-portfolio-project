from django.shortcuts import render
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views import generic

from good_hands.models import Institution, Donation
from good_hands.forms import MyRegistrationForm


class LandingPageView(generic.TemplateView):
    template_name = "good_hands/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['institutions_donated_to'] = Donation.objects.order_by('institution').distinct('institution').count()
        context['donation_qty'] = Donation.objects.all().aggregate(Sum('quantity'))
        context['intitutions_foundations'] = Institution.objects.filter(type='FU')
        context['intitutions_ngo'] = Institution.objects.filter(type='OP')
        context['intitutions_local'] = Institution.objects.filter(type='ZL')
        return context

# class LoginView(generic.TemplateView):
#     template_name = "good_hands/templates/registration/login.html"

class RegisterView(generic.CreateView):
    form_class = MyRegistrationForm
    template_name = "good_hands/register.html"
    success_url = reverse_lazy('login')

class MakeDonationView(generic.TemplateView):
    template_name = "good_hands/form.html"
from django.shortcuts import render
from django.db.models import Sum
from django.views import generic

from good_hands.models import Institution, Donation


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

class LoginView(generic.TemplateView):
    template_name = "good_hands/login.html"

class RegisterView(generic.TemplateView):
    template_name = "good_hands/register.html"

class MakeDonationView(generic.TemplateView):
    template_name = "good_hands/form.html"
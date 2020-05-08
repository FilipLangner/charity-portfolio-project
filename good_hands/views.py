from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from good_hands.models import Institution, Donation, Category
from good_hands.forms import MyRegistrationForm, DonationForm, DonationIsTakenForm

import json


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


class RegisterView(generic.CreateView):
    form_class = MyRegistrationForm
    template_name = "good_hands/register.html"
    success_url = reverse_lazy('login')


class MakeDonationView(LoginRequiredMixin, generic.FormView):
    template_name = "good_hands/form.html"
    form_class = DonationForm
    success_url = reverse_lazy('form_confirmation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['institutions'] = Institution.objects.all()
        return context

    def form_valid(self, form):
        quantity = form.cleaned_data['quantity']
        institution = form.cleaned_data['institution']
        address = form.cleaned_data['address']
        phone_number = form.cleaned_data['phone_number']
        city = form.cleaned_data['city']
        zip_code = form.cleaned_data['zip_code']
        pick_up_date = form.cleaned_data['pick_up_date']
        pick_up_time = form.cleaned_data['pick_up_time']
        pick_up_comment = form.cleaned_data['pick_up_comment']
        user = self.request.user
        categories = form.cleaned_data['categories']
        donation = Donation.objects.create(
            quantity=quantity,
            institution=institution,
            address=address,
            phone_number=phone_number,
            city=city,
            zip_code=zip_code,
            pick_up_date=pick_up_date,
            pick_up_time=pick_up_time,
            pick_up_comment=pick_up_comment,
            user=user
        )
        # do a loop for categories
        for category in categories:
            donation.categories.add(category)

        return super().form_valid(form)


class FormConfirmationView(generic.TemplateView):
    template_name = 'good_hands/form-confirmation.html'


class UserDetailView(generic.TemplateView):
    template_name = 'good_hands/user-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['donations'] = Donation.objects.filter(user=self.request.user).order_by(
            'is_taken',
            'pick_up_date'
        )
        return context


class DonationIsTakenView(generic.UpdateView):
    form_class = DonationIsTakenForm
    template_name = "good_hands/donation_is_taken.html"
    success_url = reverse_lazy('user_detail')
    # initial = {'is_taken': True}

    def get_object(self, queryset=None):
        return get_object_or_404(Donation, id=self.kwargs.get('donation_id'))

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from good_hands.models import Institution, Donation, Category
from good_hands.forms import MyRegistrationForm, DonationForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['institutions'] = Institution.objects.all()
        return context

def get_institution(request):
    category_id = request.GET.get('category_id')
    if category_id:
        # Only works if one category is selected TODO:change to accomodate multiple categories
        institutions = Institution.objects.filter(categories=Category.objects.get(pk=category_id))
    else:
        institutions = Institution.objects.all()

    return HttpResponse(create_json(institutions))


def create_json(institution):
    inst_lst = []
    for item in institution:
        inst_lst.append({'id': item.id, 'type': item.type, 'name': item.name, 'description': item.description})
    return json.dumps({'institution': inst_lst})
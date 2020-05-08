from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


from good_hands.models import Donation

User = get_user_model()

class MyRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=True)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ['user']


class DonationIsTakenForm(forms.ModelForm):
    is_taken = forms.BooleanField(label='Dar odebrany:', required=False)
    class Meta:
        model = Donation
        fields = ['is_taken']




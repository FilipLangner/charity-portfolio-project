"""Portfolio_Lab_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from good_hands import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('make_donation/', views.MakeDonationView.as_view(), name="make_donation"),
    path('form_confirmation/', views.FormConfirmationView.as_view(), name="form_confirmation"),
    path('user_detail/', views.UserDetailView.as_view(), name='user_detail'),
    path('donation_taken/<int:donation_id>/', views.DonationIsTakenView.as_view(), name='donation_taken'),
]

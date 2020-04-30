from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=128)


class Institution(models.Model):
    FUNDACJA = 'FU'
    ORGANIZACJA_POZARZADOWA = 'OP'
    ZBIORKA_LOKALNA = 'ZL'
    TYPE_CHOICES = [
        (FUNDACJA, 'fundacja'),
        (ORGANIZACJA_POZARZADOWA, 'organizacja pozarządowa'),
        (ZBIORKA_LOKALNA, 'zbiórka lokalna')
    ]

    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=FUNDACJA)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=32)
    pick_up_date = models.CharField(max_length=32)
    pick_up_time = models.CharField(max_length=32)
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

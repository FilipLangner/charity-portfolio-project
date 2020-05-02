from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Donation, Institution, Category

admin.site.register(User, UserAdmin)
admin.site.register(Donation)
admin.site.register(Institution)
admin.site.register(Category)
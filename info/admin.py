from django.contrib import admin
from .models import Phone
from django.db import models
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from phonenumber_field.modelfields import PhoneNumberField

# Register your models here.

class PhoneAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PhoneNumberField: {'widget': PhoneNumberInternationalFallbackWidget},
    }

admin.site.register(Phone,PhoneAdmin)


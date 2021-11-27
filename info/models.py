from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Phone(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100, unique=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name








from django.shortcuts import render
from .models import Phone

# Create your views here.

def phonenumber(request,phone_num):
    try:
        p_number = Phone.objects.get(phone_number=phone_num)
    except Phone.DoesNotExist:
        p_number = None
    return render(request, 'phonenum.html', {'phone_number': p_number})

def person_name(request,n_name):
    try:
        p_name = Phone.objects.get(name=n_name)
    except Phone.DoesNotExist:
        p_name = None
    return render(request, 'name.html', {'pers_name': p_name})


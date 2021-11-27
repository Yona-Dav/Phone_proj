from django.shortcuts import render, redirect
from .models import Phone
from .forms import PhoneForm

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

def search_form(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get('email')
            if len(name) != 0:
                return redirect('name', name)
            elif len(phone_number)!=0:
                return redirect('phone', phone_number)
            else:
                return redirect('email', email)
    else:
        form = PhoneForm()
    return render(request, 'search.html',{'form':form})

def person_email(request,e_email):
    try:
        p_email = Phone.objects.get(email=e_email)
    except Phone.DoesNotExist:
        p_email = None
    return render(request, 'email.html', {'pers_email': p_email})
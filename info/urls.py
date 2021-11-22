from django.urls import path
from . import views

urlpatterns = [
    path('name/<slug:n_name>/', views.person_name),
    path('phone/<slug:phone_num>/', views.phonenumber),
]
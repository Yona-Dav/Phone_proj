from django.urls import path
from . import views

urlpatterns = [
    path('name/<slug:n_name>/', views.person_name, name='name'),
    path('email/<str:e_email>/', views.person_email, name='email'),
    path('phone/<slug:phone_num>/', views.phonenumber, name='phone'),
    path('search/', views.search_form, name='search'),

]
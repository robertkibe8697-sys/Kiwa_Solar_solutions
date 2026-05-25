from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('contact/', views.contact_page, name='contact'),

    path('api/contact/', views.contact, name='api_contact'),
]
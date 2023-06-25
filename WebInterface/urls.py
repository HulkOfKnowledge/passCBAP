from . import views
from django.urls import path
from FormsInterface.views import sign_in 



urlpatterns = [
    path('',views.home,name='index'),
    path('home/',views.home,name='home'),
    path('contact/', views.contact, name='contact'),
    path('register/sign-in',sign_in,name='sign-in')
]


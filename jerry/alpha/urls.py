from xml.etree.ElementInclude import include
from django.urls import path
from alpha import views

urlpatterns = [
    path('',views.landingPage,name='Landing page'),
    path('signup',views.signup , name='SignUp page')
]

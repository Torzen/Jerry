from xml.etree.ElementInclude import include
from django.urls import path
from alpha import views

urlpatterns = [
    path('',views.main,name='Landing page'),
    path('user-signup',views.user_signup , name='SignUp page')
]

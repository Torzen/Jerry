from django.urls import path
from alpha import views




def url_patterns():


    userRegistration = [
           path('userApproval',views.approveUser,name="User approval"),
           path('registrationKeyApproval',views.keyApproval,name = "Key approval" )
    ]
    
    urlpatterns = [
        path('',views.main,name='Landing page'),
        path('user_signup',views.user_signup , name='SignUp page')
    ]

    urlpatterns+=userRegistration                                       #   FOR  USER REGISTRATIONS

    return urlpatterns



urlpatterns = url_patterns()
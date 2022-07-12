from alpha import views
from django.urls import path


urlpatterns = [

    path('',views.main,name='Main page'),
    path('about',views.about , name="About page"),
    path('contact',views.contact,name='contact page'),
    path('register',views.register,name='Staff registration'),
    path('patners',views.patners ,name="patner page"),
    path('alumuni',views.alumuni,name="Alumini page"),
    path('help',views.help , name = "help page"),
    path('complain',views.complain,name="Complain page"),
    path('feedback',views.feedback,name = "feedback page"),
    path('plans',views.plans,name = "plans and visions"),
    path('team',views.team,name = "team page")
]

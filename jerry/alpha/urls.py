from alpha import views
from django.urls import path

parentUrl = ""
urlpatterns = [

    path(f'{parentUrl}',views.main,name='Main page'),
    # path(f'{parentUrl}/about',views.about , name="About page"),
    path(f'{parentUrl}contact',views.contact,name='contact page'),
    path(f'{parentUrl}register',views.register,name='Staff registration'),
    # path(f'{parentUrl}/patners',views.patners ,name="patner page"),
    # path(f'{parentUrl}/alumuni',views.alumuni,name="Alumini page"),
    # path(f'{parentUrl}/help',views.help , name = "help page"),
    # path(f'{parentUrl}/complain',views.complain,name="Complain page"),
    # path(f'{parentUrl}/feedback',views.feedback,name = "feedback page"),
    # path(f'{parentUrl}/plans',views.plans,name = "plans and visions"),
    # path(f'{parentUrl}/team',views.team,name = "team page")
]

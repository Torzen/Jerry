from django.urls import path
from store import views

parenturl = "store"
urlpatterns = [
    path(f'{parenturl}',views.main,name = "main"),
    path(f'{parenturl}/track',views.track,name="tracker")
]

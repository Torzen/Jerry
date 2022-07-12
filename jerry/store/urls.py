from django.urls import path
from store import views

urlpatterns = [
    path('',views.main,name = "main"),
    path('track',views.track,name="tracker")
]

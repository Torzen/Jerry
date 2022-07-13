from django.urls import path
from . import views
    

urlpatterns = [
    path('',views.main ,name=''),
    path('staffs',views.staffs ,name='staffs'),
    path('costumers',views.costumers ,name='costumers'),
    path('services',views.services ,name='services'),
    path('delete',views.delete ,name='delete'),
    path('add',views.add ,name='add'),
    path('crm',views.crm ,name='crm'),
    path('ratings',views.ratings ,name='ratings'),
    path('complainBox',views.complainBox,name = 'complainBox'),
    path('registrationApproval',views.registrationApproval ,name='registrationApproval'),
    path('feedbacks',views.feedbacks,name = "feedbacks"),
    path('contact',views.contact,name = "Contact"),
    path('datasets',views.datasets,name = "Dataset page"),
    path('tools',views.tools,name ="Tools page" ),
    path('services',views.services,name ="services page" ),
    path('reports',views.reports,name ="reports page" ),
    path('login',views.login,name="Login page") 
]

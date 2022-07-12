from django.urls import path
from management import views


urlpatterns = [
    path('',views.main ,name=''),
    path('/staffs',views.staffs ,name='staffs'),
    path('/contumers',views.contumers ,name='contumers'),
    path('/services',views.services ,name='services'),
    path('/delete',views.delete ,name='delete'),
    path('/add',views.add ,name='add'),
    path('/crm',views.crm ,name='crm'),
    path('/ratings',views.ratings ,name='ratings'),
    path('/complainBox',views.complainBox,name = 'complainBox'),
    path('/registrationApproval',views.registrationApproval ,name='registrationApproval'),
    path('/feedbacks',views.feedbacks,name = "feedbacks"),
    path('/contact',views.contact,name = "Contact")
]

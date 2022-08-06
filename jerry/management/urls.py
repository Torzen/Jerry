from django.urls import path
from management import views
    
parentUrl = "management"
urlpatterns = [
    path(f'{parentUrl}/main',views.main ,name=''),
    # path(f'{parentUrl}/staffs',views.staffs ,name='staffs'),
    # path(f'{parentUrl}/costumers',views.costumers ,name='costumers'),
    # path(f'{parentUrl}/services',views.services ,name='services'),
    # path(f'{parentUrl}/delete',views.delete ,name='delete'),
    path(f'{parentUrl}/add',views.add ,name='add'),
    # path(f'{parentUrl}/crm',views.crm ,name='crm'),
    # path(f'{parentUrl}/ratings',views.ratings ,name='ratings'),
    path(f'{parentUrl}/complainBox',views.complainBox,name = 'complainBox'),
    path(f'{parentUrl}/registrationApproval',views.registrationApproval ,name='registrationApproval'),
    # path(f'{parentUrl}/feedbacks',views.feedbacks,name = "feedbacks"),
    path(f'{parentUrl}/contact',views.contact,name = "Contact"),
    # path(f'{parentUrl}/datasets',views.datasets,name = "Dataset page"),
    path(f'{parentUrl}/tools',views.tools,name ="Tools page" ),
    # path(f'{parentUrl}/services',views.services,name ="services page" ),
    path(f'{parentUrl}/reports',views.reports,name ="reports page" ),
    path(f'{parentUrl}/',views.login,name="Login page") ,
    # path(f'{parentUrl}/forgetPassword',views.forgetPassword,name = "Forget password")
    path(f'{parentUrl}/approve',views.approve,name='aproval page'),
    path(f'{parentUrl}/registration/disapprove',views.disapprove,name='disaproval page'),
    path(f'{parentUrl}/registration/seemore',views.seemore,name="See more")


]
    
# Developer notebook

* 1st stage Urls patterns
` 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('/services',include('store.urls')),
    path('/management',include('management.urls')),
    path('',include('alpha.urls'))
]

`

**Second stage url pattern
    // alpha application

    $$ mean for first priority
urlpatterns = [
    path('',views.main,name='Main page'),$$
    path('/about',views.about , name="About page"),$$
    path('/contact',views.contact,name='contact page'),$$
    path('/register',views.register,name='Staff registration'),$$
    path('/patners',views.patners ,name="patner page"),
    path('/alumuni',views.alumuni,name="Alumini page"),
    path('/help',views.help , name = "help page"),
    path('/complain',views.complain,name="Complain page"),
    path('/feedback',views.feedback,name = "feedback page"),
    path('/plans',views.plans,name = "plans and visions")
    path('/team',views.team,name = "team page")$$
]


//management application

urlpatterns = [
    path('',views.main ,name=''),$$
    path('/staffs',views.staffs ,name='staffs'),$$
    path('/contumers',views.contumers ,name='contumers'),
    path('/services',views.services ,name='services'),$$
    path('/delete',views.delete ,name='delete'),
    path('/add',views.add ,name='add'),
    path('/crm',views.crm ,name='crm'),
    path('/ratings',views.ratings ,name='ratings'),
    path('/complainBox',views.complainBox,name = 'complainBox'),
    path('/registrationApproval',views.registrationApproval ,name='registrationApproval'),$$
    path('/feedbacks',views.feedbacks,name = "feedbacks"),
    path('/contact',views.contact,name = "Contact")$$
]

//store
urlpatterns = [
    path('',views.main,name = "main"),
    path('/track',views.track,name="tracker")
]






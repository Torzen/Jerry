from django.http import HttpResponse
from django.shortcuts import render
from alpha.models import staffRegistration
# Create your views here.
def main(request):
    return HttpResponse("main")
def about(request):
    return HttpResponse("about")
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        a = (f"name:{name},subject:{subject},email:{email},desc:{desc}")
        return HttpResponse(a)
    else:
        return render(request,'contact.html')
    # return HttpResponse("contact")
def  register(request):
    if request.method  == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        fullname= request.POST.get('fullname')
        email= request.POST.get('email')
        address= request.POST.get('address')
        number= request.POST.get('number')
        nationality= request.POST.get('nationality')
        photoUrl= request.POST.get('photoUrl')
        user = staffRegistration(username = username,password = password , fullname = fullname , email = email , address = address , number = number , nationality = nationality , photoUrl = photoUrl)
        user.save()
    return render(request , 'register.html')
   
def alumuni(request):
    return HttpResponse("alumuni")
def patners(request):
    return HttpResponse("patners")
def help(request):
    return HttpResponse("help")
def complain(request):
    return HttpResponse("complain")
def feedback(request):
    return HttpResponse("feedback")
def plans(request):
    return HttpResponse("plans")
def team(request):
    return HttpResponse("team")
def approve(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        staff_detail_record = staffRegistration.objects.get().filter(id = id)
        for i in staff_detail_record:
            print(i)
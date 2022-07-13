from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def main(request):
    return render(request,'managementMain.html')

def staffs(request):
    return HttpResponse("staffs")
def costumers(request):
    return HttpResponse("costumers")
def services(request):
    return HttpResponse("services")
def delete(request):
    return HttpResponse("delete")
def add(request):
    return HttpResponse("add")
def crm(request):
    return HttpResponse("crm")
def ratings(request):
    return HttpResponse("ratings")
def complainBox(request):
    return HttpResponse("complainBox")
def registrationApproval(request):
    return HttpResponse("registrationApproval")
def feedbacks(request):
    return HttpResponse("feedbacks")
def contact(request):
    return HttpResponse("Contact")
def datasets(request):
    return render(request,'dataset.html')
def services(request):
    return render(request,'services.html')
def tools(request):
    return render(request,'tools.html')
def reports(request):
    return render(request,'reports.html')


def login(request):
    if request == "POST":
        pass
    else:
        return render(request , 'login' )
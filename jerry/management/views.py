from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main(request):
    return HttpResponse("main")
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
def rating(request):
    return HttpResponse("rating")
def rating(request):
    return HttpResponse("rating")
def complainBox(request):
    return HttpResponse("complainBox")
def registrationApproval(request):
    return HttpResponse("registrationApproval")
def feedbacks(request):
    return HttpResponse("feedbacks")
def contact(request):
    return HttpResponse("Contact")
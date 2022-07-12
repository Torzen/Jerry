from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main(request):
    return HttpResponse("main")
def about(request):
    return HttpResponse("about")
def contact(request):
    return HttpResponse("contact")
def  register(request):
    return HttpResponse("register")
def alumini(request):
    return HttpResponse("alumini")
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

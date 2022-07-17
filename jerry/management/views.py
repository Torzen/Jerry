from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import *
from django.contrib import messages

# Create your views here.
def main(request):
    if userAuthenticated ==True:
        return 
    # return render(request,'managementMain.html')
    else:
        return HttpResponse('you arent authenticated')

# def staffs(request):
#     return HttpResponse("staffs")

# def costumers(request):
#     return HttpResponse("costumers")
# def services(request):
#     return HttpResponse("services")
# def delete(request):
#     return HttpResponse("delete")
def add(request):
    return HttpResponse("add")
# def crm(request):
#     return HttpResponse("crm")
# def ratings(request):
#     return HttpResponse("ratings")
def complainBox(request):
    return render(request , 'tools.html')
def registrationApproval(request):
    return HttpResponse("registrationApproval")
# def feedbacks(request):
#     return HttpResponse("feedbacks")
def contact(request):
    return render(request,'services/contact.html')
# def datasets(request):
#     return render(request,'dataset.html')
# def services(request):
#     return render(request,'services.html')
def tools(request):
    return render(request,'tools.html')
def reports(request):
    return render(request,'reports.html')


def login(request):
    if request == "POST":
        userName = request.POST.get('username')
        password = request.POST.get('password')
        if (userAuthenticated(request,userName,password)) == True:
            redirect('management/main',userAuthenticated = True)
def forgetPassword(request):
    return render(request,'forgetPassword.html')





# utilities
def userAuthenticated(request , username = "default",password = "default"):

        user = authenticate(username = username, password = password)
        if user == 'authenticated':
            return True
        # main(request,user = user)
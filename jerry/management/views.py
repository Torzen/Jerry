from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate 
from django.contrib import messages



# Create your views here.
def main(request,userAuthenticated = True):
    return render(request , 'managementMain.html')



def add(request):
    return HttpResponse("add")
def complainBox(request):
    return render(request , 'tools.html')
def registrationApproval(request):
    return HttpResponse("registrationApproval")
def contact(request):
    return render(request,'services/contact.html')
def tools(request):
    return render(request,'tools.html')
def reports(request):
    return render(request,'reports.html')


def login(request):
    if request.method == "POST":
        userName = request.POST.get('username')
        passWord = request.POST.get('password')
        if isUserAuthenticated(userName , passWord) == True:
            print('Authentication working ')
        else:
            print('authentication not working')
        return render(request , 'login.html')

    else:
        # print('failed authentication')

        return render(request , 'login.html')



def forgetPassword(request):
    return render(request,'forgetPassword.html')









def isUserAuthenticated(username,password):
        user = authenticate(username = username, password = password)
        if user is not None:
            return True



# def staffs(request):
#     return HttpResponse("staffs")

# def costumers(request):
#     return HttpResponse("costumers")
# def services(request):
#     return HttpResponse("services")
# def delete(request):
#     return HttpResponse("delete")
# def crm(request):
#     return HttpResponse("crm")
# def ratings(request):
#     return HttpResponse("ratings")
# def datasets(request):
#     return render(request,'dataset.html')
# def services(request):
#     return render(request,'services.html')
# def feedbacks(request):
#     return HttpResponse("feedbacks")

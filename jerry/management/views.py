from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate 
from django.contrib import messages
from utilities.mailSystem import Mymail

from alpha.models import staffRegistration
from management.models import staffs,staffs_detail

# Create your views here.
def main(request,userAuthenticated = True):
    return render(request , 'managementMain.html')



def add(request):
    return HttpResponse("add")
def complainBox(request):
    return render(request , 'tools.html')
def registrationApproval(request):
    registrationRequests = staffRegistration.objects.all()
    data = {'requests':registrationRequests}
    return render(request,'services/registrationApproval.html',data)
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


def approve(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        reg_data = staffRegistration.objects.filter(id = id)
        for i in reg_data:
            print(i)
            stf = staffs(username = i.username , password = i.password)
            stf_dtl = staffs_detail(fullname = i.fullname , email = i.email , address = i.email , 
                number = i.number , nationality = i.nationality , photoUrl = i.photoUrl)
            stf.save()
            stf_dtl.save()
            print(stf)
            print(stf_dtl)
        staffRegistration.objects.filter(id = id).delete()      
        return HttpResponse("Approved  \n <a href='http://localhost:8000/management/registrationApproval'> Go back </a>")
    return HttpResponse('not approved')


def seemore(request):                                                   #op[1] mean 
    if request.method == 'GET':
        id = request.GET.get('id')
        data = staffRegistration.objects.filter(id = id)
        
        for i  in data:
            dataRecord = i
            break
        data = {
            'dataRecord':dataRecord
        }
        return render(request,'services/seemore.html',data)
    else:
        return HttpResponse('Not a contexed request')

    
def disapprove(request):
    if request.method == 'POST':                    
        id = request.POST.get('id')                                   # key of record to be dissaproved
        message = request.POST.get('message')                        #getting message of dissaproval
        records = staffRegistration.objects.filter(id = id)
        print(id , message)
        print(records)
        for i in records:                                             #extracting list from list of list
            rec = i
        print(rec)
        mailAddr = rec.email
        records.delete()                                            #deleting the record after been disapproved
        Mymail.disappoval_message(mailAddr , id ,message)              #sasta bantai mail sytem
        print(f'the registration of id:{id} is disapproved')
        return HttpResponse('Registration request disapproved')
    else:
        return 'Forbidden request'


    
from django.shortcuts import render,HttpResponse,redirect
from hashlib import sha256
from utilities import encription,randoms
from alpha.model import userRegistrations

# Create your views here.
def main(request):
    return HttpResponse( 'Main page')


def user_signup(request):
    if request.method == "POST":
        formData = {
            'username' :  request.POST.get('name'),
            'email' : request.POST.get('email'),
            'hashedPassword' : encription.encript(request.POST.get('password'))
        }
        mdl = userRegistrations(username = formData['username'], email = formData['email'], password = formData['hashedPassword'])
        mdl.save()
        approveUser(request,formData= formData)

    return render(request,'signup.html')


def approveUser(request , formData):
    
    data = dict()
    data.update(formData)

    return render(request ,'userApproval.html',formData)
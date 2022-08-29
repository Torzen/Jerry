from django.shortcuts import render,HttpResponse
from hashlib import sha256
from utilities import encription
from alpha.model import userRegistrations

# Create your views here.
def main(request):
    return HttpResponse( 'Main page')


def user_signup(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email  = request.POST.get('email')
        password = request.POST.get('password')
        hashedPassword = encription.encript(password)
        mdl = userRegistrations(username = username , email = email , password = hashedPassword)
        mdl.save()
    return render(request,'signup.html')
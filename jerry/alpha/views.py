from django.shortcuts import render,HttpResponse,redirect
from hashlib import sha256
from utilities import  mail ,randoms ,encription
from alpha.model import userRegistrations, myusers

userApprovalCode = int()
# Create your views here.
def main(request):
    return render(request,"index.html")


def user_signup(request):
    if request.method == "POST":

        formData = {
            'username' :  request.POST.get('name'),
            'email' : request.POST.get('email'),
            'hashedPassword' : encription.encript(request.POST.get('password')),
            'approvalkey' : randoms.userApprovalRandom()
        }
        mdl = userRegistrations(username = formData['username'], email = formData['email'], password = formData['hashedPassword'],approvalKey = formData['approvalkey'])
        mdl.save()
        approveUser(request,formData= formData)
        return render(request,'userApproval.html',formData)
        
    else:
        return render(request,'user_signup.html')


def approveUser(request , formData):
    uAC = formData['approvalkey']                           #MESSAGE_MAIL_SYSTEM
    mailmessage = f"\n {uAC}"
    print(f"message:'{mailmessage}'")
    data = formData
    data.update({'uac':uAC})
    approvalMail = mail.Mail(formData['email'],'userRegistration' ,mailmessage)
    print(approvalMail.userRegistration())

def keyApproval(request):
    if request.method == 'POST':
        emailaddr = request.POST.get('email')
        code = request.POST.get('code')
        cursor = userRegistrations.objects.filter(email = emailaddr)
        for i in cursor:
            if(int(code) == i.approvalKey):
                try:
                    a = myusers(username = i.username , email = i.email , password  = i.password)
                    a.save()
                    return HttpResponse('Sucessfull\n <a href = "userlogin">login</a>')
                except TypeError:
                    return HttpResponse("Type Error")
                # except:
                #     return HttpResponse('Eror')
                break
            else:
                return HttpResponse('Error')



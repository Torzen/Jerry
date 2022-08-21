from django import forms
class signUpForm(forms.Form):
    Username = forms.CharField(max_length=50)
    mailAddr = forms.EmailField()
    password = forms.PasswordInput()
    
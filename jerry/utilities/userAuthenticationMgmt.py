from django.contrib.auth import authenticate

def isUserAuthenticated(request , username,password):
        user = authenticate(username = username, password = password)
        if user is not None:
            return True
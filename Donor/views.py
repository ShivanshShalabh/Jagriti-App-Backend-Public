from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from Accounts.models import App_User
# Create your views here.


def user_authentication(request, file):
    if not request.user.is_authenticated:
        return ("/accounts/login")
    else:
        email = (request.user.email)
        user = App_User.objects.get(email=email)
        user_type = user.user_type
        if user_type == 'donor':
            return file
        else:
            return ('/')


def donate(request):
    file = 'Donor/donate.html'
    if user_authentication(request, file) == file:
        return render(request, file)
    else:

        return redirect(user_authentication(request, file))

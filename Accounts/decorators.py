from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return func(request, *args, **kwargs)
    return wrapper


def authenticated_user(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        else:
            return func(request, *args, **kwargs)
    return wrapper

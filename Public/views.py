from Accounts.models import App_User
from django.shortcuts import render

# Create your views here.


def render_req(request):
    if not request.user.is_authenticated:
        return -1
    else:
        email = (request.user.email)
        user = App_User.objects.get(email=email)
        user_type = user.user_type
        if user_type == 'Donor':
            return True
        return False


def home(request):
    # print("'"+str(request.user.groups.all()[0].name)+"'")
    if(render_req(request) == -1):
        return render(request, 'home.html')
    else:
        return render(request, 'home.html', {'user_type_bool': render_req(request)})


def base(request):
    return render(request, 'template.html')


def about(request):
    return render(request, 'Public/about_us.html')


def jagrukta(request):
    return render(request, 'Public/jagrukta_zone.html')


def volunteer(request):
    return render(request, 'Public/volunteer.html')

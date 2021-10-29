import django.contrib.messages as messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .models import App_User
from django.contrib.auth.models import User
from .decorators import *
# Create your views here.
# List of states
states = ['Andhra Pradesh',
          'Arunachal Pradesh',
          'Assam',
          'Bihar',
          'Chhattisgarh',
          'Goa',
          'Gujarat',
          'Haryana',
          'Himachal Pradesh',
          'Jharkhand',
          'Karnataka',
          'Kerala',
          'Madhya Pradesh',
          'Maharashtra',
          'Manipur',
          'Meghalaya',
          'Mizoram',
          'Nagaland',
          'Odisha',
          'Punjab',
          'Rajasthan',
          'Sikkim',
          'Tamil Nadu',
          'Telangana',
          'Tripura',
          'Uttarakhand',
          'Uttar Pradesh',
          'West Bengal',
          'Andaman and Nicobar Islands',
          'Chandigarh',
          'Dadra and Nagar Haveli and Daman & Diu',
          'The Government of NCT of Delhi',
          'Jammu & Kashmir',
          'Ladakh',
          'Lakshadweep',
          'Puducherry']

states.sort()

# Function to check if the name is already taken and return a uniqe name


def name_assign(name):
    num = 1
    if(not (User.objects.filter(username=name).exists())):
        return name
    while((User.objects.filter(username=f'{name}_{num}').exists())):
        num += 1
    return f'{name}@{num}'

# Function to signup a new user


@unauthenticated_user
def signup_request(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = str(request.POST['user_email']).lower()
        mobile = str(request.POST['user_mobile']).replace(" ", "")
        address1 = request.POST['user_address_1']
        address2 = request.POST['user_address_2']
        city = request.POST['user_city']
        state = request.POST['user_state']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        user_type = request.POST['user_type']
        first_name.replace(" ", "")
        last_name.replace(" ", "")
        # Check if passwords match
        check_num_ok = True
        if not (mobile.replace("+", "").isdigit() and len(mobile.replace("+", "")) == 12):
            messages.error(request, 'Invalid Mobile Number')
            check_num_ok = False

        if (pass1 == pass2):
            # Check if the email is already taken
            if App_User.objects.filter(email=email).exists():
                messages.error(request,
                               "The email id you entered is already registered with us.")
                # Check if the mobile number is already taken
                if App_User.objects.filter(mobile=mobile).exists():
                    messages.error(request,
                                   "The mobile number you entered is already registered with us.")
            else:
                # Check if the mobile number is already taken
                if App_User.objects.filter(mobile=mobile).exists():
                    messages.error(request,
                                   "The mobile number you entered is already registered with us.")
                # Save the user data in the database
                elif user_type in ['donor', 'donee'] and check_num_ok:
                    custom_user = App_User(first_name=first_name, last_name=last_name, email=email, mobile=mobile, address1=address1,
                                           address2=address2, city=city, state=state, password=pass1, user_type=user_type)
                    custom_user.save()
                    name = f'{first_name}_{last_name}'.lower()
                    name = name_assign(name)
                    user = User.objects.create_user(name, email, pass1)
                    user.first_name = first_name
                    user.last_name = last_name
                    if user_type == 'donee':
                        group = Group.objects.get(name='Donee')
                        group.user_set.add(user)
                    user.save()
                    user = authenticate(
                        request, username=name, password=pass1)
                    auth_login(request, user)
                    return redirect('/')
        # If passwords don't match, re-render the signup form after checking if the email is already taken and the mobile number is already taken
        else:
            # Error message if passwords don't match
            messages.error(request,
                           "Both of the passwords didn't match.")
            if App_User.objects.filter(email=email).exists():
                messages.error(request,
                               "The email id you entered is already registered with us.")
            if App_User.objects.filter(mobile=mobile).exists():
                messages.error(request,
                               "The mobile number you entered is already registered with us.")

        return render(request, 'Accounts/signup.html')
    else:
        return redirect('/')


@unauthenticated_user
def signup(request):
    return render(request, 'Accounts/signup.html', {'states': states})

# Function to login a user


@unauthenticated_user
def login_request(request):
    email = request.POST['email']
    password = request.POST['password']
    if App_User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        user = authenticate(
            request, username=user.username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
    else:
        messages.error(request,
                       "The login was not successful. Please try again with correct combination of  email and  password. ")
    return render(request, 'Accounts/login.html')


@unauthenticated_user
def login(request):
    return render(request, 'Accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('/')


def myaccount(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        email = request.user.email
        user = App_User.objects.get(email=email)
        user_first_name_login = user.first_name
        user_last_name_login = user.last_name
        user_name_login = user_first_name_login+" "+user_last_name_login
        user_email = user.email
        user_mobile = user.mobile
        user_address1 = user.address1
        user_address2 = user.address2
        user_city = user.city
        user_state = user.state
        user_type = user.user_type.capitalize()
        user_address = [user_address1, user_address2, user_city, user_state]
        return render(request, 'Accounts/myaccount.html', {'name': user_name_login, 'email': user_email, 'mobile': user_mobile, 'address': user_address, 'user_type': user_type})


@authenticated_user
def edit_account(request):
    if (request.method == 'POST'):
        email = request.user.email
        user = App_User.objects.get(email=email)

        if user.password == request.POST['password']:
            user_first_name_login = user.first_name
            user_last_name_login = user.last_name
            user_email = user.email
            user_mobile = user.mobile
            user_address1 = user.address1
            user_address2 = user.address2
            user_city = user.city
            user_state = user.state
            user_type = user.user_type.capitalize()
            user_type_bool = True if user_type == 'Donor' else False
            user_pass = user.password
            return render(request, 'Accounts/edit_account.html', {"user_first_name_login": user_first_name_login, 'user_last_name_login': user_last_name_login, 'email': user_email, 'user_mobile': user_mobile, 'user_address1': user_address1, 'user_address2': user_address2, 'user_city': user_city, 'user_state': user_state, 'user_type': user_type, 'states': states, 'user_type_bool': user_type_bool, 'user_pass': user_pass})
        else:
            messages.error(request,
                           "Authentication failed. Please try again.")
    return render(request, 'Accounts/authenticate.html')


@authenticated_user
def save_edit_account(request):
    if request.method == 'POST':
        # Getting data and saving changes in custom model
        email = request.user.email
        user = App_User.objects.get(email=email)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user.address1 = request.POST['user_address_1']
        user.address2 = request.POST['user_address_2']
        user.city = request.POST['user_city']
        user.state = request.POST['user_state']
        first_name.replace(" ", "")
        last_name.replace(" ", "")
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        # Saving data in Django model
        user2 = User.objects.get(email=email)
        name = f'{first_name} {last_name}'
        name = name_assign(name)
        user2.first_name = first_name
        user2.last_name = last_name
        user2.save()
    return redirect('/')

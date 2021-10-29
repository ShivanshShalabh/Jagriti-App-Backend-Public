from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="Login"),
    path('signup', views.signup, name="Sign Up"),
    path('myaccount/edit', views.edit_account, name="My Account"),
    path('myaccount', views.myaccount, name="My Account"),
    path('login_request', views.login_request, name="Login Request"),
    path('signup_request', views.signup_request, name="Sign Up Request"),
    path('save_edit_account', views.save_edit_account, name="Edit Account"),
    path('logout', views.user_logout, name="Logout")
]

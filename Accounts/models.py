from django.db import models


class App_User(models.Model):
    user_id = models.AutoField
    first_name = models.CharField(max_length=100, unique=False, default="")
    last_name = models.CharField(max_length=100, unique=False, default="")
    email = models.CharField(max_length=100, unique=True, default="")
    mobile = models.IntegerField(unique=True)
    address1 = models.CharField(max_length=125, default="")
    address2 = models.CharField(max_length=125, default="")
    city = models.CharField(max_length=75, default="")
    state = models.CharField(max_length=125, default="")
    password = models.CharField(max_length=20, default="")
    user_type = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.email

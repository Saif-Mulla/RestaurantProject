from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField()
    pincode = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=200)
    name = models.CharField(max_length=100, null=True,blank=True)
    role = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.user.username}'


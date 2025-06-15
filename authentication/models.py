from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    role_choices=(
        ('patient','Patient'),
        ('doctor','Doctor')
    )
    role=models.CharField(choices=role_choices,max_length=10)
    profile_picture=models.ImageField(upload_to='profile_pictures/',null=True,blank=True)

    def __str__(self):
        return self.username

class Address(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='address')
    street=models.CharField(max_length=250)
    state=models.CharField(max_length=75)
    city=models.CharField(max_length=75)
    pincode=models.CharField(max_length=10)
    country=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.username} - {self.pincode}'

    

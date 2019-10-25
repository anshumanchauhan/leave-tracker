from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

USER_TYPES = (
	(0, ''),
	(1,	'manager'),
    (2, 'Employees'),
    
)


class Employee_Add(models.Model):
    emp_name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    contact_number=models.IntegerField()
    username=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    working_days=models.IntegerField()
       
class Employee_Leaves(models.Model):
    leave_from=models.DateTimeField()
    leave_to=models.DateTimeField()
    days=models.IntegerField(default=0)
    notes=models.CharField(max_length=1000)
    
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    user_type = models.IntegerField(choices=USER_TYPES)
    def __str__(self):
        return self.user.username


    




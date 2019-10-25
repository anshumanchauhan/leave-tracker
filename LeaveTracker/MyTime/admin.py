from django.contrib import admin
from .models import Employee_Leaves
from .models import Employee_Add
from MyTime.models import UserProfileInfo, User
# Register your models here.

admin.site.register(Employee_Add)
admin.site.register(Employee_Leaves)
admin.site.register(UserProfileInfo)



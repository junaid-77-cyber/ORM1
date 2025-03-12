# Ex02 Django ORM Web Application
## Date: 12.03.2024

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details .

## PROGRAM
```
Admin.py
from django.contrib import admin
from.models import Employees,EmployeeAdmin
admin.site.register(Employees,EmployeeAdmin)

Models.py
from django.db import models
from django.contrib import admin
class Employees (models.Model):
    Emp_id=models.IntegerField(primary_key=True)
    Emp_name=models.CharField(max_length=30)
    Emp_salary=models.IntegerField()
    Emp_email=models.EmailField()

class EmployeeAdmin (admin.ModelAdmin):
    list_display=('Emp_id','Emp_name','Emp_salary','Emp_email')
```


## OUTPUT

![alt text](<Screenshot (18).png>)


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully

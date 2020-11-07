from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField("Gender", max_length=500, default='NULL')
    dob = models.CharField("Date Of Birth", max_length=500,default='NULL')
    qualification = models.CharField("Educational Qualification", max_length=500,default='NULL')
    
    designation = models.CharField("Designation", max_length=50, default='NULL')
    address = models.CharField("Address", max_length=500,default='NULL')
    phone_no = models.CharField("Phone", max_length=15,default='NULL')
    lsgd = models.CharField("LSGD", max_length=50,default='NULL')
    recent_application = models.CharField("Recent Application", max_length=500,default='NULL')
    total_apps = models.CharField("Total Applications", max_length=500,default='NULL')
    entered_apps = models.CharField("Entered Applications", max_length=500,default='NULL')
    verified_apps = models.CharField("Verified Applications", max_length=500,default='NULL')

    def __str__(self):
        return f'{self.designation} Profile'
        

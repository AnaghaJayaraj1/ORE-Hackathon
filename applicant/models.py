from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Applicant_details(models.Model):
    application = (
        ('Birth Certificate', 'Birth Certificate'),
        ('Death Certificate', 'Death Certificate'),
        ('Marriage Certificate', 'Marriage Certificate'),
        ('License', 'License'),
    )
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    #emp = models.ForeignKey(User)
    applicant_name = models.CharField("Name of Applicant", max_length=50, default='NULL', null='true')
    application_no = models.CharField("Application Number", max_length=50, default='NULL', null='true')
    phone_no = models.CharField("Phone", max_length=15,default='NULL', null='true')
    recent_application = models.CharField("Recent Application ", max_length=50, default='NULL', choices=application, null='true')

    def __str__(self):
        return self.application_no

class Feedback(models.Model):
    one = models.CharField("Q1", max_length=50, default='NULL', null='false')
    two = models.CharField("Q2", max_length=50, default='NULL', null='false')
    three = models.CharField("Q3", max_length=50, default='NULL', null='false')
    four = models.CharField("Q4", max_length=50, default='NULL', null='false')
    five = models.CharField("Q5", max_length=50, default='NULL', null='false')
    six = models.CharField("Q6", max_length=50, default='NULL', null='false')

    def __str__(self):
        return self.one
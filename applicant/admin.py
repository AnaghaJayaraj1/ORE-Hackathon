from django.contrib import admin

# Register your models here.
from .models import Applicant_details, Feedback

admin.site.register(Applicant_details)
admin.site.register(Feedback)


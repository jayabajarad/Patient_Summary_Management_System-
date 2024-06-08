from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
  
class UserProfile(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
   
    def __str__(self):
        return self.user.username 

class Hospital(models.Model):
    HospitalName = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.HospitalName  
    
class Patient(models.Model):
    hospital = models.ForeignKey(Hospital, related_name='patients',on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100, null=False)
    phoneNo = models.CharField(max_length=10,null=False)
    email = models.CharField(max_length=100, null=False)
    dob = models.DateField(null=True)
    GENDER_TYPES = [
        ('Female', _('Female')),
        ('Male', _('Male')),
        ('Other', _('other')),
        # Add more types as needed
    ]
    gender = models.CharField(max_length=20, choices=GENDER_TYPES)
    address = models.CharField(max_length=255, null=False)
    doctor = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Report(models.Model):
    patient = models.ForeignKey(Patient, related_name='reports',on_delete=models.CASCADE, null=False)
    DieaseName = models.CharField(max_length=100, null=False)
    TestReport = models.FileField(upload_to='images/',null=True, blank=True)
    Medicine = models.FileField(upload_to='images/',null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.DieaseName 


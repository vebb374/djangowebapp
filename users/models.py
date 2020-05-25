from django.db import models 
from django.contrib.auth.models import  User
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField



    
# Create your models here.

class profile(models.Model):
    gender_choices = [
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other'),]

    category_choices =[
        ('OC','Other Caste'),
        ('BC','Backward Caste'),
        ('SC','Scheduled Caste'),
        ('ST','Scheduled Tribe'),

    ]

    pwd_choices=[
        ('yes','yes'),
        ('no','no'),

    ]

    nationality_choices=[
        ('India','India'),
        ('Other country','Other country'),

    ]

    branch_choices=[
        ('Cse','Cse'),
        ('Ece','Ece'),
        ('Eee','Eee'),
        ('Civil','Civil'),
        ('Mech','Mech'),
        ('Chemical','Chemical'),
        ('Bio-tech','Bio-tech'),
        ('metallurgy','Metallurgy'),



    ]



    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Profilepic = models.ImageField(default='default.png',upload_to='profile_pics')
    Fullname =models.CharField(blank=False,default=None,max_length=40)
    Gender = models.CharField(blank=False,choices=gender_choices,max_length=10,default=None)
    DOB=models.DateField(null=True)
    Mothername =models.CharField(blank=False,max_length=40,default=None)
    Fathername =models.CharField(blank=False,max_length=40,default=None)
    nationality =models.CharField(blank=False,max_length=30,choices=nationality_choices,default=None)
    address = models.TextField(default='your address with pincode',max_length=200)
    phone_number=PhoneNumberField(blank=False,default=None)
    pwd=models.CharField(blank=False,max_length=10,choices=pwd_choices,default=None)
    branch=models.CharField(blank=False,max_length=20,choices=branch_choices,default=None)
    category =models.CharField(blank=False,choices=category_choices,max_length=10,default=None)
    tenthcertificate = models.FileField(blank=False,upload_to='tenth',default='default.pdf')
    intercertificate = models.FileField(blank=False,upload_to='inter',default='default.pdf')
    jeerankcertificate = models.FileField(blank=False,upload_to='jee',default='default.pdf')
    aadhar_card = models.FileField(blank=False,upload_to='aadhar',default='default.pdf')






    
    
    def __str__(self):
        return f'{self.user.username} Profile'

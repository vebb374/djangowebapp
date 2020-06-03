from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import profile
from django.db import models
from btech import settings
from django.contrib.admin.widgets import AdminDateWidget
class DateInput(forms.DateInput):
    input_type = 'date'



class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model =User
        fields =['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email= forms.EmailField()
    class Meta:
        model =User
        fields =['username','email']
    
    

class ProfileUpdateForm(forms.ModelForm):
    
        DOB = forms.DateField(label='Date of Birth',widget = forms.SelectDateWidget(years=[1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]))    
        class Meta:
            model =profile
            fields =[
            'Profilepic',
            'Fullname',
            'Gender','DOB','Mothername',
            'Fathername','nationality','address','phone_number','pwd','branch','category','aadhar_card',
            'tenthcertificate','intercertificate','jeerankcertificate'
                    ]
            widgets = {
                'DOB': forms.DateInput(attrs={'class':'datepicker'}),
                
                }


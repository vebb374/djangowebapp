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
    
        DOB = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,label='Date of Birth',widget = forms.SelectDateWidget())    
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
                'DOB': DateInput(),
                }


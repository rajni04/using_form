from .models import *
from django import forms
from django.forms.widgets import DateInput

class LoginForm(forms.Form):
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'phone_number'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'password']

class StudentForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields='__all__'
        exclude = ['is_staff','last_login','is_active','date_joined','user_permissions','groups','is_superuser','status']
        labels = {
        'dob': ('D.O.B'),
    }
    widgets = {
        'dob': DateInput(attrs={'type': 'date'})
    }
class ClassForm(forms.ModelForm):
    class Meta:
        model = ClassDetail
        fields = '__all__'
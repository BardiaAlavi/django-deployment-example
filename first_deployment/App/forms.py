from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from App import models


class mainform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username', 'password', 'email')
class subform(forms.ModelForm):
    class Meta():
        model=models.user_entry
        fields=('images', 'sites')

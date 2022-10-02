from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from learner.models import Course

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class Createcourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"  




class UFF(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'mulltiple':True, 'class':'ffi'}))



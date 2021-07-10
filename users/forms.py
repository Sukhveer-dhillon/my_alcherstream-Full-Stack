#creating user creation forms (with added features)
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
# to update user profile
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        #which model it will save data
        model=User
        # how form will be displayed
        fields=['username','email','password1','password2']

# to update user profile
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        #which model it will save data
        model=User
        # how form will be displayed
        fields=['username','email']

# to update user profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']

# when we put it in template it will look like one form

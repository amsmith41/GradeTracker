from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #there is a new email!

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #the fields that are gonna be shown
        #password 1 and password2 for confirmation

#Handle user input in a structured way (e.g., via HTML forms).
#Validate and clean the data submitted by users.
#Can be standalone or tied to a model (using ModelForm).
#Provide fields for user input in templates (via {% form %} in Django templates).
#Handle validation (e.g., required fields, specific formats, custom validation).
#Return cleaned data (form.cleaned_data) after validation.

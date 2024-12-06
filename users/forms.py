from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#make sure to import the custom User Model
from .models import User


#because we wanna add more fields to the the form  just UserCreationForm is not enough
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #there is a new email!  #there is a new email! add an additional! default required = true
    #class meta gives a nested namespace for configuration keeps the config in one place
    class Meta:
        #will save it to the user
        model = User #specify the model we want this form to interact with    whenever this form validates it will create a new user
        fields = ['username', 'email', 'password1', 'password2']
        #the fields that are gonna be shown
        #password 1 and password2 for confirmation




#Handle user input in a structured way (e.g., via HTML forms).
#Validate and clean the data submitted by users.
#Can be standalone or tied to a model (using ModelForm).
#Provide fields for user input in templates (via {% form %} in Django templates).
#Handle validation (e.g., required fields, specific formats, custom validation).
#Return cleaned data (form.cleaned_data) after validation.



#class CreateUserForm(forms.ModelForm):
#    #Contains attributes like model and fields to define which model the form works with and which fields should be included.
#    class Meta:
#        model = User
#        fields = ['first_name', 'last_name', 'is_instructor', 'id_number', 'email', 'bio']
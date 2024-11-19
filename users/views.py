from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def registerNewUser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #instance of the form that has the request.POST
        if form.is_valid(): #We need ton validate the form !! if its valid! built in function
            form.save() #saving the user info to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome to our Grade Tracker! New Account created for {username}! We cheer for your success!')
            return redirect('gradetracker-home') #redirect the user back to the gradetracker home page!
    else: #any other requests
        form = UserRegisterForm() #just a blank form
    return render(request, 'users/register.html', {'form': form})

#HTTP Request: Get request which you send when you naviagte to the webpage 
#post request:  going to contain the message in the body

#message.debug
#message.info
#message.success
#message.warning
#message.error
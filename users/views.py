
from django.contrib.auth.models import User #user model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm #to create a new user form django has it built in!

from .forms import UserRegisterForm
from django.urls import reverse
#form = UserCreationForm()


#user will have its own forms and templates and routes etc that is gonna be separate fromm the blog itself
#when we update the user , we know where to loook user app
#manage.py startapp users   which handles all the user logic for us
#now lets add it to our installepd apps


def registerNewUser(request):
    if request.method == 'POST':
        ##instantiaties user form data with the post data instance of the form that has the request.POST
        form = UserRegisterForm(request.POST) #instance of the form that has the request.POST
        #valdiate it! django does backend  checks for us if failed it will go back to the register form
        if form.is_valid(): #We need ton validate the form !! if its valid! built in function
            form.save() #saving the user info to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome to our Grade Tracker! New Account created for {username}! We cheer for your success!')
            return redirect('gradetracker-home')
            #return redirect('gradetracker-home') # redirect the user back to the gradetracker home page!
    else: #any other requests
        form = UserRegisterForm() #just a blank form
    
    context = {
        'form' : form
    }
    
    
    return render(request, 'users/register.html', context)

#HTTP Request: Get request which you send when you naviagte to the webpage 
#post request:  going to contain the message in the body

#message.debug
#message.info
#message.success
#message.warning
#message.error



'''
def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('gradetracker-home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try: #first get the userobject that corresponds to the typed email
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
        
        #if authenticate success it will not be None
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('gradetracker-home')
        else: #Error!
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    
    return render('gradetracker-login')
    #return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request) #that logs a user out of the current session
    return redirect('gradetracker-home') #After the user is logged out, the function redirects the user to a page identified by the URL pattern named home.




#responsible for handling user registration process
def registerUser(request):
    form = UserRegisterForm()
    
    #A POST request indicates the user has submitted the form with data.
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): #validates the form
            user = form.save(commit=False) #Saves the form data to create a user object but doesn't commit it to the database yet.
            user.username = user.username.lower() #conver the name to a lower case , prevents potneial issues with case sensitivity
            user.save() #saves the modifed object to the databse
            login(request, user) #Logs the newly registered user in automatically using Django’s login() function.
            return redirect('base/home.html')
        else: #if invalid, adds an error message to the message framework
            messages.error(request, 'An error occurred during registration')
    
    context = {
        'form' : form
    }
    
    return render(request, 'users/register.html', context)
#f the request is not POST or the form is invalid:
#Renders the login_register.html template.
#Passes the form ({'form': form}) so it can be displayed on the page.
'''
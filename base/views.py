

#render for using html templates

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#UserPassesTestMixin so that only the author of the post can update it
#login requireed to access that functionality
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required #login required decorator login is needed to!
from django.utils import timezone

#login requireed to access that functionality   
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import User, Course, Assignment, Comment, UserCourse, StudentAssignment

from .forms import SubmittedAssignmentForm, AssignmentForm
from django.urls import reverse

#from .forms import RoomForm, UserForm, MyUserCreationForm
#list a dicti
#add some dummy data, se how we can display in our template

assignments = [
    {
        'Instructor': 'Jaehong Lee',
        'Assignment': 'Understanding Object Oriented Programming',
        'Content': 'Write a brief paragraph (100 - 200 words) on what you learned about through your Internet Research',
        'Posted': 'November 1, 2024'
    },
    {
        'Instructor': 'Jaehong Lee',
        'Assignment': 'Understanding various UML Diagrams',
        'Content': 'Write a brief paragraph (400 - 500 words) on what you learned about through your Internet Research',
        'Posted': 'November 15, 2024'
    }
]






#this is the genreic course page
#login_required   when loading the page it will cause issues also, when clicking on thesignu p causes because it redirectd
def home(request):
    #let's create a dictionary
    context = {
        #'posts': posts #dictionary we created at the top
        #'posts': Post.objects.all()
        'courses': Course.objects.all()
    }
    #sec arg: template name we wanna pass in
    return render(request, 'base/home.html', context) #still returns http response
    #pass that data into the template





def about(request):#we can also directly pass in the dic arg
    return render(request, 'base/about.html', {'title': 'About'})



'''
@login_required
def gradeReport(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'base/gradeReport.html', context)
'''


@login_required
def gradeReport(request):
     # Get the current logged-in user
    user = request.user
    
    # Retrieve the UserCourse instances for the logged-in user (all the courses they are enrolled in)
    user_courses = UserCourse.objects.filter(user=user)
    courses = Course.objects.all()
    
    # Prepare the context with user courses and their grades
    context = {
        'user_courses': user_courses,
        'courses': courses
    }
    
    return render(request, 'base/gradeReport.html', context)


#make sure to include pk as the second argument so that it can accept url that has pk as argument as well!
def course(request, pk): #when we select a specific course
    
    # Retrieve the course object based on the primary key
    course = get_object_or_404(Course, pk=pk) #other wise return 404 error page
    
    
    # Filter assignments that are linked to this course
    assignments = Assignment.objects.filter(course_name=course.course_name)
    
    
    #if I wanna filter by the instance istself like course = course \.
    #in Course Model instead of course_name = models.CharField(max_length=100)
    #you need to change it to course = models.ForeignKey(Course, on_delete=models.CASCADE)  # ForeignKey instead of course_name

    #let's create a dictionary
    context = {
        #'assignments' : assignments #dictionary we created at the top
        #'assignments': Assignment.objects.all()
        'course' : course,
        'assignments' : assignments,
    }
    
    
    return render(request, 'base/course.html', context)


def courseAssignmentPage(request, pk):
    
    student = request.user
    # Filter assignments that are linked to this course
    course = get_object_or_404(Course, pk=pk)
    #course = Course.objects.get(pk=course_id)
    assignments = Assignment.objects.filter(course_name=course.course_name)
    student_assignments = StudentAssignment.objects.filter(student=student,
                                                           course_name=course.course_name)
    #assignments = get_object_or_404(Assignment, pk=pk) #other wise return 404 error page
    #let's create a dictionary
    context = {
        'assignments' : assignments, #dictionary we created at the top
        'student_assignments' : student_assignments,
        
        #'assignments': Assignment.objects.all()
    }
    return render(request, 'base/assignmentPage.html', context) #still returns the http response

#Works Fine!!
class AssignmentDetailView(DetailView):
    model = Assignment


def submitAssignment(request, pk):
    #first get the right assignment!
    assignment = get_object_or_404(Assignment, pk=pk)
    
    if request.method == 'POST': #if clicked on the submit assignment!
        form = AssignmentForm(request.POST, instance=assignment)  # Bind the form with the POST data
        
        #if assignment.is_submit_button_clicked == False:
        #    assignment.is_submit_button_clicked = True
        #form = SubmittedAssignmentForm(request.POST, instance=assignment)
        
        # Manually update the fields
        #assignment.is_submitted = True
        #assignment.submitted_response = request.POST.get('submitted_response', '')  # Get the response from the form
        #assignment.submission_posted = timezone.now()  # Set the current timestamp
        
        #assignment.save()
        if form.is_valid():
            assignment = form.save(commit=False)  # Save the form but don't commit yet
            assignment.is_submitted = True  # Mark the assignment as submitted
            assignment.submitted_response = request.POST.get('submitted_response', '')  # Get the response from the form
            assignment.submission_posted = timezone.now()  # Set the current timestamp
            
            assignment.save()  # Save the assignment data to the database
        #    form.save()  # Save the changes to the database
        #    assignment.is_submit_button_clicked = False
        #    return redirect(reverse('gradetracker-assignment-detail', kwargs={'pk': assignment.pk}))
        #    #return redirect('gradetracker-assignment-detail', pk=assignment.pk)  # Redirect to the assignment details page after submission
            
    else: #if not submitting the assignment
        form = SubmittedAssignmentForm(instance=assignment)
        #assignment.is_submit_button_clicked = False #set to false
      
    context = {
        "assignment": assignment,
        'form' : form
    }  
        
    
    return render(request, 'base/assignment_detail.html', context)

def submitPage(request, pk):
    #first get the right assignment!
    assignment = get_object_or_404(Assignment, pk=pk)
    
    
    context = {
        "assignment": assignment,
    }
    return render(request, 'base/submitPage.html', context)






def commentPage(request, pk):
    assignment = get_object_or_404(Assignment, pk = pk)
    context = {
        'assignment' : assignment,
        'comments': Comment.objects.all(),
    }
    return render(request, 'base/comment_detail.html' , context)




class CourseListView(ListView):
    model = Course
    template_name = 'base/base.html'
    context_object_name = 'courses'
    ordering = ['-date_posted']

class CourseDetailView(DetailView):
    model = Course



class CommentListView(ListView):
    model = Comment
    template_name = 'base/commentPage.html'  # <app>/<model>_<viewtype>.html ##LOOK FOR THE TEMPLATE THIS FORM
    context_object_name = 'comments'
    ordering = ['-date_posted'] # Comments listed newest to oldest

class CommentDetailView(DetailView):
    model = Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'base/comment_form.html' #make sure to set the template name!!!
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) #super() on our parent class



#shouldnt stop from others updating the post
#only the author can uodate ut UserPasses TestMixin

#we will inherit these classes later LoginRequiredMixin, UserPassesTestMixin
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#we will inherit these classes later LoginRequiredMixin, UserPassesTestMixin
#as view function as_view() is a class method provided by Django's View class (the parent of all class-based views).
#It converts the class into a callable function that can be used in Django's URL routing system.
class CommentDeleteView(DeleteView):
    model = Comment
    #if using this the CommentDeleteView in your views likely relies on the default delete confirmation template provided by Django's generic DeleteView.
    template_name = 'base/comment_delete.html' #therefore, we need to explicitly specify the html to look for
    #success_url = 'base/commentPage.html' #after it deletes it it goes back to the orioginal url
    #success_url = '/' if written like this it will go back to the original url 
    
    #but instead we will use this method to go back to the commentPage
    def get_success_url(self):
    # Redirect back to the specific comment page
        return reverse('gradetracker-commentPage', kwargs={'pk': self.object.pk})

    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





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
    form = CreateUserForm()
    
    #A POST request indicates the user has submitted the form with data.
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): #validates the form
            user = form.save(commit=False) #Saves the form data to create a user object but doesn't commit it to the database yet.
            user.username = user.username.lower() #conver the name to a lower case , prevents potneial issues with case sensitivity
            user.save() #saves the modifed object to the databse
            login(request, user) #Logs the newly registered user in automatically using Django’s login() function.
            return redirect('gradetracker-home')
        else: #if invalid, adds an error message to the message framework
            messages.error(request, 'An error occurred during registration')
    
    context = {
        'form' : form
    }
    
    return render(request, 'base/register.html', context)
#f the request is not POST or the form is invalid:
#Renders the login_register.html template.
#Passes the form ({'form': form}) so it can be displayed on the page.
'''
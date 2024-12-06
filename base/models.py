from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #user model
from django.urls import reverse

#for User class
#username: The user's username (e.g., "johndoe").
#first_name: The user's first name (e.g., "John").
#last_name: The user's last name (e.g., "Doe").
#email: The user's email address (e.g., "johndoe@example.com").
#password: The user's hashed password (used internally for authentication).

#django has already a built in authentication system
#and already has a user model  that its created for us

#inherits from Model class






class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_registered  = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    course_description = models.TextField(default="No description available") #lines lines of text unrestricted
    
    
    #to make the course print out by title
    def __str__(self):
        return self.course_name




class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    participation = models.FloatField(null=True, blank=True)
    assignment_average = models.FloatField(null=True, blank=True)
    midterms_average = models.FloatField(null=True, blank=True)
    final = models.FloatField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.user.first_name} - {self.course.course_name}"



class Assignment(models.Model):
    #one to many: an instructor can upload many assignments
    course_name = models.CharField(max_length=100, default= "Unknown")
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment_title = models.CharField(max_length=100)
    assignment_posted = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)  # Grade field as a float
    instruction = models.TextField(default = "Here are the instructions for the assignment!")
    
    is_submit_button_clicked = models.BooleanField(default=False) 
    is_submitted = models.BooleanField(default=False)  # Boolean field, default is False
    #auto_now=True, which updates the timestamp whenever the object is modified.
    submission_posted = models.DateTimeField(auto_now=True) #for last modified
    submitted_response = models.TextField(null = True, blank=True)
    
    
    #to make the post print out by title
    def __str__(self):
        return f"{self.assignment_title} by {self.instructor.first_name} {self.instructor.last_name}"
    
    
    #if succeessfuly submitting the assignment!
    #if I wanna go back to after click or sth I should get url function and return reverse!!
    def get_success_url(self):
    # Redirect back to the specific comment page
        return reverse('gradetracker-assignmentPage', kwargs={'pk': self.object.pk})


class StudentAssignment(models.Model):
    course_name = models.CharField(max_length=100, default= "Unknown")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_assignments")
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="student_assignments")
    grade = models.FloatField(null=True, blank=True)  # Unique score for each student
    submitted_response = models.TextField(null=True, blank=True)  # Student's unique response
    is_submitted = models.BooleanField(default=False)
    submission_posted = models.DateTimeField(auto_now=True)  # Last submission timestamp
    
    def __str__(self):
        return f"{self.student.username}'s {self.assignment.assignment_title} assignment"



class Comment(models.Model):
    #multiple authors can leave many comments on the discussion post
    title = models.CharField(max_length=100, default= 'No title') #max length 100
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField() #lines lines of text unrestricted
    date_posted = models.DateTimeField(default=timezone.now)
    
    #to make the comment print out by title
    def __str__(self):
        return f"{self.author.first_name} {self.author.last_name}'s comment"
    
    
    #so django know how to find the location of the url of the specific post!
    def get_absolute_url(self):  #it needs with a primary key
        return reverse('gradetracker-commentPage', kwargs={'pk': self.pk}) #simply return the url as a string
        #and let the view handle the redirect for us.     it needs a speicific post with a primary key
        #so instance of that post with a primary key
    #redirect: redirect to that speicifc route
    #reverse will simply return the full url to that route as a string
    

    
    
    

class Post(models.Model):
    title = models.CharField(max_length=100) #max length 100
    content = models.TextField() #lines lines of text unrestricted
    date_posted = models.DateTimeField(default=timezone.now)  #since I like flexibility of the date changed 
    #now pass in the fucntuion as the default value  we dont want to execute the func at that point
    #auto_now = true, meaning update the date posted to the current date time every time the post was updated
    #auto_now_add = True meaning that would set the date posted to the current date time only when this object is created
    # this cavet ti you cant update the value of the date posted. 
    
    #each post has one author author can have multiple posts.
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user deleted we also delting the posts as well
    #but if deleting a post it wont delete the user
    
    #to make the post print out by title
    def __str__(self):
        return self.title
    
    #we need to make migrations and  migrate!
    
    
    

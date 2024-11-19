from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #user model

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

class Assignment(models.Model):
    #one to many: an instructor can upload many assignments
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment_title = models.CharField(max_length=100)
    assignment_posted = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)  # Grade field as a float
    instruction = models.TextField(default = "Here are the instructions for the assignment!")
    #to make the post print out by title
    def __str__(self):
        return f"{self.assignment_title} by {self.instructor.first_name} {self.instructor.last_name}"

class Comment(models.Model):
    #multiple authors can leave many comments on the discussion post
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField() #lines lines of text unrestricted
    comment_posted = models.DateTimeField(default=timezone.now)
    
    #to make the comment print out by title
    def __str__(self):
        return f"{self.author.first_name} {self.author.last_name}'s comment"
    

    
    
    

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
    
    
    

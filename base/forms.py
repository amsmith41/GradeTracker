from django import forms
from .models import Assignment
from django.utils import timezone


class AssignmentForm(forms.ModelForm):
    submitted_response = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))
    class Meta:
        model = Assignment
        fields = ['course_name', 'assignment_title', 'instruction', 'grade', 'is_submit_button_clicked', 'submitted_response']




#we need to create a form ! because submitted assignment involved getting an input from user !
class SubmittedAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['is_submitted', 'submitted_response'] #listing the fields that the form will handle
    
    
    #In a Django form class, self refers to the form instance itself, 
    #not the model instance that the form is linked to. For example, self inside a form's method (like clean or save) refers to the form object, not the specific model object.
    def save(self, commit = True): #In django save used to save an object to the database
        #if self.cleaned_data.get('is_submitted'):
        #self.instance refers to the model that you are working iwht
        self.instance.is_submitted = True
        self.instance.submission_posted = timezone.now() #set the currrent time!
        
        #calls the parent class’s save() method (
        return super().save(commit)
    
    #commit = True means that object should be save immediately to the data base
    #if commit = False, we should just return an unsaved instance (commit=False) without saving it so that further modifications can be made before the object the object to the database.
        
    
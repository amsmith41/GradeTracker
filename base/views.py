

#render for using html templates

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#login requireed to access that functionality   
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Course, Assignment, Comment, Post



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

#this is the genereic course page
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

def courseAssignmentPage(request):
    #let's create a dictionary
    context = {
        #'assignments' : assignments #dictionary we created at the top
        'assignments': Assignment.objects.all()
    }
    return render(request, 'base/assignment.html', context) #still returns the http response


def commentPage(request):
    context = {
        'comments': Comment.objects.all()
    }
    return render(request, 'base/comment_detail.html' , context)


class PostListView(ListView):
    model = Post
    template_name = 'base/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #newest to oldest


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) #super() on our parent class


#shouldnt stop from others updating the post
#only the author can uodate ut UserPasses TestMixin
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


#as view function as_view() is a class method provided by Django's View class (the parent of all class-based views).
#It converts the class into a callable function that can be used in Django's URL routing system.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' #after it deletes it it goes back to the orioginal url

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

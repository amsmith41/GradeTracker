from django.contrib import admin
from .models import User, Course, Assignment, Comment, Post, UserCourse, StudentAssignment
# Register your models here.
#so we show up on our admin page where we can register models on our admin site
#using backend admin view we ahave the ability to change our data as well not only jsut the console!


admin.site.register(Course)
admin.site.register(UserCourse)
admin.site.register(Assignment)
admin.site.register(StudentAssignment)
admin.site.register(Comment)
admin.site.register(Post)
from django.urls import path
from . import views
#from users import views Now users.py has  no home attribute resolved! This was the reason for the error!!!!!!!!!!!!!!
from .views import(
    CommentListView,
    CommentDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    
    AssignmentDetailView,
)



urlpatterns = [
    path('', views.home, name='gradetracker-home'),
    path('about/', views.about, name='gradetracker-about'),
    path('gradeReport/', views.gradeReport, name = 'gradetracker-grade-report'),
    path('course/<int:pk>', views.course, name = 'gradetracker-course'),
    path('assignmentPage/<int:pk>', views.courseAssignmentPage, name='gradetracker-assignmentPage'),
    path('assignment/<int:pk>', AssignmentDetailView.as_view(), name = 'gradetracker-assignment-detail'),
    path('submitPage/<int:pk>', views.submitPage, name = 'gradetracker-assignment-submit'),
    
    path('commentPage/create', CommentCreateView.as_view(), name='gradetracker-commentCreate'),
    path('commentPage/<int:pk>', CommentListView.as_view(), name = 'gradetracker-commentPage'),
    path('commentPage/<int:pk>/update', CommentCreateView.as_view(), name = 'gradetracker-commentUpdate'),
    path('commentPage/<int:pk>/delete', CommentDeleteView.as_view(), name = 'gradetracker-commentDelete'),

    
]

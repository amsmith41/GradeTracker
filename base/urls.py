from django.urls import path
from . import views
from .views import(
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', views.home, name='gradetracker-home'),
    path('about/', views.about, name='gradetracker-about'),
    path('assignment/', views.courseAssignmentPage, name='gradetracker-assignment'),
    path('comment_detail/', views.commentPage, name = 'gradetracker-comment'),
    
    path('', PostListView.as_view(), name='comment'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='comment-detail'),
    path('post/new/', PostCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='comment-delete'),
    path('about/', views.about, name='blog-about'),
]

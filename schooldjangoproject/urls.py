"""
URL configuration for schooldjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from django.contrib.auth import views as auth_views
from django.conf import settings
from users import views as user_views

#when we import views from users we use an ailias user_views   unlike auth_views
#so that user names dont collide each other

urlpatterns = [
    path('admin/', admin.site.urls), #this the usrl to the admin page by default!
    path('', include('base.urls')), #if nothing included go to base.urls
    
    
    path('register/', user_views.registerNewUser, name='gradetracker-register'),
    #LoginView Handles user login by rendering a login form, validating user credentials, and managing the login process.
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='gradetracker-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='gradetracker-logout'),
]

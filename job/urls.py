"""job URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from core.views import home_view,login_view,signup_view
from idea.views import idea_view, add_idea_view, self_idea_view, collab_idea
from users.views import user_profile_view , applicant_view
from django.contrib.auth.models import User

urlpatterns = [
    path('',home_view , name='home_view'),
    path('login/',login_view),
    path('signup/',signup_view , name='signup'),
    path('admin/', admin.site.urls),
    path('idea<int:idea_id>',idea_view,name="idea_view"),
    path("accounts/", include("django.contrib.auth.urls")), 
    path('addNewIdea/',add_idea_view,name='add_idea'),
    path('myJobs/',self_idea_view,name='my_ideas'),
    path('collab<int:idea_id>',collab_idea,name='collab'),
    path('myProfile/<str:user_id>',user_profile_view,name='profile'),
    path('idea<int:idea_id>/applicant/<str:user_id>',applicant_view,name='applicant'),

]

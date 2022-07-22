from django.shortcuts import render
from users.models import UserAccount
from idea.models import Idea_applicants
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

def user_profile_view(request,user_id):
    user = UserAccount.objects.filter(Username=user_id)
    context={
        'user':user[0]
    }
    return render(request,'profile.html',context)

def applicant_view(request,idea_id,user_id):
    id = User.objects.filter(useraccount=user_id)
    criterion1=Q(user=id[0])
    criterion2=Q(job_id=idea_id)
    applicant = Idea_applicants.objects.filter(criterion1 & criterion2)
    context={
        'applicant':applicant[0],
        'id':user_id
    }
    return render(request,'applicant.html',context)
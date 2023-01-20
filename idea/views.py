from django.shortcuts import redirect, render
from core.views import home_view

from django.contrib.auth.models import User
from users.models import UserAccount
from idea.models import Idea , Idea_applicants
from idea.forms import add_idea_form , collab_idea_form

# Create your views here.

def idea_view(request,idea_id):
    idea = Idea.objects.filter(pk=idea_id)
    applied_users = Idea_applicants.objects.filter(job_id=idea_id).values('user')
    list=[]
    n=len(applied_users)
    if n!=0:
        for users in applied_users:
            query = UserAccount.objects.filter(userId=users.get('user')) 
            list.append(query[0])
    context={
        'idea':idea[0],
        'applied_users':list
    }
    return render(request,"idea.html",context)

def add_idea_view(request,*args,**kwargs):
    form = add_idea_form()
    context = {'form': form}
    if request.method == "POST":
        form = add_idea_form(request.POST or None)
        if form.is_valid():
            form_data=form.cleaned_data
            Idea.objects.create(
                title=form_data.get('title'),
                short_description=form_data.get('short_description'),
                long_description=form_data.get('long_description'),
                created_by=request.user
            )
            return redirect(home_view)  
    return render(request,'add_idea.html',context)

def self_idea_view(request,*args,**kwargs):
    ideas = Idea.objects.filter(created_by=request.user)
    return render(request,'my_ideas.html',{'Idea':ideas})

def collab_idea(request,idea_id):
    form = collab_idea_form()
    if request.method =="POST":
        form = collab_idea_form(request.POST or None)
        if form.is_valid():
            print("hey")
            form_data=form.cleaned_data
            idea = Idea.objects.filter(pk=idea_id)
            Idea_applicants.objects.create(
                user=request.user,
                job_id=idea[0],
                description=form_data.get('description'),
                skills=form_data.get('skills')
            )
        return redirect(home_view)
    return render(request,'colab_idea.html',{'form':form})     


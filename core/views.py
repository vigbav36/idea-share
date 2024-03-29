from django.contrib import messages
from django.shortcuts import redirect, render
from idea.models import Idea
from users.forms import signup_form,login_form
from users.models import UserAccount
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def home_view(request,*args,**kwargs):
    ideas={}
    if request.user.is_authenticated:
        ideas = Idea.objects.all().exclude(created_by=request.user)
    #print(ideas)
    return render(request,"home.html",{'Idea':ideas})

def login_view(request,*args,**kwargs):
    form=login_form()
    if request.method=="POST":
        form=login_form(request.POST or None)
        if(form.is_valid()):
            form_data = form.cleaned_data
            return render(request,"userView.html",{'name':form_data.get("Username")})
    return render(request,"login.html",{'form':form})
    
def signup_view(request,*args,**kwargs):
    form=signup_form()
    context={
        'form': form
    }
    if request.method == "POST":
        form=signup_form(request.POST or None)
        if(form.is_valid()):
            form_data = form.cleaned_data
            user = User.objects.create_user(
                username=form_data.get('Username'),
                email=form_data.get('email'),
                password=form_data.get('password'),
                first_name=form_data.get('name').split()[0]
                )
            print(user.id)
            UserAccount.objects.create(
                Username=form_data.get('Username'),
                userId=user,
                email=form_data.get('email'),
                password=form_data.get('password'),
                name=form_data.get('name'),
                branch=form_data.get('branch'),
            )
            print(form_data.get('Username'))
            login(request, user)
            return redirect('home_view')
        else:
            print(form.errors.as_json(escape_html=False))
            print("not valid")
            return render(request,"signup.html",{'form':form})  
            
    return render(request,"signup.html",context)    
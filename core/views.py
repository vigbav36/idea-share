from django.contrib import messages
from django.shortcuts import redirect, render
from users.forms import signup_form,login_form
from users.models import UserAccount
# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})

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
            UserAccount.objects.create(**form_data)
            print(form_data.get('Username'))

            return redirect('home')
        else:
            print(form.errors.as_json(escape_html=False))
            print("not valid")
            return render(request,"signup.html",{'form':form})  
            
    return render(request,"signup.html",context)    
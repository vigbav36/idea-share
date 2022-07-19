from django.shortcuts import redirect, render
from core.views import home_view

from idea.models import Idea
from users.models import UserAccount
from idea.forms import add_idea_form

# Create your views here.

def idea_view(request,idea_id):
    idea = Idea.objects.filter(pk=idea_id)
    created_user = UserAccount.objects.filter(Username=idea[0].created_by)
    context={
        'idea':idea[0],
        'created_user':created_user[0],
    }
    print(context)
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

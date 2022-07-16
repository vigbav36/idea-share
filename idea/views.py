from django.shortcuts import render

from idea.models import Idea
from users.models import UserAccount

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

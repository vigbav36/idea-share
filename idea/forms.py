from django import forms
from idea.models import Idea,Idea_applicants

class add_idea_form(forms.Form):
    title = forms.CharField()
    short_descirption = forms.CharField()
    long_description = forms.CharField()

#class apply_idea_form(forms.Form):
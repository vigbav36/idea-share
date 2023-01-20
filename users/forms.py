from django import forms
from users.models import UserAccount

class signup_form(forms.Form):

    branches = [('CSE','CSE'),('ECE','ECE')]

    Username=forms.CharField()
    password=forms.CharField()
    name=forms.CharField()
    branch=forms.CharField(widget=forms.Select(choices=branches))
    email=forms.EmailField()

    def clean_email(self,*args, **kwargs):
        email_new=self.cleaned_data.get('email')
        if not email_new.endswith('ssn.edu.in'):
            raise forms.ValidationError('Must be valid email')
        n = UserAccount.objects.filter(email=email_new).count()
        if not n==0:
            raise forms.ValidationError('invalid')
        return email_new
    
    def clean_Username(self,*args,**kwargs):
        name=self.cleaned_data.get('Username')
        n = UserAccount.objects.filter(Username=name).count()
        if not n==0:
            raise forms.ValidationError('UserName already exists')
        return name
    
    
class login_form(forms.Form):
    Username=forms.CharField()
    password=forms.CharField()

    def clean_Username(self,*args,**kwargs):
        new_user = self.cleaned_data.get('Username')
        n = UserAccount.objects.filter(Username=new_user).count()
        if n==0:
            raise forms.ValidationError('User does not exist')
        return new_user

    def clean_password(self,*args,**kwargs):
        new_user = self.cleaned_data.get('Username')
        entered_passwd = self.cleaned_data.get('password')
        passwd = UserAccount.objects.filter(Username=new_user).values('password')
        print(passwd)
        if not passwd[0].get('password')==entered_passwd:
            raise forms.ValidationError('wrong password')
        return entered_passwd
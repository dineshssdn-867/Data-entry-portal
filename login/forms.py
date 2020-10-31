from django import forms
from django.contrib.auth import authenticate
from django.template.context_processors import request


class loginform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        if(username and password):
            user=authenticate(username=username,password=password)

            if not user:
                raise forms.ValidationError("Username or password not correct")
            return super(loginform,self).clean()

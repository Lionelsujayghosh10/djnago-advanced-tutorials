from django import forms 
from django.core.exceptions import ValidationError
import re


class LoginForm(forms.Form):


    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)




    def clean_email(self):
        try:
            email = self.cleaned_data['email'].strip()
            if email is None:
                self.add_error('email', 'Email is required.')
            else:
                if(re.search(self.regex,email)):  
                    pass  
                else: 
                    self.add_error('email', 'Invalid Email Address')
            return email
        except Exception as e:
            self.add_error('email', 'Something went wrong!')


    def clean_password(self):
        try:
            password = self.cleaned_data['password'].strip()
            if password is None:
                self.add_error('password', 'Password is required.')
            else:
                pass
            return password
        except Exception as e:
            self.add_error('password', 'Something went wrong!')



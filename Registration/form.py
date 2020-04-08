from django import forms 
from django.core.exceptions import ValidationError
import re
from .models import Users




class RegistrationForm(forms.Form):

    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


    fname = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    passconf = forms.CharField(max_length=100)




    def clean(self):
        try:
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
            retype_password = cleaned_data.get("passconf")
            if password is not None and retype_password is not None:
                if(password == retype_password):
                    pass
                else:
                    self.add_error('passconf', 'password and retype password are not same.')
            else:
                pass
                # self.add_error('passconf', 'passswod and retype password are required.') 
        except Exception as e:
            self.add_error('passconf', 'Something went wrong!')



    def clean_email(self):
        try:
            email = self.cleaned_data['email'].strip()
            if email is None:
                self.add_error('email', 'Email is required.')
            else:
                if(re.search(self.regex,email)):  
                    check_email = Users.objects.filter(email=email, is_delete=0).values()
                    if(check_email.exists()):
                        self.add_error('email', 'Email already exists.')
                    else:
                        pass  
                else: 
                    # forms.ValidationError("Invalid Email Address") 
                    self.add_error('email', 'Invalid Email Address')
            return email
        except Exception as e:
            self.add_error('email', 'Something went wrong!')




    def clean_fname(self):
        try:
            fname = self.cleaned_data['fname'].strip()
            if fname is None:
                self.add_error('fname', 'fname is required.')
            return fname
        except Exception as e:
            self.add_error('fname', 'fname is required.')



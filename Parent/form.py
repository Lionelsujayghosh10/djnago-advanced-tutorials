from django import forms 
from django.core.exceptions import ValidationError
from django.conf import settings
from .models import Parent




class CreateParentForm(forms.Form):


    parent_code = forms.CharField(max_length=100)
    parent_name = forms.CharField(max_length=100)
    parent_email_address = forms.EmailField(max_length=150)
    parent_password = forms.CharField(max_length=100)



    def clean_parent_code(self):
        try:
            if self.cleaned_data['parent_code'].strip() is not None:
                pass
            else:
                self.add_error('parent_code', 'Parent code is required.')
        except Exception as e:
            self.add_error('parent_code', e)

from django import forms 
from django.core.exceptions import ValidationError
from .models import Classes



class CreateClassForm(forms.Form):



    class_code = forms.CharField(max_length=100)
    class_name = forms.CharField(max_length=100)


    def clean_class_code(self):
        try:
            class_code = self.cleaned_data['class_code'].strip()
            if class_code is not None:
                class_code_exists = Classes.objects.filter(class_code=class_code, deleted__isnull=True).values()
                if class_code_exists.exists():
                    self.add_error('class_code', 'Class code already exists.')
                return class_code
            else:
                self.add_error('class_code', 'Class code is required.')
        except Exception as e:
            self.add_error('class_code', 'Something went wrong!')



    def clean_class_name(self):
        try:
            class_name = self.cleaned_data['class_name'].strip()
            if class_name is not None:
                return class_name
            else:
                self.add_error('class_name', 'Class name is required.')
        except Exception as e:
            self.add_error('class_name', 'Something went wrong!')

from django import forms 
from django.core.exceptions import ValidationError
from .models import Classes, Section



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



class CreateSectionForm(forms.Form):

    section_code = forms.CharField(max_length=100)
    section_name = forms.CharField(max_length=100)
    class_id = forms.IntegerField()


    def clean_section_code(self):
        try:
            section_code = self.cleaned_data['section_code'].strip()
            if section_code is not None:
                section_code_exists = Section.objects.filter(section_code=section_code).values()
                if section_code_exists.exists():
                    self.add_error('section_code', 'Section code already exists.')
                return section_code
            else:
                self.add_error('section_code', 'Section code is required.')
        except Exception as e:
            self.add_error('section_code', 'Something went wrong!')

    def clean_section_name(self):
        try:
            section_name = self.cleaned_data['section_name'].strip()
            if section_name is None:
                self.add_error('section_name', 'Section name already exists.')
            return section_name
        except Exception as e:
            self.add_error('section_name', 'Something went wrong!')


    def clean_class_id(self):
        try:
            class_id = self.cleaned_data['class_id']
            if class_id is None:
                self.add_error('class_id', 'Class id is required.')
            else:
                return class_id
        except Exception as e:
            self.add_error('class_id', 'Something went wrong!')

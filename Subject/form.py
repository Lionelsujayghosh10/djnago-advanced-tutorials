from django import forms 
from django.core.exceptions import ValidationError
from .models import Subject, AssignSubject



class CreateSubjectForm(forms.Form):
    


    subject_code = forms.CharField(max_length=100)
    subject_name = forms.CharField(max_length=100)


    def clean_subject_code(self):
        try:
            subject_code = self.cleaned_data['subject_code'].strip()
            if subject_code is not None:
                subject_code_exists = Subject.objects.filter(subject_code=subject_code).values()
                if subject_code_exists.exists():
                    self.add_error('subject_code', 'Subject code already exists.')
                return subject_code
            else:
                self.add_error('subject_code', 'Subject code is required.')
        except Exception as e:
            self.add_error('subject_code', 'Something went wrong!')



    def clean_subject_name(self):
        try:
            subject_name = self.cleaned_data['subject_name'].strip()
            if subject_name is not None:
                return subject_name
            else:
                self.add_error('subject_name', 'Subject name is required.')
        except Exception as e:
            self.add_error('subject_name', 'Something went wrong!')
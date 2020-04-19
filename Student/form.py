from django import forms 
from django.core.exceptions import ValidationError
from django.conf import settings
from .models import Student




class CreateStudentForm(forms.Form):


    student_code = forms.CharField(max_length=100)
    student_name = forms.CharField(max_length=255)
    roll_number = forms.IntegerField()
    class_id = forms.IntegerField()
    section_id = forms.IntegerField()
    student_image = forms.FileField(required=False)



    def clean(self):
        try:
            cleaned_data = super().clean()
            check_roll_number_exists = Student.objects.filter(section_id=cleaned_data.get('section_id'), roll_number=cleaned_data.get('roll_number')).values()
            if check_roll_number_exists.exists():
                self.add_error('roll_number', 'ROll Number already exists.')
            else:
                return cleaned_data 
        except Exception as error:
            self.add_error('student_code', error)



    def clean_student_code(self):
        try:
            if self.cleaned_data['student_code'].strip() is not None:
                student_code_exists = Student.objects.filter(student_code=self.cleaned_data['student_code']).values()
                if student_code_exists.exists():
                    self.add_error('student_code', 'Student Code already exists.')
                else:
                    return self.cleaned_data['student_code'].strip()
            else:
                self.add_error('student_code', 'Student Code is required.')
        except Exception as errors:
            self.add_error('student_code', 'Something went wrong.')
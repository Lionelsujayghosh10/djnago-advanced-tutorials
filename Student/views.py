from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from .form import CreateStudentForm
from ClassSection.models import Classes, Section
from .models import Student
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required




@login_required
def create_student(request):
    try:
        classes = Classes.objects.all();
        if request.method == 'POST':
            student_form = CreateStudentForm(request.POST, request.FILES)
            if student_form.is_valid():
                # return HttpResponse(request.FILES['student_image'])
                Student.objects.create(student_code=student_form.cleaned_data['student_code'], student_name=student_form.cleaned_data['student_name'], classes_id=student_form.cleaned_data['class_id'], section_id=student_form.cleaned_data['section_id'], roll_number=student_form.cleaned_data['roll_number'],student_image=student_form.cleaned_data['student_image'])
                return render(request, 'student/createstudent.html', {'class_list' : classes, 'success' : 'Student created successfully done.'})
            else:
                send_data = {
                    'class_list' : classes,
                    'form_details' : student_form
                }
            return render(request, 'student/createstudent.html', send_data)
        else:
            send_data = {
                'class_list' : classes
            }
            return render(request, 'student/createstudent.html', send_data)
    except Exception as e:
            send_data = {
                'class_list' : classes,
                'error' : e
            }
            return render(request, 'student/createstudent.html', send_data)

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from .form import CreateSubjectForm
from .models import Subject, AssignSubject
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from ClassSection.models import Classes, Section


@login_required
def create_subject(request):
    try:
        if request.method == 'POST':
            create_form_subject = CreateSubjectForm(request.POST.dict())
            if create_form_subject.is_valid():
                Subject.objects.create(subject_code=create_form_subject.cleaned_data['subject_code'], subject_name=create_form_subject.cleaned_data['subject_name'])
                return render(request, 'subject/createsubject.html', {'success' : 'Subject created successfully done.'})
            else:
                return render(request, 'subject/createsubject.html', {'form_details' : create_form_subject})
        else:
            return render(request, 'subject/createsubject.html')
    except Exception as e:
        return render(request, 'subject/createsubject.html', {'error' : e})



@login_required
def assign_subject(request):
    try:
        class_list = Classes.objects.all()
        subject_list = Subject.objects.all()
        if request.method == 'POST':
            pass
        else:
            return render(request, 'subject/createassignsubject.html', {'class_list' : class_list, 'subject_list' : subject_list})
    except Exception as e:
        class_list = Classes.objects.all()
        subject_list = Subject.objects.all()
        return render(request, 'subject/createassignsubject.html', {'error' : e, 'class_list' : class_list, 'subject_list' : subject_list})

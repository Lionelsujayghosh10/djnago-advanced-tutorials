from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from .form import CreateSubjectForm, AssignSubjectForm
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
            form = AssignSubjectForm(request.POST)
            if form.is_valid():
                if request.POST.get("section_status") == 'true':
                    fetch_all_section = Section.objects.filter(classes_id = form.cleaned_data['class_id'])
                    for single_section in fetch_all_section:
                        check_subject_assign = AssignSubject.objects.filter(subject_id=form.cleaned_data['subject_id'], section_id=single_section.section_id).values()
                        if check_subject_assign.exists():
                            return render(request, 'subject/createassignsubject.html', {'class_list' : class_list, 'subject_list' : subject_list, 'error':'subject already assign.'})
                        else:
                            assign_subject = AssignSubject(classes_id=form.cleaned_data['class_id'], section_id=single_section.section_id,subject_id=form.cleaned_data['subject_id'])
                            assign_subject.save()
                    return render(request, 'subject/createassignsubject.html', {'class_list' : class_list, 'subject_list' : subject_list, 'success':'Subject assign successfully done.'})
                else:
                    if request.POST.get("section_id") is None:
                        return render(request, 'subject/createassignsubject.html', {'class_list' : class_list, 'subject_list' : subject_list, 'error':'Section Id is required.'})
                    else:
                        check_subject_assign = AssignSubject.objects.filter(subject_id=form.cleaned_data['subject_id'], section_id=request.POST.get("section_id")).values()
                        if check_subject_assign.exists():
                            return render(request, 'subject/createassignsubject.html', {'class_list' : class_list, 'subject_list' : subject_list, 'error':'subject already assign.'})
                        else:
                            assign_subject = AssignSubject(classes_id=form.cleaned_data['class_id'], section_id=request.POST.get("section_id"),subject_id=form.cleaned_data['subject_id'])
                            assign_subject.save()
                            return render(request, 'subject/createassignsubject.html', {'class_list' : class_list, 'subject_list' : subject_list, 'success':'Subject assign successfully done.'})
            else:
                return render(request, 'subject/createassignsubject.html', {'class_list' : class_list, 'subject_list' : subject_list, 'form_details':form})
        else:
            return render(request, 'subject/createassignsubject.html', {'class_list' : class_list, 'subject_list' : subject_list})
    except Exception as e:
        class_list = Classes.objects.all()
        subject_list = Subject.objects.all()
        return render(request, 'subject/createassignsubject.html', {'error' : e, 'class_list' : class_list, 'subject_list' : subject_list})



@login_required
def assign_subject_list(request):
    try:
        assign_subject_list = AssignSubject.objects.select_related('classes').select_related('section').select_related('subject').all()
        paginator = Paginator(assign_subject_list, 10)
        page = request.GET.get('page')
        assign_subject_list = paginator.get_page(page)
        return render(request, 'subject/assignsubjectlist.html', {'assign_subject_list': assign_subject_list})
    except Exception as e:
        return HttpResponse(e)

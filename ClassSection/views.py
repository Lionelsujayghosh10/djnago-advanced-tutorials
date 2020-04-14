from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from .form import CreateClassForm, CreateSectionForm
from .models import Classes, Section
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers



@login_required
def create_class(request):
    try:
        if request.method == 'POST':
            create_class_form = CreateClassForm(request.POST)
            if create_class_form.is_valid():
                Classes.objects.create(class_code=create_class_form.cleaned_data['class_code'], class_name=create_class_form.cleaned_data['class_name'])
                return render(request, 'createclass.html', { 'success' : 'Class created successfully done.'})
            else:
                data = {
                    'form_details' : create_class_form
                }
                return render(request, 'createclass.html', data)
        else:
            return render(request, 'createclass.html')
    except Exception as e:
        return render(request, 'createclass.html', { 'error' : e})




@login_required
def list_class(request):
    try:
        # class_list = Classes.objects.filter(deleted__isnull=True)
        class_list = Classes.objects.all()
        paginator = Paginator(class_list, 10)
        page = request.GET.get('page')
        class_details = paginator.get_page(page)
        return render(request, 'classlist.html', {'class_list': class_details})
    except Exception as e:
        return render(request, 'classlist.html', { 'error' : e})
    except ValueError:
        raise Http404



@login_required
def delete_class(request):
    try:
        if request.method == 'POST':
            if request.POST.get('class_id') is not None:
                try:
                    class_exists = Classes.objects.get(pk=request.POST.get('class_id'))
                    class_exists.delete()
                    data = {
                        'success' : 'successfully done.'
                    }
                    return JsonResponse(data)
                except ObjectDoesNotExist:
                    data = {
                        'error' : 'Invalid class id.'
                    }
                    return JsonResponse(data)
            else:
                data = {
                    'error' : 'class Id required.'
                }
                return JsonResponse(data)  
        else:
            data = {
                'error' : 'Unexcepted error ocurred.'
            }
            return JsonResponse(data)
    except Exception as e:
        data = {
            'error' : 'Unexcepted error ocurred.'
        }
        return JsonResponse(data)


@login_required
def create_section(request):
    try:
        class_list = Classes.objects.all()
        if request.method == 'POST':
            create_section_form = CreateSectionForm(request.POST.dict())
            if create_section_form.is_valid():
                #todo : option tag selected in template
                create_section = Section.objects.create(section_code=create_section_form.cleaned_data['section_code'], section_name=create_section_form.cleaned_data['section_name'], classes_id=create_section_form.cleaned_data['class_id'])
                return render(request, 'createsection.html', {'class_list':class_list, 'success' : 'section_created successfully done.'})
            else:
                return render(request, 'createsection.html', {'class_list':class_list, 'form_details' : create_section_form})
        else:
            return render(request, 'createsection.html', {'class_list':class_list})
    except Exception as e:
        class_list = Classes.objects.all()
        return render(request, 'createsection.html', { 'error' : e, 'class_list':class_list})



@login_required
def list_section(request):
    try:
        section_list = Section.objects.select_related('classes').all()
        paginator = Paginator(section_list, 10)
        page = request.GET.get('page')
        section_details = paginator.get_page(page)
        return render(request, 'sectionlist.html', {'section_list': section_details})
    except Exception as e:
        return render(request, 'classlist.html', { 'error' : e})
    except ValueError:
        raise Http404



@login_required
def delete_section(request):
    try:
        if request.method == 'POST':
            if request.POST.get('section_id') is not None:
                try:
                    section_exists = Section.objects.get(pk=request.POST.get('section_id'))
                    section_exists.delete()
                    data = {
                        'success' : 'successfully done.'
                    }
                    return JsonResponse(data)
                except ObjectDoesNotExist:
                    data = {
                        'error' : 'Invalid  section id.'
                    }
                    return JsonResponse(data)
            else:
                data = {
                    'error' : 'section Id required.'
                }
                return JsonResponse(data)
        else:
            data = {
                'error' : 'Unexcepted error ocurred.'
            }
            return JsonResponse(data)
    except Exception as e:
        data = {
            'error' : 'Unexcepted error ocurred.'
        }
        return JsonResponse(data)



@login_required
@csrf_exempt
#error ache
def section_list(request):
    try:
        if request.method == 'POST':
            if request.POST.get('class_id') is not None:
                try:
                    section_list = Section.objects.filter(classes_id=request.POST.get('class_id'))
                    data = serializers.serialize("json", section_list, fields=['section_name', 'section_id', 'section_code'])
                    # return JsonResponse(serializers.serialize('json', list(section_list), fields=['section_name', 'section_id', 'section_code']))
                    return HttpResponse(data, content_type='application/json')
                except ObjectDoesNotExist:
                    data = {
                        'error' : 'Invalid class id.'
                    }
                    return JsonResponse(data)
            else:
                data = {
                    'error' : 'Class Id required.'
                }
                return JsonResponse(data)
        else:
            data = {
                'error' : 'Unexcepted error ocurred.'
            }
            return JsonResponse(data)
    except Exception as e:
        data = {
            'e' : e,
            'error' : 'Unexcepted error ocurred.'
        }
        return JsonResponse(data)


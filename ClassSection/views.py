from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .form import CreateClassForm
from .models import Classes
from django.core.paginator import Paginator

# Create your views here.

from django.contrib.auth.decorators import login_required



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
        return render(request, 'createclass.html', { 'error' : e})



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
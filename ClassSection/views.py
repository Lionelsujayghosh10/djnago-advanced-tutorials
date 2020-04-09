from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import CreateClassForm
from .models import Classes

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
        pass
    except Exception as e:
        return render(request, 'createclass.html', { 'error' : e})
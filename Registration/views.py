from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import RegistrationForm
from .models import Users
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.





def registration(request):
    try:
        if request.method == 'POST':
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                Users.objects.create(fname=registration_form.cleaned_data['fname'], email=registration_form.cleaned_data['email'], password=make_password(registration_form.cleaned_data['password']))
                return render(request, 'registration.html', {'success': 'Registration Successfully done. Login Now!'})
            else:
                return render(request, 'registration.html', {'form_details':registration_form, 'form_data': request.POST})
        else:
            return render(request, 'registration.html')
    except Exception as e:
        return HttpResponse(e)

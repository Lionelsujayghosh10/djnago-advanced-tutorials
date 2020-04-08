from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .form import LoginForm
from django.contrib.auth.models import User
from Registration.backends import MyAuthBackend
from django.contrib.auth import authenticate, login
# Create your views here.




def user_login(request):
    try:
        if request.method == 'POST':
            login_form =  LoginForm(request.POST)
            if login_form.is_valid():
                user_status = MyAuthBackend.authenticate(request.POST, login_form.cleaned_data['email'],login_form.cleaned_data['password'])
                if user_status is not None:
                    login(request, user_status, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('create_class')
                else:
                    return render(request, 'login.html', {'error': 'Email or Password not match.', 'form_data' : request.POST})
            else:
                return render(request, 'login.html', {'form_error': login_form, 'form_data' : request.POST})
        else:
            return render(request, 'login.html')
    except Exception as e:
        return HttpResponse(e)

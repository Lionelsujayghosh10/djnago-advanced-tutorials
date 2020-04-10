from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



@login_required
def user_logout(request):
    try:
        logout(request)
        return redirect('user_login')
    except Exception as e:
        print(e)
        raise Http404

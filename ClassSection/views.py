from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from django.contrib.auth.decorators import login_required



@login_required
def create_class(request):
    try:
        if request.method == 'POST':
            pass
        else:
            return render(request, 'createclass.html')
    except Exception as e:
        return HttpResponse(e)
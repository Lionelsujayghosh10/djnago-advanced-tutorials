from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def create_parent(request):
    try:
        if request.method == 'POST':
            pass
        else:
            return render(request, 'parent/createparent.html')
    except Exception as e:
        return HttpResponse(e)




from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings

import magic
import os




@login_required
def create_parent(request):
    try:
        if request.method == 'POST':
            if request.FILES is not None:
                content_type = ('image/png', 'image/jpg', 'image/jpeg')
                max_size = 4*1024*1024
                image_file = request.FILES['parent_image']
                file_type = magic.from_buffer(image_file.file.read(), mime=True)
                if file_type in content_type:
                    if image_file.size < max_size:
                        fs = FileSystemStorage("Images/parent")
                        filename = fs.save(image_file.name, image_file)
                        parent_image = fs.url(filename) 
                    else:
                        return render(request, 'parent/createparent.html', { 'error': 'File must be less than 4MB.' })
                else:
                    return render(request, 'parent/createparent.html', { 'error': 'Invalid image type.' })
                # image_type = request.FILES['image_type']
                # fs = FileSystemStorage("Images/parent")
                # filename = fs.save(image_file.name, image_file)
                # uploaded_url = fs.url(filename) 
                
                return HttpResponse(parent_image)
            else:
                parent_image = NULL
            return HttpResponse(parent_image)
        else:
            return render(request, 'parent/createparent.html')
    except Exception as e:
        return HttpResponse(e)




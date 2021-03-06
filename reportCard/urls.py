"""reportCard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Registration/', include('Registration.urls')),
    path('Login/', include('Login.urls')),
    path('ClassSection/', include('ClassSection.urls')),
    path('Logout/', include('Logout.urls')),
    path('Subject/', include('Subject.urls')),
    path('Student/', include('Student.urls')),
    path('Parent/', include('Parent.urls'))
]

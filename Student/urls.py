from django.urls import path
from . import views



urlpatterns = [
    path('createstudent', views.create_student, name="create_student")
]
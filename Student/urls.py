from django.urls import path
from . import views



urlpatterns = [
    path('createstudent', views.create_student, name="create_student"),
    path('liststudent', views.list_student, name="list_student")
]
from django.urls import path
from . import views






urlpatterns = [
    path('createsubject', views.create_subject, name="create_subject"),
    path('createassignsubject', views.assign_subject, name="assign_subject")
]
from django.urls import path
from . import views






urlpatterns = [
    path('createsubject', views.create_subject, name="create_subject"),
    path('createassignsubject', views.assign_subject, name="assign_subject"),
    path('subjectassignlist', views.assign_subject_list, name="assign_subject_list"),
    path('searchassignsubect', views.search_assign_subject, name="search_assign_subject")
]
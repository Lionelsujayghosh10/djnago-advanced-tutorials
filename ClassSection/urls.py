from django.urls import path
from . import views






urlpatterns = [
    path('createclass', views.create_class, name="create_class"),
    path('listclass', views.list_class, name="list_class"),
    path('deleteclass', views.delete_class, name="delete_class"),
    path('createsection', views.create_section, name="create_section"),
    path('listsection', views.list_section, name="list_section")
]
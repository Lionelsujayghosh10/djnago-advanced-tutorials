from django.urls import path
from . import views






urlpatterns = [
    path('createclass', views.create_class, name="create_class"),
    path('listclass', views.list_class, name="list_class")
]
from django.urls import path
from . import views






urlpatterns = [
    path('createclass', views.create_class, name="create_class")
]
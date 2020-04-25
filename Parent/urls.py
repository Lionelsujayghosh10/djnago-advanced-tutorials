from django.urls import path
from . import views



urlpatterns = [
    path('createparent', views.create_parent, name="create_parent")
]
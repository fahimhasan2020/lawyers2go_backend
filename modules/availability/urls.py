from django.urls import path
from . import views

urlpatterns = [
    path('', views.availability_list_create),
    path('create', views.availability_list_create),
    path('provider', views.provider_availability),
    path('<int:id>', views.availability_list_create),
]

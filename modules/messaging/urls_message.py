from django.urls import path
from . import views

urlpatterns = [
    path('', views.message_list_create),
    path('create', views.message_list_create),
    path('<int:id>', views.message_list_create),
]

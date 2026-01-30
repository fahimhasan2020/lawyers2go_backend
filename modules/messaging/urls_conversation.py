from django.urls import path
from . import views

urlpatterns = [
    path('', views.conversation_list_create),
    path('create', views.conversation_list_create),
    path('<int:id>', views.conversation_list_create),
]

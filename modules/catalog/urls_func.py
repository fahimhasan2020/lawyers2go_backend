from django.urls import path
from . import views

urlpatterns = [
    path('', views.func_list_create),
    path('create', views.func_list_create),
    path('hard-delete/<int:id>', views.func_list_create),
    path('<int:id>', views.func_list_create),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.case_list_create),
    path('create', views.case_list_create),
    path('hard-delete/<int:id>', views.case_list_create),
    path('<int:id>', views.case_list_create),
]

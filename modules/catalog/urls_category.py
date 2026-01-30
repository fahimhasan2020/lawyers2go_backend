from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list_create),
    path('create', views.category_list_create),
    path('hard-delete/<int:id>', views.category_list_create),
    path('<int:id>', views.category_list_create),
]

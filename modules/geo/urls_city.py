from django.urls import path
from . import views

urlpatterns = [
    path('', views.city_list_create),
    path('create', views.city_list_create),
    path('hard-delete/<int:id>', views.city_list_create),
    path('<int:id>', views.city_list_create),
]

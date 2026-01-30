from django.urls import path
from . import views

urlpatterns = [
    path('', views.county_list_create),
    path('create', views.county_list_create),
    path('hard-delete/<int:id>', views.county_list_create),
    path('<int:id>', views.county_list_create),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.package_list_create),
    path('create', views.package_list_create),
    path('<int:id>', views.package_list_create),
]

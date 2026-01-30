from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_list_create),
    path('create', views.country_list_create),
    path('<int:id>', views.country_detail),
]

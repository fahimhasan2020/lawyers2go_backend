from django.urls import path
from . import views

urlpatterns = [
    path('', views.city_rate_list_create),
    path('create', views.city_rate_list_create),
    path('<int:id>', views.city_rate_list_create),
]

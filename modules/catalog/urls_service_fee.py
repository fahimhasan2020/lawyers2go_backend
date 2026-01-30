from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_fee_list_create),
    path('create', views.service_fee_list_create),
    path('charge', views.service_fee_charge),
    path('hard-delete/<int:id>', views.service_fee_list_create),
    path('<int:id>', views.service_fee_list_create),
]

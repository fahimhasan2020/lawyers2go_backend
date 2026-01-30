from django.urls import path
from . import views

urlpatterns = [
    path('create', views.transaction_list_create),
    path('list', views.transaction_list),
    path('details/<int:id>', views.transaction_details),
    path('', views.transaction_list_create),
    path('<int:id>', views.transaction_list_create),
]

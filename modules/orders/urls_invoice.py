from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_list_create),
    path('create', views.invoice_list_create),
    path('hard-delete/<int:id>', views.invoice_list_create),
    path('<int:id>', views.invoice_list_create),
]

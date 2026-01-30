from django.urls import path
from . import views

urlpatterns = [
    path('create', views.order_create),
    path('b2b/create', views.order_b2b_create),
    path('provider', views.provider_orders),
    path('client', views.client_orders),
    path('hard-delete/<int:id>', views.order_detail),
    path('', views.order_list_create),
    path('<int:id>', views.order_detail),
]

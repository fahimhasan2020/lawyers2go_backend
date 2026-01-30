from django.urls import path
from . import views

urlpatterns = [
    path('', views.coupon_list_create),
    path('create', views.coupon_list_create),
    path('<int:id>', views.coupon_list_create),
]

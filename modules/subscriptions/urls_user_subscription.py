from django.urls import path
from . import views

urlpatterns = [
    path('list', views.user_subscription_list),
    path('details/<int:id>', views.user_subscription_details),
]

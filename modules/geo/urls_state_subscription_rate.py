from django.urls import path
from . import views

urlpatterns = [
    path('all', views.state_subscription_rate_list_create),
    path('', views.state_subscription_rate_list_create),
    path('create', views.state_subscription_rate_list_create),
    path('hard-delete/<int:id>', views.state_subscription_rate_list_create),
    path('<int:id>', views.state_subscription_rate_list_create),
]

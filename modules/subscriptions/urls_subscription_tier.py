from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_tier_list_create),
    path('active', views.active_subscription_tier),
    path('active', views.subscription_tier_activation),
    path('provider-view-case', views.provider_view_case),
    path('hard-delete/<int:id>', views.subscription_tier_list_create),
    path('<int:id>', views.subscription_tier_list_create),
]

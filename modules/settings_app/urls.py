from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_setting),
    path('stripe-public-key', views.get_stripe_public_key),
    path('', views.get_single_setting),
    path('<int:id>', views.update_setting),
]

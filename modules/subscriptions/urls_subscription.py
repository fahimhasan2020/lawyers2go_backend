from django.urls import path
from . import views

urlpatterns = [
    path('plan', views.subscription_plan),
    path('on', views.subscription_on),
    path('auto-renewal-off', views.cancel_subscription),
    path('history', views.subscription_history),
    path('billing', views.subscription_billing),
    path('retrieve', views.retrieve_subscription),
    path('resume', views.resume_subscription),
    path('renewal', views.renewal_subscription),
    path('', views.subscription_list_create),
    path('<int:id>', views.subscription_list_create),
]

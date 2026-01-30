from django.urls import path
from . import views

urlpatterns = [
    path('', views.plan_list_create),
    path('provider', views.provider_plan),
    path('city/<int:cityId>', views.plan_by_city),
    path('<int:id>', views.plan_list_create),
]

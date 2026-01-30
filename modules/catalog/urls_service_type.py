from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_type_list),
    path('sub-serviceTypes/', views.sub_service_types),
    path('sub-serviceTypes/<int:id>', views.sub_service_types),
    path('create', views.service_type_detail),
    path('hard-delete/<int:id>', views.service_type_detail),
    path('<int:id>', views.service_type_detail),
]

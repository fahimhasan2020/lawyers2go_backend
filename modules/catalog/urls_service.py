from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list_create),
    path('my-services', views.my_services),
    path('provider-services/<int:id>', views.provider_services),
    path('sub-services/', views.service_list_create),
    path('sub-services/<int:id>', views.service_list_create),
    path('search', views.service_search),
    path('b2b/search', views.b2b_search),
    path('create/', views.service_list_create),
    path('<int:id>', views.service_list_create),
]

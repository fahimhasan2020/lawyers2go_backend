from django.urls import path
from . import views

urlpatterns = [
    path('', views.state_list),
    path('create', views.state_create),
    path('hard-delete/<int:id>', views.state_detail),
    path('<int:id>', views.state_detail),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.notification_list_create),
    path('mark-read', views.mark_read),
    path('<int:id>', views.notification_list_create),
]

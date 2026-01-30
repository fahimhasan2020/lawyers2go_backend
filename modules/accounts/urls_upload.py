from django.urls import path
from . import views_upload

urlpatterns = [
    path('photo', views_upload.upload_photo),
    path('file', views_upload.upload_file),
]

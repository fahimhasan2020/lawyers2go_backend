from django.urls import path
from . import views_auth

urlpatterns = [
    path('register', views_auth.register),
    path('register/app', views_auth.register_app),
    path('login', views_auth.login),
    path('login/facebook', views_auth.facebook_login),
    path('login/google', views_auth.google_login),
    path('login/apple-v2', views_auth.apple_login),
    path('login/apple', views_auth.apple_login_v2),
    path('login/app', views_auth.login_by_app),
    path('login/web-portal', views_auth.web_portal_login),
    path('login/admin', views_auth.admin_login),
]

from django.urls import path
from . import views

urlpatterns = [
    path('create', views.review_list_create),
    path('provider', views.provider_reviews),
    path('provider/reviews-rating', views.provider_reviews_and_rating),
    path('client', views.client_reviews),
    path('', views.review_list_create),
    path('<int:id>', views.review_detail),
]

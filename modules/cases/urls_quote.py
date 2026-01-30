from django.urls import path
from . import views

urlpatterns = [
    path('create', views.quote_list_create),
    path('b2b/create', views.quote_b2b_create),
    path('b2b/provider-send-quote/<int:quoteId>', views.quote_b2b_send),
    path('b2b/provider-rejected-quote/<int:quoteId>', views.quote_b2b_reject),
    path('cases/<int:caseId>', views.quotes_by_case),
    path('provider-send-quote/<int:id>', views.quote_list_create),
    path('provider-rejected-quote/<int:quoteId>', views.quote_list_create),
    path('hard-delete/<int:id>', views.quote_list_create),
    path('', views.quote_list_create),
    path('<int:id>', views.quote_list_create),
]

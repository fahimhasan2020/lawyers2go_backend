"""
URL configuration for lawyers2go API.
Mounts all module APIs under same paths as old Express API.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # API (same prefix as old: /auth, /users, /order, etc.)
    path('auth/', include('modules.accounts.urls_auth')),
    path('role/', include('modules.accounts.urls_role')),
    path('users/', include('modules.accounts.urls_users')),
    path('category/', include('modules.catalog.urls_category')),
    path('function/', include('modules.catalog.urls_func')),
    path('country/', include('modules.geo.urls_country')),
    path('state/', include('modules.geo.urls_state')),
    path('county/', include('modules.geo.urls_county')),
    path('city/', include('modules.geo.urls_city')),
    path('serviceType/', include('modules.catalog.urls_service_type')),
    path('service/', include('modules.catalog.urls_service')),
    path('order/', include('modules.orders.urls_order')),
    path('invoice/', include('modules.orders.urls_invoice')),
    path('transaction/', include('modules.orders.urls_transaction')),
    path('review/', include('modules.reviews.urls')),
    path('notification/', include('modules.notifications.urls')),
    path('conversation/', include('modules.messaging.urls_conversation')),
    path('message/', include('modules.messaging.urls_message')),
    path('upload/', include('modules.accounts.urls_upload')),
    path('availability/', include('modules.availability.urls')),
    path('city-rate/', include('modules.geo.urls_city_rate')),
    path('payment/', include('modules.payments.urls')),
    path('case/', include('modules.cases.urls_case')),
    path('quote/', include('modules.cases.urls_quote')),
    path('plan/', include('modules.subscriptions.urls_plan')),
    path('subscription/', include('modules.subscriptions.urls_subscription')),
    path('contact-us/', include('modules.contact.urls')),
    path('service-fee/', include('modules.catalog.urls_service_fee')),
    path('settings/', include('modules.settings_app.urls')),
    path('state-subscription-rate/', include('modules.geo.urls_state_subscription_rate')),
    path('subscription-tier/', include('modules.subscriptions.urls_subscription_tier')),
    path('packages/', include('modules.subscriptions.urls_package')),
    path('coupons/', include('modules.subscriptions.urls_coupon')),
    path('user-subscription/', include('modules.subscriptions.urls_user_subscription')),
]

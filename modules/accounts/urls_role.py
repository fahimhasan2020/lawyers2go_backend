from django.urls import path
from . import views_role

urlpatterns = [
    path('', views_role.get_all_roles),
    path('system-roles', views_role.system_roles),
    path('create/', views_role.create),
    path('hard-delete/<int:id>', views_role.hard_delete),
    path('<int:id>', views_role.get_single_role),
    path('<int:id>', views_role.update),
    path('<int:id>', views_role.delete),
]

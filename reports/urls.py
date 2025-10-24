from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('create/', views.create_report, name='create_report'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete/<int:pk>/', views.delete_report, name='delete_report'),
]

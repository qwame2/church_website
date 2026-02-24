from django.urls import path
from .views import subscribe
from . import views

urlpatterns = [
    path("", subscribe, name="subscribe"),
    path('admin-login/', views.admin_login, name='admin_login'), 
    path('Admin_Dashboard/', views.dashboard, name='dashboard'),
    path('update_content/<str:page_name>/', views.update_content, name='update_content'),    
    path('clear_subscriptions/', views.clear_subscriptions, name='clear_subscriptions'),  # Add this line
    # Other paths...
]
from django.urls import path
from .views import register_view, login_view, logout_view, game_dashboard, tournaments_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', game_dashboard, name='game_dashboard'),
    path('tournaments/', tournaments_view, name='tournaments'),
]

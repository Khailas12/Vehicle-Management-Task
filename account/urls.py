from django.urls import path
from . import views



urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    
    path('super_admin/', views.super_admin_page, name='super_admin_page'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('user_page/', views.user_page, name='user_page'),
]
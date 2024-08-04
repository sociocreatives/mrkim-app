from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_admin, name='register'),
    path('jobseeker/', views.register_jobseeker, name='jobseeker'),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
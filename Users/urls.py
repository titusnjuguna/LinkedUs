from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.resolvers import URLPattern
from . import views
from .views import  *    
    
    
urlpatterns = [
       
    path('register/',views.register, name="Register"),
    path('login/',auth_views.LoginView.as_view(template_name = 'Users/login.html'),name='Login'),
    path('Logout/',auth_views.LogoutView.as_view(template_name='Users/index.html'), name='Logout'),
    path('profile/', views.Profile, name="Profile_Page"),
    path('Password-reset/',auth_views.PasswordResetView.as_view(template_name='Users/password_reset.html'), name='password_reset'),
    path('Password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='Users/password_reset_done.html'), name='password_reset_done'),
    path('Password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Users/password_reset_confirm.html'), name='password_reset_confirm'),
]
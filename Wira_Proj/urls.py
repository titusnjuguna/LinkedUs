from typing import Pattern
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from Users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Job.urls')),
    path('register/', user_views.register, name='Register'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='Login'),
    path('Logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='Logout'),
    path('profile/', user_views.profile, name='Profile_Page'),
    path('Password-reset/', auth_views.PasswordResetView.as_view(
        template_name='Users/password_reset.html'), name='password_reset'),
    path('Password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='Users/password_reset_done.html'), name='password_reset_done'),
    path('Password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='Users/password_reset_confirm.html'), name='password_reset_confirm'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

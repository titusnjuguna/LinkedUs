from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import  *

urlpatterns = [
    path('', views.home,name='Job-home'),
    path('Job/Apply/<int:pk>', views.ApplyPage ,name= 'apply'),
    path('user/<str:username>', UserJobsListView.as_view(), name="user-Jobs"),
    path('Job/New/',JobCreateView.as_view(), name="Job-create"),
    path('Job/<int:pk>/', JobDetailView.as_view(), name="Job-detail"),
    path('Job/<int:pk>/update/',JobUpdateView.as_view(), name ="update"),
    path('Job/<int:pk>/delete', JobDeleteView.as_view(),name ="Job-delete"),
    path('Job/Search', JobResultView.as_view(), name="search-result"),
    path('Job/<int:pk>/Apply', views.ApplyPage , name= 'apply'),
    path('register/',views.register, name="Register"),
    path('login/',auth_views.LoginView.as_view(template_name = 'Job/login.html'),name='Login'),
    path('Logout/',auth_views.LogoutView.as_view(template_name='Job/index.html'), name='Logout'),
    path('profile/', views.Profile, name="Profile_Page"),
    path('Password-reset/',auth_views.PasswordResetView.as_view(template_name='Job/password_reset.html'), name='password_reset'),
    path('Password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='Job/password_reset_done.html'), name='password_reset_done'),
    path('Password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Job/password_reset_confirm.html'), name='password_reset_confirm'),
    ]
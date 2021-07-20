from django.urls import path
from . import views
from .views import  JobCreateView,JobDetailView,UserJobsListView,JobDeleteView,JobUpdateView,JobResultView
urlpatterns = [
    path('', views.home,name='Job-home'),
    path('user/<str:username>', UserJobsListView.as_view(), name="user-Jobs"),
    path('Job/New/',JobCreateView.as_view(), name="Job-create"),
    path('Job/<int:pk>/', JobDetailView.as_view(), name="Job-detail"),
    path('Job/<int:pk>/update',JobUpdateView.as_view(), name ="Job-update"),
    path('Job/<int:pk>/delete', JobDeleteView.as_view(),name ="Job-delete"),
    path('Job/Search', JobResultView.as_view(), name="search-result")
    ]
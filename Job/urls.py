from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.urls.resolvers import URLPattern
from . import views
from .views import  *
from rest_framework import routers

app_name = 'Job'

"""router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'jobs', views.JobsViewSet)
path('', include(router.urls)),"""

urlpatterns = [
    path('', views.home,name='Job-home'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('Job/Apply/<int:pk>', views.ApplyPage ,name= 'apply'),
    path('user/<str:username>', UserJobsListView.as_view(), name="user-Jobs"),
    path('Job/New/',views.post_job, name="Job-create"),
    path('<int:year>/<int:month>/<int:day>/<slug:job>/',views.job_detail, name="Job-detail"),
    path('Job/<int:pk>/update/',JobUpdateView.as_view(), name ="update"),
    path('Job/<int:pk>/delete', JobDeleteView.as_view(),name ="Job-delete"),
    path('Job/<int:pk>/Apply', views.ApplyPage, name='apply'),
    path('Job/results/', views.search_view, name='search'),
    
    ]

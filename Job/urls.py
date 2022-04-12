from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.urls.resolvers import URLPattern
from rest_framework import routers
from .views import JobUpdateView,JobDeleteView,home,post_job,ApplyPage,job_detail
from .api import views as API_view
app_name = 'Job'

"""router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'jobs', views.JobsViewSet)
path('', include(router.urls)),path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),"""

urlpatterns = [
    path('',home,name='Job-home'),
    path('api/', API_view.api_view,name='api_overview'),
    path('Job-list/',API_view.Job_List, name='JobList'),
    path('Job-detail/<str:pk>/', API_view.Job_details,name='JobDetails'),
    path('Job-create/',API_view.Job_Create, name='JobCreate'),
    
    path('Job/Apply/<int:pk>', ApplyPage ,name= 'apply'),
    path('Job/New/',post_job, name="Job-create"),
    path('<int:year>/<int:month>/<int:day>/<slug:job>/',job_detail, name="Job-detail"),
    path('Job/<int:pk>/update/',JobUpdateView.as_view(), name ="update"),
    path('Job/<int:pk>/delete', JobDeleteView.as_view(),name ="Job-delete"),
   ]

from json.tool import main
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Jobs
from .serializers import JobsSerializers

@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'List':'/job-list/',
        'Detail': '/ job-detail/<str:pk> /',
        'Create': '/job-create/',
        'Update': '/job-update/<str:pk>/',
        'Delete': '/job-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def Job_List(request):
    jobs = Jobs.objects.all()
    serializers = JobsSerializers(jobs,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def Job_details(request,pk):
    jobs= Jobs.objects.get(id=pk)
    serializers = JobsSerializers(jobs, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def Job_Create(request):
    serializers = JobsSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)
   
@api_view(['POST'])
def Job_Update(request,pk):
    jobs= Jobs.objects.get(id=pk)
    serializers = JobsSerializers(instance=jobs,data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def Job_Delete(request,pk):
    jobs= Jobs.objects.get(id=pk)
    jobs.delete()
    return Response("job deleted successfully")


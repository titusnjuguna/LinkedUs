from rest_framework import serializers
from ..models import Jobs


class JobsSerializers(serializers.ModelSerializer):
     class Meta:
        model = Jobs
        fields = ['title', 'author', 'experience',
                  'description', 'Responsibility ', 
                  'qualification', 'job_type', 'salary', 
                  'total_opening', 'location','publish','updated']
          
    

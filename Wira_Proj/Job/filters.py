from .models import Jobs 
import django_filters

class JobFilter(django_filters.FilterSet):
    
    class Meta:
        model = Jobs
        fields = ['location','experience','title']

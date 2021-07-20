from django.http import request , HttpResponse
from django.shortcuts import render,get_object_or_404
#from .filters import JobFilter
from django.views.generic import CreateView,ListView,DetailView,DeleteView
from .models import Jobs
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib import messages

def home(request):
    Job_all = Jobs.objects.raw('select TOP(6) * from Jobs')
    context = {
         'Job_all': Jobs.objects.all()
    }
    return render(request,'Job/index.html',context)
# def multipleSearch(request):
 #   if request.method == 'GET' :
 #       location= request.GET.get('location')
 #       experience = request.GET.get('experience')
 #       title = request.GET.get('title')
  #      JobSearchObj = Jobs.objects.raw('select * from Job_jobs where location ="' +location+'" and experience="'+experience+'" and title="'+title+'"')
  #      return render(request,'Job/search_results.html',{'Jobs':JobSearchObj})
  #  else:
  #      JobObj = Jobs.objects.raw('select * from Job_jobs')
  #      return render(request,'Job/search_results.html',{'Jobs':JobObj})*\


class JobResultView(ListView):
    model = Jobs
    template_name = 'Job/search_results.html'
    def get_queryset(self):
        q = Q()
        query = self.request.GET.get("q")
        if q :
            object_list = Jobs.objects.filter(Q(location_icontains = query) & Q(experience_icontains = query)& Q(title_icontains = query))
            return object_list
       # else:
          #  messages.info(request,'no results found for search')
#class SearchResultList(ListView):
 #   model =Jobs
#    context_object_name = 'Job'
 #   template_name = 'Job/search_results.html'
  #  def get_queryset(self):
 #       query = self.request.GET.get("q")
 #       return Jobs.objects.annotate(search=SearchVector("location","experience","title")).filter(search=query)



class JobsListView(ListView):
    model= Jobs
    template_name= 'Job/index.html'
    context_object_name = 'Job'
    ordering_by = ['-date_posted']
    paginate_by = 6

    #def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
       # context = super().get_context_data(**kwargs)
       # context['filter'] = JobFilter(self.request.GET,queryset = self.get_queryset())
      # return context
#def hup_find(request):
#    search_vector = SearchVector('location', 'experience', 'title')
#    if ('q' in request.GET) and request.GET['q'].strip():
#        query_string=request.GET['q']
#        seens = Jobs.objects.annotate(search=search_vector).filter(search=query_string)
#    return render(request, 'search_results.html', {'seens':seens})






class UserJobsListView(ListView):
    model = Jobs
    template_name = 'Job/user_posts.html'
    context_object_name = 'Job_all'
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username')) 
        return Jobs.objects.filter(author= user).order_by('-date_posted')  

class JobCreateView(LoginRequiredMixin,CreateView):
    model= Jobs
    fields = ['title','summary','description','location','experience','salary']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class JobDetailView(DetailView):
    model = Jobs
class JobUpdateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model= Jobs
    fields = ['title','summary','description','location','experience','salary']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.author:
            return True
        return False        
class JobDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Jobs
    success= '/'
    def test_func(self):
        job = self.get_object()
        if self.request.user == job.author:
            return True
        return False    

def Search_result(request):
    search_vector = SearchVector('location','experience','title')
    
    
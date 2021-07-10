from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SearchForm
from .filters import SearchFilter
from django.views.generic import CreateView,ListView,DetailView
from .models import Jobs

def home(request):

    Job_all = Jobs.objects.raw('select TOP(10) * from Jobs')
    context = {
         'Job_all': Job_all
    }
   
    return render(request,'Job/index.html',context)

def SearchView(request):
    if request.method =="POST":
        title= request.POST.get("title")
        location = request.POST.get("location")
        experience= request.POST.get("experience")
        jobSearchobj = Job.sobjects.raw('select * from Jobs where experience="'+experience+'" and location = "'+location+'" and title="'+title+'"')
        return render(request,'Job/index.html',{'job':jobSearchobj})
    else:
        jobObj = Job.objects.raw('select * from Jobs')
        return render(request , 'Job/index.html',{'Job':jobObj})


#def SearchView(request):
   # if request.method == 'GET':
       # form = SearchForm(request.GET)
      #  if form.is_valid() :
       #     correct_name = form.cleaned_data['correct_name']  
     #       location = form.cleaned_data['location']
    #        industry = form.cleaned_data['industry']
    #        result = Jobs.objects.filter().filter().filter() 
     #       return render(request,'Job/index.html',{'form':form, 'result':result})
   #     else:
    #        form = SearchForm()
     #       return render(request,'Job/index.html',{'form':form})    



#class JobsListView(ListView):
    #model= Jobs
   # template_name= 'Job/index.html'
   # context_object_name = 'Job'
   # paginate_by = 10

    #def get_context_data(self,**kwargs):
     #   context = super(JobsListView,self).get_context_data(**kwargs)
       # context.update({
        #    keyword1:Jobs.objects.all()

       # })

    #def get_querySet(self):
     #   return Jobs.objects.filter(

       # )

class JobCreateView(CreateView):
    model= Jobs
    fields = ['title','description','location','experience','salary']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)



from django.views.generic import CreateView,ListView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate
from rest_framework import  viewsets,permissions
from django.http import request , HttpResponse
from django.contrib.postgres.search import SearchVector
from django.contrib import messages
from django.db.models import Q
from .serializers import *
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login,logout,authenticate



#Company.objects.raw('select TOP(6) * from Company')
def home(request):
    context = {
        'Job_all':Jobs.objects.all()
        }
    return render(request,'Job/index.html',context)

def ApplyPage(request,pk):
    #job = Company.objects.get(id=pk)
    Form = ApplyForm()
    if request.method =='POST':
        Form = ApplyForm(request.POST, request.FILES)
        if Form.is_valid():
            Form.save()
            return redirect('Job-home')
    context = {'form':Form}
    return render(request,'Job/apply.html',context)    




class JobResultView(ListView):
    model = Jobs
    template_name = 'Job/search_results.html'
    def get_queryset(self):
        q = Q()
        query = self.request.GET.get("q")
        if q :
            object_list = Jobs.objects.filter(Q(location_icontains = query) & Q(experience_icontains = query)& Q(title_icontains = query))
            return object_list
 
class JobsListView(ListView):
    model= Jobs
    template_name= 'Job/index.html'
    context_object_name = 'Job'
    ordering_by = ['-date_posted']
    paginate_by = 6

    
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


#API
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = CompanySerializer
    permission_classes= [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =[permissions.IsAuthenticated]

#'django.middleware.csrf.CsrfViewMiddleware',





    """if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfilePicForm(request.POST, request.FILES, instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Account update successful')
            return redirect('Profile')

    else:
        u_form= UserUpdateForm( instance= request.user)
        p_form= ProfilePicForm( instance = request.user.profile) 
        context = {
            'u_form' : u_form ,
            'p_form' : p_form
            }  
    return render(request,'Users/profile.html',context)"""

        

        
        


    
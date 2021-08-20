from django.http import request , HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import CreateView,ListView,DetailView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *

#Company.objects.raw('select TOP(6) * from Company')
def home(request):
    context = {
        'Job_all': Company.objects.all()
        }
    return render(request,'Job/index.html',context)

def ApplyPage(request,pk):
    #job = Company.objects.get(id=pk)
    form = ApplyForm()
    if request.method =='POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Job-home')
    context = {'form':form}
    return render(request,'Job/apply.html',context)    

def register(request):
    if request.method == "POST":
        form =CompRegisterForm(request.POST)
        if form.is_valid():
            currUser= form.save()
            form.data_cleaned.get('Username')
            Company.objects.create(user=currUser,name=currUser.username)
            messages.success(request,"Account created successfully, kindly login")
        return redirect('Login')
    else:
        form = CompRegisterForm()
    return render(request, 'Job/register.html',{'form':form})


@login_required
def Profile(request):
    if request.user.is_authenticated:
        candidates = Candidates.objects.filter(company__name = request.user.username)
        context = {
            'candidates':candidates,
            }
        return render(request,'Job/profile.html',context)
    else:
        return render(request, 'Job/index.html') 





class JobResultView(ListView):
    model = Company
    template_name = 'Job/search_results.html'
    def get_queryset(self):
        q = Q()
        query = self.request.GET.get("q")
        if q :
            object_list = Company.objects.filter(Q(location_icontains = query) & Q(experience_icontains = query)& Q(title_icontains = query))
            return object_list
       

class JobsListView(ListView):
    model= Company
    template_name= 'Job/index.html'
    context_object_name = 'Job'
    ordering_by = ['-date_posted']
    paginate_by = 6

    
class UserJobsListView(ListView):
    model = Company
    template_name = 'Job/user_posts.html'
    context_object_name = 'Job_all'
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username')) 
        return Company.objects.filter(author= user).order_by('-date_posted')  


class JobCreateView(LoginRequiredMixin,CreateView):
    model= Company
    fields = ['title','summary','description','location','experience','salary']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class JobDetailView(DetailView):
    model = Company


class JobUpdateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model= Company
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
    model = Company
    success= '/'
    def test_func(self):
        job = self.get_object()
        if self.request.user == job.author:
            return True
        return False    


# Create your views here.

   

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

        

        
        


    
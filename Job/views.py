from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions
from django.http import request, HttpResponse
from django.contrib.postgres.search import SearchVector
from django.contrib import messages
from django.db.models import Q
from .serializers import *
from .forms import *
from .models import Jobs
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate



def home(request):
    job_list = Jobs.published.all()
    search_job = SearchForm()

    return render(request, 'Job/index.html', {'job_list': job_list, 'search_job': search_job})


def ApplyPage(request):
    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Job-home')
    context = {'form': form}
    return render(request, 'Job/apply.html', context)


def job_detail(request, year, month, day, job):
    job = get_object_or_404(Jobs, slug=job,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    App_form = ApplyForm()
    if request.method == 'POST':
        App_form = ApplyForm(request.FILES, data=request.POST)
        if App_form.is_valid():
            App_form.save()
            return redirect('Job-home')

    return render(request, 'Job/Job_detail.html',
                  {'job': job, 'App_form': App_form})


def search_view(request):
    search_job = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        search_job = SearchForm(request.GET)
        if search_job.is_valid():
            query = search_job.cleaned_data['query']
            results = Jobs.published.annotate(
                search=SearchVector('location', 'experience', 'title'),).filter(search=query)
    return render(request, 'Job/search_results.html', {'query': query, 'results': results})





class JobsListView(ListView):
    model = Jobs
    template_name = 'Job/index.html'
    context_object_name = 'Job'
    ordering_by = ['-date_posted']
    paginate_by = 6


class UserJobsListView(ListView):
    model = Jobs
    template_name = 'Job/user_posts.html'
    context_object_name = 'Job_all'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Jobs.objects.filter(author=user).order_by('-date_posted')


"""
 class JobCreateView(LoginRequiredMixin, CreateView):
    model = Jobs
    fields = ['title', 'description','location', 'experience', 'salary']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)"""


def post_job(request):
    if request.method == 'POST':
        post_form = JobCreateForm(request.POST)
        if post_form.is_valid:
            post_form.save()
            return redirect('Job-detail')
    else:
        post_form = JobCreateForm()
    return render(request, 'Job/jobs_form.html', {'post_form': post_form})


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Jobs
    fields = ['title', 'summary', 'description',
              'location', 'experience', 'salary']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.author:
            return True
        return False


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Jobs
    success = '/'

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.author:
            return True
        return False


"""class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]"""

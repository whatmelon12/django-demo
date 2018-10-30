import csv

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import render, get_list_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .resources import UserResource, JobResource
from .models import Job, User, Ints

# Create your views here.
@login_required
class UserIndexView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'users'
    model = User
    paginate_by = 10

@login_required    
class JobIndexView(generic.ListView):
    template_name = 'job/index.html'
    context_object_name = 'jobs'
    model = Job
    paginate_by = 10

@login_required
def homeView(request):
    return render(request, 'authentication/index.html')

def loginView(request, newContext=None):
    return render(request, 'authentication/login.html', newContext)

def login(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return homeView(request)
    else:
        loginView(request, { error_message: True })

def logout(request):
    logout(request)

# Streaming csv file
@login_required
def export(request, model):
    if model == 'users':
        resource = UserResource()
    elif model == 'jobs':
        resource = JobResource()
    else: return None

    dataset = resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(model)
    return response
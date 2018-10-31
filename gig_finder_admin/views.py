import csv

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .resources import UserResource, JobResource
from .models import Job, User, Ints

# Create your views here.
class UserIndexView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'users'
    model = User
    paginate_by = 10
   
class JobIndexView(generic.ListView):
    template_name = 'job/index.html'
    context_object_name = 'jobs'
    model = Job
    paginate_by = 10

@login_required
def home_view(request):
    return render(request, 'home/index.html')

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
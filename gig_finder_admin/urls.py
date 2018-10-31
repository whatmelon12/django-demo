from django.urls import  path, include
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'gigFinderAdmin'
urlpatterns = [
    path('home/', views.home_view, name='homeIndex'),
    path('users/', login_required(views.UserIndexView.as_view()), name='userIndex'),    
    path('jobs/', login_required(views.JobIndexView.as_view()), name='jobIndex'),
    path('<str:model>/download/', views.export, name='modelExport')
]
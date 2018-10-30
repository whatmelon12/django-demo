from django.urls import  path
from . import views

app_name = 'gigFinderAdmin'
urlpatterns = [
    path('home/', views.homeView, name='homeIndex'),
    path('users/', views.UserIndexView.as_view(), name='userIndex'),    
    path('jobs/', views.JobIndexView.as_view(), name='jobIndex'),
    path('<str:model>/download/', views.export, name='modelExport'),
    path('login/', views.loginView, name="adminLogin"),
    path('logout/', views.logout, name="logout"),
    path('login/authenticate/', views.login, name="login")
]
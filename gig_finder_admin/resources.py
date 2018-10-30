from import_export import resources
from .models import User, Job

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class JobResource(resources.ModelResource):
    class Meta:
        model = Job
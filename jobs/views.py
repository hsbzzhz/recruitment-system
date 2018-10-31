from rest_framework import viewsets, mixins, permissions
#from django.contrib.auth.models import User
from jobs.models import Company,Category,Job,Applicant
from jobs.serializers import CompanySerializer,CategorySerializer,JobSerializer, ApplicantSerializer

from jobs.filter import JobFilter

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    #filter function initialize
    #filter_backends = (DjangoFilterBackend,)
    filter_class = JobFilter


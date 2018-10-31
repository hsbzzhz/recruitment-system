from rest_framework import viewsets, mixins, permissions
#import the custome user model using get_user_model
from django.contrib.auth import get_user_model
from users.models import StudentProfile, CompanyProfile, Policy, Skill, Transcript, Education,Wh,Interest, SkillTest
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication
from users.serializers import UserSerializer, StudentProfileSerializer, CompanyProfileSerializer, PolicySerializer, SkillSerializer, TranscriptSerializer, EducationSerializer,WhSerializer, InterestSerializer, SkillTestSerializer
from users.permissions import (
    IsOwnerOrReadOnly, IsAdminUserOrReadOnly, IsSameUserAllowEditionOrReadOnly
)


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsSameUserAllowEditionOrReadOnly,)


class StudentProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """

    serializer_class = StudentProfileSerializer
    queryset = StudentProfile.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

class CompanyProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class SkillViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)

class TranscriptViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Transcript.objects.all()
    serializer_class = TranscriptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)

class EducationViewSet(viewsets.ModelViewSet):

    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)


class WhViewSet(viewsets.ModelViewSet):

    queryset = Wh.objects.all()
    serializer_class = WhSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)


class InterestViewSet(viewsets.ModelViewSet):


    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)

class SkillTestViewSet(viewsets.ModelViewSet):


    queryset = SkillTest.objects.all()
    serializer_class = SkillTestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)

class PolicyViewSet(viewsets.ModelViewSet):


    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)

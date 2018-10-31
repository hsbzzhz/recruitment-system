from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from users import views



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'studentprofiles', views.StudentProfileViewSet)
router.register(r'companyprofiles', views.CompanyProfileViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'transcripts', views.TranscriptViewSet)
router.register(r'educations', views.EducationViewSet)
router.register(r'whs', views.WhViewSet)
router.register(r'skill_test', views.SkillTestViewSet)
router.register(r'interests', views.InterestViewSet)
router.register(r'policies', views.PolicyViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]

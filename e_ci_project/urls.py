from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token


# import the media path
from django.views.static import serve
from e_ci_project.settings import MEDIA_ROOT



# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [

    # add urls for two apps
    url(r'^users/', include('users.urls')),
    url(r'^jobs/', include('jobs.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token, name='api-token-auth'),
    # define the file path to url
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),

]

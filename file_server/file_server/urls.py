"""file_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.conf.urls import url
# from django.conf.urls import url,include
# from django.contrib import admin
# from django.urls import path
# from rest_framework import routers
# from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework.urlpatterns import format_suffix_patterns
# from file import views
# from file.views import(
#     FileUploaderViewSet,
#     )
#
# # router = routers.DefaultRouter()
# # router.register(r'upload', views.FileUploaderViewSet)
#
# urlpatterns = [
#     path(r'^admin/', admin.site.urls),
#     path('upload/', include('file.urls')),
#
#     # url(r'^', include(router.urls)),
#     # url(r'^upload/$',FileUploaderViewSet.as_view()),
#
# ]
#
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload', include('file.urls')),
    path('notificate', include('detection.urls')),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
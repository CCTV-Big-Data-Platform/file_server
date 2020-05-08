# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from file import views
#
# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('file', views.upload_file, name='upload_file'),
# ]

from django.urls import path
from .views import *

urlpatterns = [
    path('', FileUploadView.as_view())
]
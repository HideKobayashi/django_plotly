from django.urls import path
from . import views

urlpatterns = [
    path("", views.FileDownloadView.as_view(), name="filedownload"),
    path("download/", views.FileDownloadView.as_view(), name="download"),
]

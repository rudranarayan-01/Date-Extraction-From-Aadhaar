from django.urls import path
from .views import upload_aadhar

urlpatterns = [
    path("upload/", upload_aadhar, name="upload_aadhar"),
]

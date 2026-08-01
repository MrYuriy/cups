from django.urls import path

from . import views

app_name = "firmware"

urlpatterns = [
    # /api/firmware/label/download/  та  /api/firmware/stock/download/
    path("<str:device_type>/download/", views.firmware_download, name="download"),
]

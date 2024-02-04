from django.urls import path
from .views import LabelListView, my_view

urlpatterns = [
    path("labels/", LabelListView.as_view(), name="labels"),
    path("my-url/", my_view, name='my-url-name'),
]
app_name = "label"

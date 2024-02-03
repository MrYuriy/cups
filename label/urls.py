from django.urls import path
from .views import LabelListView

urlpatterns = [
    path("labels/", LabelListView.as_view(), name="labels"),
]
app_name = "label"

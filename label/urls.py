from django.urls import path
from .views import LabelListView, reprint_label ,my_view

urlpatterns = [
    path("labels/", LabelListView.as_view(), name="labels"),
    path("labels/reprint/", reprint_label, name="label_reprint"),
    path("my-url/", my_view, name='my-url-name'),
]
app_name = "label"

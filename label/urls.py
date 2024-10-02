from django.urls import path
from .views import LabelListView, LabelStockListView, reprint_label ,my_view

urlpatterns = [
    path("labels/", LabelListView.as_view(), name="labels"),
    path("labels/reprint/", reprint_label, name="label_reprint"),
    path("labels-stock/", LabelStockListView.as_view(), name="labels_stock"),
    path("labels-stock/reprint/", reprint_label, name="label_stock_reprint"),
    path("my-url/", my_view, name='my-url-name'),
]
app_name = "label"

from django.urls import path
from .views import (
    LabelListView,
    LabelStockListView,
    ReturnLabelListView,
    my_view,
    reprint_label,
    reprint_return_labels,
)

urlpatterns = [
    path("labels/", LabelListView.as_view(), name="labels"),
    path("labels/reprint/", reprint_label, name="label_reprint"),
    path("labels-stock/", LabelStockListView.as_view(), name="labels_stock"),
    path("labels-stock/reprint/", reprint_label, name="label_stock_reprint"),
    path("labels-returns/", ReturnLabelListView.as_view(), name="labels_returns"),
    path("labels-returns/reprint/", reprint_return_labels, name="labels_returns_reprint"),
    path("my-url/", my_view, name='my-url-name'),
]
app_name = "label"

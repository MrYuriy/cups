from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Label, LabelStock, ReturnLabel
from .serializers import LabelSerializer, LabelStockSerializer, ReturnLabelSerializer
from .utils import generate_label, generate_label_stock, generate_return_labels
from django.http import JsonResponse
from rest_framework.decorators import api_view
from firmware.services import get_active_version

# Create your view

class LabelListView(APIView):
    def get(self, request):
        label_set = Label.objects.all().filter(print_status__in=[False])

        labels_code=[]
        if label_set:
            labels_code = generate_label(label_set)
            label_set.update(print_status=True)
        response = Response({"label_code":labels_code})
        # OTA: віддати ESP актуальну версію прошивки для типу "label"
        fw_version = get_active_version("label")
        if fw_version:
            response["X-Firmware-Version"] = fw_version
        return response

    def post(self, request):
        serializer = LabelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LabelStockListView(APIView):
    def get(self, request):
        label_set = LabelStock.objects.all().filter(print_status__in=[False])

        labels_code=[]
        if label_set:
            labels_code = generate_label_stock(label_set)
            label_set.update(print_status=True)
        response = Response({"label_code":labels_code})
        # OTA: віддати ESP актуальну версію прошивки для типу "stock"
        fw_version = get_active_version("stock")
        if fw_version:
            response["X-Firmware-Version"] = fw_version
        return response

    def post(self, request):
        serializer = LabelStockSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReturnLabelListView(APIView):
    """Labels for returned orders: the ESP takes what is not printed yet, the CRM posts new ones."""

    def get(self, request):
        label_set = ReturnLabel.objects.all().filter(print_status__in=[False])

        labels_code = []
        if label_set:
            labels_code = generate_return_labels(label_set)
            label_set.update(print_status=True)
        response = Response({"label_code": labels_code})
        fw_version = get_active_version("label")
        if fw_version:
            response["X-Firmware-Version"] = fw_version
        return response

    def post(self, request):
        # The CRM sends one record per kind of goods (intact / damaged).
        serializer = ReturnLabelSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reprint_return_labels(request):
    """Print a return's labels again: oh_number of the order, optionally one kind only."""
    labels = ReturnLabel.objects.filter(oh_number=request.data.get("oh_number"))
    kind = request.data.get("kind")
    if kind:
        labels = labels.filter(kind=kind)
    if not labels:
        return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)
    labels.update(print_status=False)
    return Response({"labels": labels.count()}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def reprint_label(request):
    identifier = request.data.get("identifier")
    exsist_label = Label.objects.filter(identifier=identifier).first()
    if exsist_label:
        exsist_label.print_status = False
        exsist_label.save()
        return Response(status=status.HTTP_201_CREATED)

    serializer = LabelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.print_status = False
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reprint_label_stock(request):
    identifier = request.data.get("identifier")
    exsist_label = LabelStock.objects.filter(identifier=identifier).first()
    if exsist_label:
        exsist_label.print_status = False
        exsist_label.save()
        return Response(status=status.HTTP_201_CREATED)

    serializer = LabelStockSerializer(data=request.data)
    if serializer.is_valid():
        serializer.print_status = False
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def my_view(request):
    # Your view logic here
    data = {
        'key1': 'value1',
        'key2': 'value2',
    }
    return JsonResponse(data)
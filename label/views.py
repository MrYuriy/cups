from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Label, LabelStock
from .serializers import LabelSerializer, LabelStockSerializer
from .utils import generate_label, generate_label_stock
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your view

class LabelListView(APIView):
    def get(self, request):
        label_set = Label.objects.all().filter(print_status__in=[False])

        labels_code=[]
        if label_set:
            labels_code = generate_label(label_set)
            label_set.update(print_status=True)
        return Response({"label_code":labels_code})

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
        return Response({"label_code":labels_code})

    def post(self, request):
        serializer = LabelStockSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
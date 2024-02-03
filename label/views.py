from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Label
from .serializers import LabelSerializer
from .utils import generate_label

# Create your view

class LabelListView(APIView):
    def get(self, request):
        label = Label.objects.all().filter(print_status=False)[0]
        label.print_status = True
        #label.save()
        serializer = LabelSerializer(label)
        label_code = generate_label(label)
        #return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"label_code":label_code})

    def post(self, request):
        serializer = LabelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


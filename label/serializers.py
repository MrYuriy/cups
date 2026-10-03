from rest_framework import serializers
from .models import Label, LabelStock, ReturnLabel

class LabelSerializer(serializers.ModelSerializer):
    print_status = serializers.BooleanField(read_only=True)
    class Meta:
        model = Label
        fields = "__all__"

class LabelStockSerializer(serializers.ModelSerializer):
    print_status = serializers.BooleanField(read_only=True)
    class Meta:
        model = LabelStock
        fields = "__all__"

class ReturnLabelSerializer(serializers.ModelSerializer):
    print_status = serializers.BooleanField(read_only=True)
    class Meta:
        model = ReturnLabel
        fields = "__all__"

from rest_framework import serializers
from .models import Label

class LabelSerializer(serializers.ModelSerializer):
    print_status = serializers.BooleanField(read_only=True)
    class Meta:
        model = Label
        fields = "__all__"

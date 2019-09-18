from .models import DetectionRequest, DetectionResult
from rest_framework import serializers

class DetectionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetectionRequest
        fields = "__all__"
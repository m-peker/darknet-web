from django.utils import timezone
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import DetectionRequestSerializer
from detections.models import DetectionRequest
from yolopy.yolo import YoloNetwork

class RunDetectionView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        request.data['created_time'] = timezone.now()
        file_serializer = DetectionRequestSerializer(data=request.data)

        if file_serializer.is_valid():
            network = YoloNetwork.get_instance()

            file_serializer.save()

            print(network.detect_objects(request.data.original_image))

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def start_detections(self):
        pass
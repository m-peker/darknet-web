from django.shortcuts import render
from .models import DetectionRequest

# Create your views here.

def HomeView(request):
    return render(request, 'detections/home.html')

#class NewDetectionView(CreateView):
    #model = DetectionRequest

def DetectionListView(request):
    data = {
        "detections" : DetectionRequest.objects.all()
    }

    return render(request, 'detections/detection_list.html', data)

def NewDetectionView(request):
    return render(request, 'detections/new_detection.html')

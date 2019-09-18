from django.urls import path
from .views import HomeView, NewDetectionView, DetectionListView

app_name = 'detections'

urlpatterns = [
    path('', HomeView, name='home'),
    path('detections', DetectionListView, name='list'),
    path('new_detection', NewDetectionView, name='new')
]

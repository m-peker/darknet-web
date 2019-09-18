from django.urls import path
from .views import RunDetectionView

app_name = 'api'

urlpatterns = [
    path('run_detection', RunDetectionView.as_view(), name='run')
]

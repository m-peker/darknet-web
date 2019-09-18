from django.contrib import admin
from .models import DetectionRequest, DetectionResult, DetectableObject, DetectedObject

@admin.register(DetectionRequest)
class DetectionRequestAdmin(admin.ModelAdmin):
    pass

@admin.register(DetectionResult)
class DetectionResultAdmin(admin.ModelAdmin):
    pass

@admin.register(DetectableObject)
class DetectableObjectAdmin(admin.ModelAdmin):
    pass

@admin.register(DetectedObject)
class DetectedObjectAdmin(admin.ModelAdmin):
    pass
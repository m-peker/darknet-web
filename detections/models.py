from django.db import models

class DetectionRequest(models.Model):
    created_time = models.DateTimeField()
    original_image = models.ImageField(upload_to="images/originals/")

    def __str__(self):
        return f"{self.created_time}"

    class Meta:
        db_table = 'DetectionRequest'
        verbose_name = 'DetectionRequest'
        verbose_name_plural = 'DetectionRequests'

class DetectionResult(models.Model):
    created_time = models.DateTimeField()
    duration = models.IntegerField()
    object_count = models.IntegerField()
    tag_count = models.IntegerField()
    image_width = models.IntegerField()
    image_height = models.IntegerField()
    tagged_image = models.ImageField(upload_to="images/tagged/")
    human_readable = models.CharField(max_length=500)
    detection_request = models.OneToOneField(DetectionRequest, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return f"{self.created_time} ({self.object_count} objects, {self.duration / 100} seconds)"

    class Meta:
        db_table = 'DetectionResponse'
        verbose_name = 'DetectionResponse'
        verbose_name_plural = 'DetectionResponses'

class DetectableObject(models.Model):
    tag = models.CharField(max_length=50, primary_key=True)
    singular = models.CharField(max_length=50)
    plural = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tag} ({self.singular}"

    class Meta:
        db_table = 'DetectableObject'
        verbose_name = 'DetectableObject'
        verbose_name_plural = 'DetectableObjects'
        
class DetectedObject(models.Model):
    POSITION_CHOICES = [
        (0, 'TOP'),
        (0, 'MIDDLE')
    ]

    tag = models.ForeignKey(DetectableObject, on_delete=models.CASCADE)
    accuracy_rate = models.DecimalField(max_digits=22, decimal_places=16)
    x_right = models.DecimalField(max_digits=22, decimal_places=16)
    x_left = models.DecimalField(max_digits=22, decimal_places=16)
    y_right = models.DecimalField(max_digits=22, decimal_places=16)
    y_left = models.DecimalField(max_digits=22, decimal_places=16)
    #overall_position = models.
    detection = models.ForeignKey(DetectionResult, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tag} ({self.detected_time})"

    class Meta:
        db_table = 'DetectedObject'
        verbose_name = 'DetectedObject'
        verbose_name_plural = 'DetectedObjects'
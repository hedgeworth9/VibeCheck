from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    address = models.TextField()
    notes = models.TextField()
    image = models.ImageField(blank=True, upload_to='user_propery_images')
    price = models.IntegerField(default=0)
    safety = models.IntegerField(default=0)
    convenience = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)
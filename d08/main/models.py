from django.db import models

# Create your models here.
class ImageUpload(models.Model):
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to='uploadedimg/')
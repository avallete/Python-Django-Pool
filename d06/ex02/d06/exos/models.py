from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AUser(AbstractUser):
    pass

class Tip(models.Model):
    content = models.TextField()
    auteur = models.ForeignKey(AUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, editable=False)
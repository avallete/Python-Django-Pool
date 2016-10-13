from .models import ImageUpload
from django import forms

class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageUpload
        fields = ['title', 'file']
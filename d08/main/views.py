from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from .forms import ImageUploadForm

class HomePage(View):
    form = ImageUploadForm()

    def get(self, request):
        return render(request, 'main/homepage.html', {'form': self.form})
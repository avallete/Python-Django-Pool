from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from .forms import ImageUploadForm

class HomePage(View):
    form = ImageUploadForm

    def get(self, request):
        f = self.form(request.POST)
        return render(request, 'main/homepage.html', {'form': f})

    def post(self, request):
        f = self.form(request.POST)
        try:
            if f.is_valid():
                f.save()
            print("Form is valid: %s" % request.POST)
            return redirect('/')
        except ValueError as e:
            print("An error occured")
            print(e)
            return render(request, 'main/homepage.html', {'form': f})
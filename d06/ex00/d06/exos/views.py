import datetime
from random import choice
from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.

def main(request):
    response = render(request, 'exos/base.html')
    if not request.COOKIES.get('username'):
        random_user = choice(settings.USER_POOL)
        request.COOKIES['username'] = random_user
        response = render(request, 'exos/base.html')
        response.set_cookie('username', random_user, max_age=42)
    return response

import requests
import uuid
from django.shortcuts import render

# Create your views here.
def index(request):
    user_uuid = request.COOKIES.get('user_uuid')
    response = render(request, 'objectives/index.html')
    if(user_uuid is None):
        response.set_cookie('user_uuid', uuid.uuid4(), max_age=60*60*24*365)  # 1 year
    return response
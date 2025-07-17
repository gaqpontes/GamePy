
import json
import requests
import base64

from django.shortcuts import render
from django.http import HttpResponse

from .forms import UploadFileForm
from .helpers.gemini import GEMINI_URL, GEMINI_HEADERS, REQUEST_CONFIG

class Output:
    result: str
# Create your views here.
def index(request):
    if(request.method == "POST"):
        form = UploadFileForm(request.POST, request.FILES);
        if(form.is_valid):
            picture = request.FILES["picture"];
            encoded_picture = base64.b64encode(picture.read()).decode("ASCII")
            final_request = REQUEST_CONFIG.replace('{$REPLACE_BASE64}', encoded_picture)
            response = requests.post(GEMINI_URL, headers=GEMINI_HEADERS, data=final_request)
            print(response.text)

    result = {
        "success": True,
        "result": response.text
    }
    return HttpResponse(json.dumps(result), content_type='application/json');


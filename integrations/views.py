
import json
import requests
import base64

from django.shortcuts import render
from django.http import HttpResponse

from .forms import UploadFileForm
from .helpers.gemini import GEMINI_URL, GEMINI_HEADERS, REQUEST_CONFIG
from objectives.models import Objective
class Output:
    result: str
# Create your views here.
def index(request):
    user_uuid = request.COOKIES.get('user_uuid')
    response = ''
    
    if(request.method == "POST"):
        
        form = UploadFileForm(request.POST, request.FILES);
        if(form.is_valid()):
            
            picture = request.FILES["picture"];
            encoded_picture = base64.b64encode(picture.read()).decode("ASCII")
            final_request = REQUEST_CONFIG.replace('{$REPLACE_BASE64}', encoded_picture).replace('{$REPLACE_TEXT}', form.cleaned_data['helper_text'])
            response = requests.post(GEMINI_URL, headers=GEMINI_HEADERS, data=final_request).text
            response_parts = json.loads(json.loads(response)['candidates'][0]['content']['parts'][0]['text'])
            objective_list = []
            
            for suggested_objective in response_parts:
            
                objective = Objective(
                    title=suggested_objective['objective'],
                    points=suggested_objective['rewards'],
                    owner=user_uuid
                )
                print(objective)
                objective_list.append(objective)
            
            Objective.objects.bulk_create(objective_list)

    result = {
        "success": True,
        "result": response
    }
    return HttpResponse(json.dumps(result), content_type='application/json');


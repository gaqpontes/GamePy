import uuid, json
 
from django.http import HttpResponse
from django.shortcuts import render

from .models import Objective

# Create your views here.
def index(request):
    user_uuid = request.COOKIES.get('user_uuid')
    
    if(user_uuid is None):
        user_uuid = str(uuid.uuid4());
    
    objectives = Objective.objects.filter(owner=user_uuid).order_by('-created_at')
    context_data = {}
    context_data['objectives'] = objectives
    context_data['user_uuid'] = user_uuid

    response = render(request, 'objectives/index.html', context=context_data)
    response.set_cookie('user_uuid', user_uuid, max_age=60*60*24*365)  # 1 year

    return response


def complete_objective(request, objective_id):
    user_uuid = request.COOKIES.get('user_uuid')
    objective = Objective.objects.filter(uuid=objective_id, owner=user_uuid)
    
    if(objective.count() == 0):
        return HttpResponse(status=404)
    
    request_body = json.loads(request.body.decode('utf-8'))
    status = request_body['completed']
    
    if status not in [True, False]:
        return HttpResponse(status=400)
    
    objective.update(completed=status)
    return HttpResponse(status=204) 

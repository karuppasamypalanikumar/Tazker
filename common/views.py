from django.shortcuts import render
import json
from django.http import JsonResponse

def index_page(request):
    return render(
        request=request,
        template_name='common/index.html'
    )

def health_check(request):
    data = {
        'status': True,
        'message': 'Connected to the Server'
    }
    return JsonResponse(
        data=data
    )
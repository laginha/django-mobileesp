# Create your views here.
from django.http import HttpResponse
from django.conf import settings

def home(request):
    for i in getattr(settings, 'DETECT_USER_AGENTS', {}).keys():
        print i, getattr(request, i)
    return HttpResponse('success')

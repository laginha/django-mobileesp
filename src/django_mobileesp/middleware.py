from django.conf import settings
from django.utils.functional import SimpleLazyObject

DETECT_USER_AGENTS = getattr(settings, 'DETECT_USER_AGENTS', {})

def lazy_detection(request, key):
    detector = DETECT_USER_AGENTS[key]
    return SimpleLazyObject( lambda: detector(request) )


class UserAgentDetectionMiddleware(object):
    """
    Middleware to detect request's user agent
    """
    def process_request(self, request):
        for each in DETECT_USER_AGENTS:
            setattr( request, each, lazy_detection(request, each) )


from django.conf import settings
DETECT_USER_AGENTS = getattr(settings, 'DETECT_USER_AGENTS', {})

class UserAgentDetectionMiddleware(object):
    """
    Middleware to detect request's user agent
    """
    def process_request(self, request):
        for k,v in DETECT_USER_AGENTS.iteritems():
            setattr(request, k, v(request))


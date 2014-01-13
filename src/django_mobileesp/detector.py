import mdetect

def is_browser(request):
    agent = request.META.get('HTTP_USER_AGENT') or ''
    return agent.startswith('Mozilla/')    

def is_server(request):
    return not is_browser( request )


class Detector(object):
    def __init__(self, first, other=False, op='or', detect=None):
        self.first  = first
        self.other  = other
        self.op     = op
        self.detect = detect or self.mobileesp
        
    def __call__(self, request):
        return self.detect( request )
        
    def __or__(self, other):
        return Detector( self, other, 'or' )
    
    def __and__(self, other):
        return Detector( self, other, 'and' )
        
    def __str__(self):
        return "(%s %s %s)" %(self.first, self.op, self.other)
        
    def mobileesp(self, request):
        
        def get_agent():
            user_agent  = request.META.get("HTTP_USER_AGENT")
            http_accept = request.META.get("HTTP_ACCEPT")
            return mdetect.UAgentInfo(userAgent=user_agent, httpAccept=http_accept)
            
        def get_result(el):
            return getattr(agent, el)() if isinstance(el, str) else el(request)
              
        agent = get_agent()
        if self.other:
            if self.op == "or":
                return get_result( self.first ) or get_result( self.other )
            return get_result( self.first ) and get_result( self.other )
        return get_result( self.first )
        

class UserAgent(object): 
    def __getattr__(self, name):
        if name == 'detectBrowser':
            return Detector( name, detect=is_browser )
        elif name == 'detectServer':
            return Detector( name, detect=is_server )
        return Detector( name )


class PythonicWrapper(object):
    def __init__(self, agent):
        self.agent = agent
        
    def __getattr__(self, name):
        split = name.split('_')
        name = ''.join( [i[0].upper()+i[1:] for i in split[1:]] )
        return getattr(self.agent, split[0]+name)


mobileesp_agent = UserAgent()        
python_agent = PythonicWrapper(mobileesp_agent)

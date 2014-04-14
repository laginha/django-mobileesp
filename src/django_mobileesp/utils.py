import mdetect


def get_user_agent_info(request):
    user_agent  = request.META.get("HTTP_USER_AGENT")
    http_accept = request.META.get("HTTP_ACCEPT")
    return mdetect.UAgentInfo(userAgent=user_agent, httpAccept=http_accept)
    

def is_browser_agent(request):
    agent = request.META.get('HTTP_USER_AGENT') or ''
    return agent.startswith('Mozilla/')    

def is_server_agent(request):
    return not is_browser( request )

def is_tablet_agent(request):
    return get_user_agent_info( request ).detectTierTablet()

def is_smartphone_agent(request):
    return get_user_agent_info( request ).detectTierIphone()

def is_mobile_agent(request):
    agent = get_user_agent_info( request )
    tablet     = agent.detectTierTablet()
    smartphone = agent.detectTierIphone()
    other      = agent.detectMobileQuick()
    return tablet or other or smartphone

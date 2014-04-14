# Django Mobileesp

Detect request's mobile user agents using the [mobileesp](http://blog.mobileesp.com/) lib. 

This is an alternative to [django-user_agents](https://github.com/selwin/django-user_agents) project. 


## Install

    pip install git+https://github.com/laginha/django-mobileesp/

## Usage

Add to your `settings.py`:

```python
MIDDLEWARE_CLASSES = (
    ...
    'django_mobileesp.middleware.UserAgentDetectionMiddleware'
)

from django_mobileesp.detector import mobileesp_agent as agent

DETECT_USER_AGENTS = {
    'is_android': agent.detectAndroid,
    'is_ios': agent.detectIos,
    'is_windows_phone': agent.detectWindowsPhone,
    'is_mobile': agent.detectTierTablet | \
                 agent.detectTierIphone | \
                 agent.detectMobileQuick,
}
```

Adapt the `DETECT_USER_AGENTS` to your needs:

- _Key_: name of attribute to add to each request instance. 
- _Value_: bounded method to be invocked on each request by `UserAgentDetectionMiddleware`. 
    - Can be combined with `&`(AND) and `|`(OR) operands. 
    - Read the [mobileesp docs](http://blog.mobileesp.com/?page_id=53) to check all the available methods.

If you prefer more pythonic methods, you can user a wrapper agent as follows:

```python
from django_mobileesp.detector import python_agent as agent

DETECT_USER_AGENTS = {
    'is_android': agent.detect_android,
    'is_ios': agent.detect_ios,
    'is_windows_phone': agent.detect_windows_phone,
    'is_mobile': agent.detect_tier_tablet | \
                 agent.detect_tier_iphone | \
                 agent.detect_mobile_quick,
}
```

Finally access the defined attributes in your views:

```python
def view(request):
    if request.is_mobile:
        ...
```

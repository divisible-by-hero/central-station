import urllib, hashlib
from django import template

register = template.Library()

@register.inclusion_tag('templatetags/gravatar.html')
def show_gravatar(email, size=48):
    default = "http://www.mysite.com/media/images/no-avatar.gif"

    url = "http://www.gravatar.com/avatar.php?"
    url += urllib.urlencode({
        'gravatar_id': hashlib.md5(email).hexdigest(),
        'default': default,
        'size': str(size)
    })

    return {'gravatar': {'url': url, 'size': size}}

@register.inclusion_tag('templatetags/get_gravatar.html')
def get_gravatar(email, size=48):
    default = "http://www.mysite.com/media/images/no-avatar.gif"
    
    url = "http://www.gravatar.com/avatar.php?"
    url += urllib.urlencode({
        'gravatar_id': hashlib.md5(email).hexdigest(),
        'default': default,
        'size': str(size)
    })
    return {'gravatar': {'url': url, 'size': size}}
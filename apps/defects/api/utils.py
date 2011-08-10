from piston.utils import *

'''
These methods are quick helpers that check for the existence of keys, make sure they are valid, and return errors
'''

def key_required_error():
    resp = rc.BAD_REQUEST
    resp.write(" An API Key is required for this method.")
    return resp

def key_incorrect_error():
    resp = rc.FORBIDDEN
    resp.write(" API Key is incorrect.")
    return resp

def key_exists(attrs):
    if "key" not in attrs:
        return False
    else:
        return True

def key_check(attrs):
    keys = Keys.objects.active()
    for key in keys:
        if attrs['key'] == key.key:
            return True
    else:
        return False

def log_use(key, str_object, object_id, action):
    key = Keys.objects.get(key=key)
    usage_log = KeyUsage(key=key, log_message='%s - ID %d was %s' % (str_object, object_id, action,))
    usage_log.save()
    return True
    
    
    
from piston.resource import Resource

class CsrfExemptResource(Resource):
    def __init__(self, handler, authentication=None):
        super(CsrfExemptResource, self).__init__(handler, authentication)
        self.csrf_exempt = getattr(self.handler, 'csrf_exempt', True)
__author__ = 'Derek Stegelman'
__date__ = '10/19/12'


class IdentifyOrg(object):

    def process_request(self, request):
        org = request.session.get('current_organization', None)
        if not org:
            request.session['current_organization'] = 'k-state'
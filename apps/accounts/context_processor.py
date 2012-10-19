__author__ = 'Derek Stegelman'
__date__ = '10/19/12'

from accounts.models import RoleAssigned

def accounts(request):
    teams = RoleAssigned.objects.filter(user=request.user)
    context = {'teams': teams, 'account_slug': request.session.get('account_slug')}
    return context
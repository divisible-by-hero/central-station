__author__ = 'Derek Stegelman'
__date__ = '9/6/12'

from django.contrib import admin

from accounts.models import Team, Account, Role, RoleAssigned

admin.site.register(Team)
admin.site.register(Account)
admin.site.register(Role)
admin.site.register(RoleAssigned)
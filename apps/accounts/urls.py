__author__ = 'Derek Stegelman'
__date__ = '9/5/12'


from django.conf.urls import patterns, url
from accounts.views import registration

urlpatterns = patterns('',
    url(r'^registration/$', registration, name="account_registration"),


)

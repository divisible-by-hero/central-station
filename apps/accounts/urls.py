__author__ = 'Derek Stegelman'
__date__ = '9/5/12'


from django.conf.urls import patterns, url
from accounts.views import registration, account_home

urlpatterns = patterns('',
    url(r'^$', account_home, name='account_home'),
    url(r'^registration/$', registration, name="account_registration"),


)

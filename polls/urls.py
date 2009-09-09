from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'polls.views.index', name='polls_index'),
    url(r'^create/$', 'polls.views.create', name='polls_create'),
    url(r'^(?P<poll_id>\d+)/$', 'polls.views.detail', name='polls_detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'polls.views.results', name='polls_results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote', name='polls_vote'),
)

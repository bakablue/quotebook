from django.conf.urls import include, url

from . import views

urlpatterns = [
        url(r'^(?P<page_index>[0-9]+)?$', views.index, name='index'),
        url(r'^add/$', views.add, name='add'),
        url(r'^login/$', views.connect, name='login'),
        url(r'^signup/$', views.signup, name='signup'),
        url(r'^logout/$', views.disconnect, name='logout'),
        url(r'^vote/(?P<quote_id>[0-9]+)/',
            include([
                     url(r'^like/$', views.vote, { 'vote_type' : 'like' }, name='vote'),
                     url(r'^hate/$', views.vote, { 'vote_type' : 'hate' }, name='vote'),
                    ])),
        ]

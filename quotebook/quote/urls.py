from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^(?P<page_index>[0-9]+)?$', views.index, name='index'),
        url(r'^add/', views.add, name='add'),
        ]

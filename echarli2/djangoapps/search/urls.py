from __future__ import absolute_import, unicode_literals
from django.conf.urls import patterns, url
from . import views
urlpatterns = [
    url(
        regex=r'^$',
        view=views.SearchView.as_view(),
        name='main-search'
    ),
]
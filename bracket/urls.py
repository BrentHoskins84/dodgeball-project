from django.conf.urls import url
from django.urls import path
# from .views import BracketView
from . import views

app_name = 'bracket'

urlpatterns = [
    # url(r'^(?P<tournament_id>[0-9]+)/$', views.index, name='tournament'),
    path('', views.index, name='tournament'),
]

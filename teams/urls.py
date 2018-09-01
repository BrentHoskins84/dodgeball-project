from django.urls import path
from .views import *

app_name = 'teams'

urlpatterns = [
    path('', TeamListView.as_view(), name='team-list'),
    path('create-team/', TeamCreateView.as_view(), name='team-create'),
    path ('<int:id>/', TeamDetailView.as_view(), name='team-detail'),

    path('create-player/', PlayerCreateView.as_view(), name='player-create'),
    path('players/', PlayerListView.as_view(), name='player-list'),
    path('private/team-list/', PrivateTeamlistView.as_view(), name='private'),

]

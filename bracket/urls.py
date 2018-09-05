from django.urls import path
from .views import BracketView

app_name = 'teams'

urlpatterns = [
    path('', BracketView.as_view(), name='bracket-list'),
]

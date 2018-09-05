from django.urls import path
from .views import BracketView

app_name = 'teams'

urlpatterns = [
    path('<int:id>/', BracketView, name='bracket-list'),
]

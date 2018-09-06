from django.urls import path
from .views import BracketView

app_name = 'bracket'

urlpatterns = [
    path('', BracketView.as_view(), name='bracket'),
]

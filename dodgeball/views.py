from django.shortcuts import render
from teams.models import Team, Player

def index(request):
    team = Team.objects.all()
    player = Player.objects.all()
    return render(request, 'index.html', {'team': team, 'player': player})

from django.template import loader
from django.http import HttpResponse
from .models import Tournament
from django.db.models import Q
import json

# Create your views here.



def index(request):
    tournament_id = 1
    tournament = Tournament.objects.filter(id=tournament_id).prefetch_related(
        "matches").prefetch_related("teams").get()
    tournament.match_list = tournament.matches.filter(
        ~Q(status="BYE")).order_by("id")
    tournament.player_list = tournament.teams.order_by("rank")
    teams, results = get_bracket_info(tournament)
    template = loader.get_template('bracket.html')
    context = {
        'tournament': tournament,
        'teams':json.dumps(teams),
        'results': json.dumps(results)
    }
    return HttpResponse(template.render(context, request))

def get_bracket_info(tournament):
    results = []
    teams = list(map(lambda x: x.get_player_names(), tournament.matches.filter(match_round=1).order_by('id')))

    for r in range(1, tournament.rounds+1):
        results.append(list(map(lambda x: x.get_result_values(), tournament.matches.filter(match_round=r).order_by('id'))))

    return teams, results

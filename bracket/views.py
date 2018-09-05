from django.template import loader
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from bracket.models import Match, Tournament
from teams.models import Player

from django.http import HttpResponse
import json

# Create your views here.

# class BracketView(ListView):
def BracketView(request, id):
    template = loader.get_template('bracket.html')
    queryset = Match.objects.all()
    tournament = Tournament.objects.filter(id=id).prefetch_related("tournament").get()
    teams, results = get_bracket_info(Match)


    context = {
        'tournament': tournament,
        'teams':json.dumps(teams),
        'results': json.dumps(results)
    }
    return HttpResponse(template.render(context, request))

def get_bracket_info(Match):
    results = []
    teams = list(map(lambda x:x.get_player_names(), Match.objects.filter(round=1).order_by('match_id')))

    for r in range(1, Match.round+1):
        results.append(list(map(lambda x: x.get_result_values(), matches.objects.filter(round=r).order_by('match_id'))))

    return teams, results

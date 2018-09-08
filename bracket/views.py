from django.views.generic import ListView
from bracket.models import Match, Tournament
import json


def get_bracket_info(matches):
    results = []
    teams = list(map(lambda x: x.get_team_names(), matches.filter(match_round=1).order_by('id')))


    for r in range(1, len(matches)):
        results.append(list(map(lambda x: x.get_result_values(), matches.filter(match_round=r).order_by('id'))))

    return teams, results

class BracketView(ListView):
    template_name = 'bracket.html'
    model = Match
    def get_context_data(self, *args, **Kwargs):
        context = super(BracketView, self).get_context_data(*args, **Kwargs)
        tournament = Tournament.objects.all()
        matches = list(Match.objects.all())
        teams, results = get_bracket_info(Match.objects.all())

        context = {
            'tournament': Tournament,
            'teams':json.dumps(teams),
            'results': json.dumps(results)
        }
        return context

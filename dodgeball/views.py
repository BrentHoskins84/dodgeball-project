from django.shortcuts import render
from bracket.models import Team, Player
from django.views.generic import TemplateView

from .charts import NationalityPieChart
from pygal.style import Style

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        custom_style = Style(
            background='transparent',
            opacity_hover='.9',
        )

        cht_nat = NationalityPieChart(
            height=300,
            width=400,
            explicit_size=True,
            style=custom_style
        )

        team = Team.objects.all()
        player = Player.objects.all()

        context= {
            'cht_nat': cht_nat.generate(),
            'team': team,
            'player': player
        }
        return context


class RuleView(TemplateView):
    template_name = 'rules.html'



# def index(request):
#     team = Team.objects.all()
#     player = Player.objects.all()
#
#
#
#     return render(request, 'index.html', {'team': team, 'player': player})

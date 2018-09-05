from django.views.generic import ListView
from bracket.models import Match, Tournament


# Create your views here.
# def replace_none(self):
#     for i in context['match_list']:
#         if self.team_1_score == None:
#             context['match_list'].append()

# class BracketView(ListView):
class BracketView(ListView):
    template_name = 'match_list.html'
    # queryset = Match.objects.all()
    model = Match

    def get_context_data(self, *args, **Kwargs):
        context = super(BracketView, self).get_context_data(*args, **Kwargs)
        context['match_list'] = Match.objects.all()
        return context

from django.contrib import admin
from .models import Team, Tournament, Match
from .utils import genearte_random_string
import math
from datetime import timedelta
from django.contrib import messages

# Register your models here.
def generate_schedules(modeladmin, request, queryset):
    for tournament in queryset:
        tournament.matches.all().delete()
        tournament.save()
        create_schedules(tournament)
        messages.add_message(request, messages.SUCCESS, 'tournament generated for {}.'.format(tournament))

def create_schedules(tournament):
    _team_list = list(tournament.teams.order_by('rank'))
    _len = len(_team_list)
    if _len == 0:
        return
    tournament.rounds = int(math.ceil(math.log(_len, 2)))
    tournament.save()

    _number_of_teams = int(math.pow(2, tournament.rounds))
    _teams = _team_list + ([None]*(_number_of_teams - _len))

    _date = tournament.start_date
    _matches = []
    _counter = 1
    _round = 1
    for i in range(_number_of_teams//2):
        _match = Match()
        _match.tournament = tournament
        _match.match_round = _round
        if _teams[i]:
            _match.team_1 = _teams[i]
        if _teams[-1-i]:
            _match.team_2 = _teams[-1-i]

        if _match.team_1 and _match.team_2:
            _match.match_number = _counter
            _match.date = _date
            if _counter%tournament.matches_per_day ==0:
                print("date change",_counter)
                _date = _date + timedelta(days=1)
            print(_counter)
            _counter = _counter+1

        _match.save()

        _matches.append(_match)

    generate_next_rounds(tournament, _matches, _round+1, _counter, _date + timedelta(days=1))

def generate_next_rounds(tournament, matches, _round, counter, _date):
    _matches = []
    _len = len(matches)
    if _len <=1:
        return
    for i in range(_len//2):
        _match = Match()
        _match.tournament = tournament
        _match.match_round = _round
        _match.left_previous = matches[i]
        _match.right_previous = matches[-1-i]

        _left_bye, _left_winner = _match.left_previous.is_bye()
        if _left_bye:
            _match.team_1 = _left_winner
        _right_bye, _right_winner = _match.right_previous.is_bye()
        if _right_bye:
            _match.team_2 = _right_winner

        _match.match_number = counter
        _match.date = _date
        if counter%tournament.matches_per_day == 0:
            print("date change", counter)
            _date = _date + timedelta(days=1)
        print(counter)
        counter = counter+1

        _match.save()

        _matches.append(_match)

    generate_next_rounds(tournament, _matches, _round+1, counter, _date + timedelta(days=1))

generate_schedules.short_description = "Generate knockout tournament"

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'rank', 'tournament']
    ordering = ['name']

class MatchAdmin(admin.ModelAdmin):
    readonly_fields = ('description', 'name', 'match_number','tournament','match_round', 'left_previous','right_previous','team_1', 'team_2', 'status','winner',)
    fields = ('date', 'name', 'description', 'tournament', 'match_number',  'team_1', 'team_2','match_round', 'status','winner', 'team_1_score', 'team_2_score', )
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        print(actions.items())
        return actions

class MatchInline(admin.TabularInline):
    model = Match
    ordering = ['match_number',]
    readonly_fields = ('description', 'match_number','tournament','match_round', 'left_previous','right_previous','team_1', 'team_2', 'status','winner',  )
    fields = ('date', 'description', 'match_number', 'team_1', 'team_2','match_round', 'status','winner','team_1_score', 'team_2_score', )
    can_delete = False
    def has_add_permission(self, request):
        return False

class TeamInline(admin.TabularInline):
    model = Team
    ordering = ['rank']
    fields = ('name', 'rank', )

class TournamentAdmin(admin.ModelAdmin):
    readonly_fields = ('rounds',)
    fields = ('name', 'description', 'icon', 'start_date', 'matches_per_day', )
    inlines = [
        TeamInline,
        MatchInline,
    ]
    actions = [generate_schedules]

admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Tournament, TournamentAdmin)

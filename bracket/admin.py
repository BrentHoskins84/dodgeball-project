from django.contrib import admin
from bracket.models import Match, Tournament, Team
import math
import random
# Register your models here.

def seed(teams, _len):
    _seed = []
    _high = _len+1

    for r in range(1,_high):
        _seed.append(r)

    random.shuffle(_seed)
    i = 1
    for t in teams:
        if i < _high:
            t.seed = _seed[i-1]
            t.save()
            i += 1


def create_match(teams, tournament):

    _tournament = Tournament()
    for t in tournament:
        _tournament = t

    for i in range(0, len(teams),2):
        _match = Match()

        t1 = teams[i]
        t2 = teams[i+1]
        i += 1

        _match.tournament = _tournament
        if t1 != 'None':
            _match.team_1 = t1
        if t2 != 'None':
            _match.team_2 = t2
        _match.status = 'Scheduled'
        _match.match_round = '1'
        _match.save()


def add_byes(teams):
    length = int(len(teams))
    print(length)
    if (length < 4):
        bye =  4 - len(teams)
        print(bye)
        for i in range(bye):
            teams.append(None)

    elif (length > 4 and length < 8):
        bye = 8 - len(teams)
        for i in range(bye):
            teams.append(None)

    elif (length > 8 and length < 16):
        bye = 16 - len(teams)
        for i in range(bye):
            teams.append(None)
    else:
        pass

    random.shuffle(teams)
    # print(teams)
    # for i in range(length-1):
    #     if teams[i] == None and teams[i+1] == None:
    #         print(teams[i])
    # print(teams)
    return teams



def generate_matches(modeladmin, request, queryset):
    for t in queryset:
        t.matches.all().delete()

    tournament = queryset

    _len = len(Team.objects.all())
    if _len == 0:
        return

    tournament.update(rounds=int(math.ceil(math.log(_len, 2))))

    _teams_list = list(Team.objects.all().order_by('seed'))
    _teams_list = add_byes(_teams_list)
    print(_teams_list)
    create_match(_teams_list, tournament)



class MatchInline(admin.TabularInline):
    model = Match
    fields = ('team_1', 'team_2', 'team_1_score', 'team_2_score' )



@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    actions = [generate_matches]
    inlines = [MatchInline, ]

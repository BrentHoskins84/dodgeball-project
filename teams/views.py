from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView, FormView
from bracket.models import Team, Player, TeamPasscode, Tournament
from .forms import TeamModelForm, PlayerModelForm, TeamCreateModelForm, PlayerCreateModelForm

class TeamCreateView(FormView):
    template_name = 'team_create.html'
    form_class = TeamCreateModelForm

    def get_success_url(self):
        return '/'

    def form_valid(self, form):
        tournament = Tournament.objects.all()
        for t in tournament:
            _tour = t
        print(tournament)
        team = Team()
        team.name = form.cleaned_data['team_name']
        team.tournament = _tour
        team.save()
        passcode = TeamPasscode()
        passcode.team = team
        passcode.passcode = form.cleaned_data['team_passcode']
        passcode.save()
        player = Player()
        player.team = team
        player.first_name = form.cleaned_data['player_first_name']
        player.last_name = form.cleaned_data['player_last_name']
        player.nationality = form.cleaned_data['player_nationality'].upper()
        player.email = form.cleaned_data['players_email']
        player.phone_number = form.cleaned_data['phone_Number']
        player.save()
        send_email(team, passcode, player)
        return super(TeamCreateView, self).form_valid(form)


class TeamListView(ListView):
    template_name = 'team_list.html'
    queryset = Team.objects.all()


class TeamDetailView(DetailView):
    template_name = 'team_detail.html'
    queryset = Team.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Team, id=id_)


class PlayerCreateView(FormView):
    template_name = 'player_create.html'
    form_class = PlayerCreateModelForm

    def get_success_url(self):
        return '/'

    def form_valid(self, form):
        team_name = TeamPasscode.objects.get(passcode=form.cleaned_data['team_passcode'])
        team = Team.objects.get(name=team_name)
        player = Player()
        player.team = team
        player.first_name = form.cleaned_data['player_first_name']
        player.last_name = form.cleaned_data['player_last_name']
        player.nationality = form.cleaned_data['player_nationality'].upper()
        player.email = form.cleaned_data['players_email']
        player.phone_number = form.cleaned_data['phone_Number']
        player.save()

        return super(PlayerCreateView, self).form_valid(form)


class PlayerListView(ListView):
    template_name = 'player_list.html'
    queryset = Player.objects.all()


class PrivateTeamlistView(ListView):
    template_name = 'private_team_list.html'
    queryset = Team.objects.all()


def send_email(team, passcode, player):
    subject = 'Thank you for signing up for the US International Dodgeball Tournament'
    message = f'Your team name is: {team.name} \n  your team passcode is: {passcode.passcode} \n \n You will need to give the team passcode to your teammates. With out this passcode they will not be able to join your team. \n \n \n Thank You \n US Contengient \n SAMS II / Raising 6 / Top 3 '
    from_email = settings.EMAIL_HOST_USER
    to_list = [player.email, settings.EMAIL_HOST_USER]
    send_mail(subject, message, from_email, to_list, fail_silently=False)

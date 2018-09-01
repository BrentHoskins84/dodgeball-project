from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView, FormView
from .models import Team, Player, TeamPasscode
from .forms import TeamModelForm, PlayerModelForm, TeamCreateModelForm, PlayerCreateModelForm
from django.http import HttpResponse


class TeamCreateView(FormView):
    template_name = 'team_create.html'
    form_class = TeamCreateModelForm

    def get_success_url(self):
        return '/'

    def form_valid(self, form):
        # print(form.cleaned_data)
        team = Team()
        team.name = form.cleaned_data['team_name']
        team.save()
        passcode = TeamPasscode()
        passcode.team = team
        print(form.cleaned_data['team_passcode'])
        passcode.passcode = form.cleaned_data['team_passcode']
        passcode.save()
        player = Player()
        player.team = team
        player.first_name = form.cleaned_data['player_first_name']
        player.last_name = form.cleaned_data['player_last_name']
        player.nationality = form.cleaned_data['player_nationality']
        player.email = form.cleaned_data['players_email']
        player.phone_number = form.cleaned_data['phone_Number']
        player.save()
        return super(TeamCreateView, self).form_valid(form)


class TeamListView(ListView):
    template_name = 'team_list.html'
    queryset = Team.objects.all()


class TeamDetailView(DetailView):
    template_name = 'team_detail.html'
    # queryset = Team.objects.all()

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
        player.nationality = form.cleaned_data['player_nationality']
        player.email = form.cleaned_data['players_email']
        player.phone_number = form.cleaned_data['phone_Number']
        player.save()

        return super(PlayerCreateView, self).form_valid(form)


class PlayerListView(ListView):
    template_name = 'player_list.html'
    queryset = Player.objects.all()

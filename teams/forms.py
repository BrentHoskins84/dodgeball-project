from django import forms
from bracket.models import *
from django.utils.translation import gettext_lazy as _


class TeamModelForm(forms.ModelForm):
    passcode = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Team
        fields = '__all__'

        error_messages = {
            'name': {
                'unique':_('A team with this name already exists, please select a different name.')
            },
        }
        labels = {
            'name':_('Team Name'),
        }


class PlayerModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'


class TeamCreateModelForm(forms.Form):
    team_name = forms.CharField()
    team_passcode = forms.CharField(widget=forms.PasswordInput)
    player_first_name = forms.CharField()
    player_last_name = forms.CharField()
    player_nationality = forms.CharField()
    players_email = forms.EmailField()
    phone_Number = forms.CharField()


    def clean_team_name(self):
        data = self.cleaned_data['team_name']
        if Team.objects.filter(name=data).exists():
            raise forms.ValidationError('A team with this name already exists, please select a different name.')
        return data

    def clean_team_passcode(self):
        data = self.cleaned_data['team_passcode']
        if TeamPasscode.objects.filter(passcode=data).exists():
            raise forms.ValidationError('this passcode is already in use, please select a different passcode.')
        return data

    def clean_players_email(self):
        data = self.cleaned_data['players_email']
        if Player.objects.filter(email=data).exists():
            player = Player.objects.get(email=data)
            raise forms.ValidationError(f'Player with this email already exist and is signed up to play on {player.team}.')
        return data

class PlayerCreateModelForm(forms.Form):
    team_passcode = forms.CharField(widget=forms.PasswordInput)
    player_first_name = forms.CharField()
    player_last_name = forms.CharField()
    player_nationality = forms.CharField()
    players_email = forms.EmailField()
    phone_Number = forms.CharField()

    def clean_team_passcode(self):
        data = self.cleaned_data['team_passcode']
        if not TeamPasscode.objects.filter(passcode=data).exists():
            raise forms.ValidationError('That is not the correct passcode for this team, please re-enter your team passcode.')
        return data

    def clean_players_email(self):
        data = self.cleaned_data['players_email']
        if Player.objects.filter(email=data).exists():
            player = Player.objects.get(email=data)
            raise forms.ValidationError(f'Player with this email already exist and is signed up to play on {player.team}.')
        return data

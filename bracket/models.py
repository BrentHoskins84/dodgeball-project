from django.db import models

from teams.models import Team

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, default='', null=True)
    start_date = models.DateField('Start date')
    current_round = models.IntegerField(default=0)
    rounds = models.IntegerField(default=0)
    icon = models.ImageField(upload_to='static/icons', verbose_name='image', blank=True)

    def __str__(self):
        return '%s' % (self.name)



class Match(models.Model):
    match_id = models.AutoField(primary_key=True, name='match_id')
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT, related_name='tournament')
    team_1 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="player_1", unique=False)
    team_2 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="player_2", unique=False)
    team_1_score = models.IntegerField(name='team_1_score', null=True, blank=True, unique=False)
    team_2_score = models.IntegerField(name='team_2_score', null=True, blank=True, unique=False)
    # start_time = models.DateTimeField(null=True, blank=True, name='time')
    round = models.IntegerField(name='round', null=True, blank=True, unique=False)
    winner = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='match_winner', null=True, blank=True, unique=False)


    def __str__(self):
        return 'Match %s' % (self.match_id)

    def get_player_names(self):
        return [str(self.player_1) if self.player_1 else None, str(self.player_2) if self.player_2 else None,]

    def set_winner(self):
        if self.team_1_score > self.team_2_score:
            self.winner = self.team_1
        else:
            self.winner = self.team_2


    def get_result_values(self):
        return [self.team_1_score, self.team_2_score,]

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
    class Meta:
        verbose_name_plural = "Matches"

    MATCH_STATUS = [
        ("BYE", 'BYE'),
        ("Not Scheduled", 'Not Scheduled'),
        ("Scheduled", "Scheduled"),
        ('Finished', 'Finished')
    ]

    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT, related_name='matches')
    team_1 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="team_1", unique=False)
    team_2 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="team_2", unique=False)
    status = models.CharField(max_length=20, choices=MATCH_STATUS, default='Not Scheduled')
    team_1_score = models.PositiveIntegerField(null=True, blank=True, name='team_1_score', default=0)
    team_2_score = models.PositiveIntegerField(null=True, blank=True, name='team_2_score', default=0)
    start_time = models.DateTimeField(null=True, blank=True, name='time')
    match_round = models.IntegerField(default=1)
    winner = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='match_winner', null=True, blank=True, unique=False)


    def __str__(self):
        return "{} - {} vs {}".format(self.id, self.team_1, self.team_2)

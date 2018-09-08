from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django import forms

from django.dispatch import receiver
from django.db.models.signals import post_save
# from bracket.models import Tournament

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    seed = models.PositiveIntegerField(null=True, blank=True, name='seed')


    def __str__(self):
        return '%s' % (self.name)

    def get_absolute_url(self):
        return reverse('teams:team-detail', kwargs={'id': self.id})


class TeamPasscode(models.Model):
    team = models.OneToOneField('Team', on_delete=models.CASCADE, related_name="passcode")
    passcode = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return '%s' % (self.team)


class Player(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256, null=True)
    email = models.EmailField(max_length=54, unique=True)
    PHONE_REGEX = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '999999999', with no spaces. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[PHONE_REGEX], max_length=17, blank=True) # validators should be a list
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='players')
    # tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="players", blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

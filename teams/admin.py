from django.contrib import admin
from teams.models import Team, Player, TeamPasscode

# Register your models here.

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(TeamPasscode)

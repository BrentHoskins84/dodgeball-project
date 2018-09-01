import pygal

from teams.models import Team, Player

class NationalityPieChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        # self.chart.title = 'Nationalities'

    def get_data(self):
        # team = Team.objects.all()
        data = {}
        for player in Player.objects.all():
            count = Player.objects.filter(nationality=player.nationality).count() #should return all players on a team
            data[player.nationality] = int(count)
        return data

    def generate(self):
        chart_data = self.get_data()

        for key, value in chart_data.items():
            self.chart.add(key, value)

        return self.chart.render(is_unicode=True)

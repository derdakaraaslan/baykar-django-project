from django.db import models
from .aircrafts import Aircraft
from .teams import Team

class Part(models.Model):
    name = models.CharField(max_length=100)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
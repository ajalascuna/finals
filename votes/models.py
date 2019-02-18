from django.db import models
from datetime import datetime

# Create your models here.

class Partylist(models.Model):
    partylist_name = models.CharField(max_length = 100)
    description = models.TextField()
    def __str__(self):
        return format(self.partylist_name)



class Position(models.Model):
    position_name = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return 'Position {}'.format(self.position_name)

class Candidate(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    partylist = models.ForeignKey(Partylist,
                on_delete = models.CASCADE,
                related_name = 'partylist',
                null=True, blank=True)
    position = models.ForeignKey(Position,
                on_delete = models.CASCADE,
                related_name = 'positions',
                null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    platform = models.TextField()
    # is_active =

    def __str__(self):
        return 'Candidate: {}'.format(self.firstname, self.lastname)



class Vote(models.Model):
    name = models.CharField(max_length = 100)
    candidate = models.ForeignKey(Candidate,
                on_delete = models.CASCADE,
                related_name = 'candidates',
                null=True, blank=True)
    vote_datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return 'Vote {}'.format(self.name)

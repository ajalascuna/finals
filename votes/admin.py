from django.contrib import admin
from .models import Candidate, Position, Vote, Partylist

# Register your models here.

admin.site.register(Partylist)
admin.site.register(Candidate)
admin.site.register(Position)
admin.site.register(Vote)

from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from .models import Partylist, Candidate, Position



class PartylistModelForm(ModelForm):
    class Meta:
        model = Partylist
        exclude = ['id']

class CandidateModelForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['id', 'position']

class PositionModelForm(ModelForm):
    class Meta:
        model = Position
        exclude = ['id']

class RegistrationModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': PasswordInput()
}

from django.shortcuts import render, redirect
from .models import Candidate, Position, Vote
from .forms import (CandidateModelForm, PositionModelForm,
                    RegistrationModelForm, PartylistModelForm)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def index(request):
    context = {}
    candidates = Candidate.objects.all().order_by('position')
    context['candidates'] = candidates
    # partylists = Partylist.objects.partylist.all()
    # context['partylists'] = partylists

    return render(request, 'index.html', context)

@login_required
def detail_candidate(request, partylist_id, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)
    context['candidate'] = candidate
    return render(request, 'detail_candidate.html', context)

@login_required
def create_candidate(request):
    context = {}
    positions = Position.objects.all()
    context['position'] = positions
    if request.method == 'POST':
        form = CandidateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')
        else:
            context['form'] = form
    else:
        form = CandidateModelForm()
        context['form'] = form
    return render(request, 'create_candidate.html', context)


@login_required
def create_partylist(request):
    context = {}
    if request.method == 'POST':
        form = PartylistModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')
        else:
            context['form'] = form
    else:
        form = PartylistModelForm()
        context['form'] = form
    return render(request, 'create_partylist.html', context)



@login_required
def update_candidate(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)
    if request.method == 'POST':
        form = CandidateModelForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('votes:detail', form.instance.id)
        else:
            context['form'] = form
    else:
        form = CandidateModelForm(instance=candidate)
        context['form'] = form
    return render(request, 'update_candidate.html', context)

@login_required
def create_position(request):
    context = {}
    if request.method == 'POST':
        form = PositionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')
        else:
            context['form'] = form
    else:
        form = PositionModelForm()
        context['form'] = form
    return render(request, 'create_position.html', context)

@login_required
def vote(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    vote = Vote(candidate=candidate)
    vote.save()
    return redirect('votes:index')





def registration(request):
    form = RegistrationModelForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = RegistrationModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect('votes:index')
        else:
            context['form'] = form
    return render(request, 'registration.html', context)

def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            # messages.info(request, 'Your password is incorrect!')
            return redirect('votes:index')
    return render(request, 'login.html', context)


def user_logout(request):
    context = {}
    logout(request)
    return redirect('votes:index')

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll
from polls.forms import PollForm
import datetime
from django.template import RequestContext

def index(request):
    latest_poll_list = Poll.objects.filter(muaccount=request.muaccount).order_by('-pub_date')
    return render_to_response('polls/index.html', RequestContext(request, locals()))

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p}, RequestContext(request, locals()))

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, RequestContext(request, locals()))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p}, RequestContext(request, locals()))

def create(request):
    
    if (request.POST):
        form = PollForm(request.POST)
        poll = form.save(commit=False)
        poll.muaccount = request.muaccount
        poll.pub_date = datetime.datetime.now()
        poll.save()        
        if request.POST['choice1']:
            c1 = Choice()
            c1.poll = poll
            c1.choice = request.POST['choice1']
            c1.votes = 0
            c1.save()
        if request.POST['choice2']:
            c2 = Choice()
            c2.poll = poll
            c2.choice = request.POST['choice2']
            c2.votes = 0
            c2.save()
        if request.POST['choice3']:
            c3 = Choice()
            c3.poll = poll
            c3.choice = request.POST['choice3']
            c3.votes = 0
            c3.save()
        if request.POST['choice4']:
            c4 = Choice()
            c4.poll = poll
            c4.choice = request.POST['choice4']
            c4.votes = 0
            c4.save()

        return HttpResponseRedirect(reverse('polls.views.index'))
    else:
        form = PollForm()
        return render_to_response('polls/create.html', {'form': form}, RequestContext(request, locals()))

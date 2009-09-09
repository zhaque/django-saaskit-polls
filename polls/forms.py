from django import forms
from polls.models import Choice, Poll

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ('muaccount', 'pub_date')

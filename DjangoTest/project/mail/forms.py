import datetime
from django import forms
from django.forms import DateInput

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    ###################
    # Changed
    ###################
    date = forms.DateField(initial=datetime.date.today,
    ###################
    # Changed
    ###################
        widget=DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date'},
        )
    )

    class Meta:
        model = Appointment
        fields = [
            'client_name',
            'message',
            'date',
        ]

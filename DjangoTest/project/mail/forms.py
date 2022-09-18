from django import forms
from django.forms import DateInput

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(
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
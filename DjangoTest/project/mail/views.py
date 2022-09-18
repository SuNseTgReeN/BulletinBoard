from django.core.mail import send_mail
from django.utils.datetime_safe import datetime
from django.views.generic import CreateView

from .forms import AppointmentForm
from .models import Appointment


class AppointmentView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'make_appointment.html'

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            message=request.POST["message"],
            client_name=request.POST["client_name"],
            date=datetime.strptime(request.POST["date"], '%Y-%m-%d'),
        )

        send_mail(
            subject=f'{appointment.message} '
                    f'{appointment.date}',
            message=appointment.message,
            from_email='zminator.zm@yandex.ru',
            recipient_list=['zminator.zm@yandex.ru'],
        )

        return super().post(request, *args, **kwargs)
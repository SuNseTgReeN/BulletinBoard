from django.shortcuts import render, redirect
from django.views import generic, View
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from datetime import datetime

from django.template.loader import render_to_string
from .models import Appointment
from .forms import AppointmentForm
from .tasks import hello, printer


class AppointmentView(generic.CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'appointment/make_appointment.html', {'form': AppointmentForm()})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
        print(date)
        appointment = Appointment(
            date=date,
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        print(appointment)
        appointment.save()

        html_content = render_to_string(
            'appointment/appointment_created.html',
            {
                'appointment': appointment,
            }
        )

        # в конструкторе уже знакомые нам параметры, да? Называются правда немного по другому, но суть та же.
        msg = EmailMultiAlternatives(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            body=appointment.message,  # это то же, что и message
            from_email='zminator.zm@yandex.ru',
            to=['layla.fond@mail.ru', 'ahtohio_pal09@bk.ru'],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем

        return redirect('appointments:make_appointment')


class IndexView(View):
    def get(self, request):
        hello.delay()
        printer.delay(10)
        return HttpResponse('Hello!')

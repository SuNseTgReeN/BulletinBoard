from django.urls import path

from .views import AppointmentView, IndexView

app_name = 'appointments'

urlpatterns = [
    path('', AppointmentView.as_view(), name='make_appointment'),
    path('index', IndexView.as_view()),
]

from django.urls import path

from .views import AppointmentView

###################
# Changed
###################


app_name = 'appointments'

urlpatterns = [
    path('', AppointmentView.as_view(), name='make_appointment'),

]

###################
# Changed
###################
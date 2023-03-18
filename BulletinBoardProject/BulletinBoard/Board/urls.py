from django.urls import path

from .views import NotificationList, NotificationDetail, NotificationSearch

app_name = 'Board'

urlpatterns = [
    path('', NotificationList.as_view(), name='notification_list'),
    path('detail/<int:pk>', NotificationDetail.as_view(), name='notification_detail'),
    path('search/', NotificationSearch.as_view(), name='notification_search'),

]

from django.urls import path

from .views import NotificationList, NotificationDetail, NotificationSearch, NotificationCreate, NotificationUpdate, \
    NotificationDelete, ResponsesListNotif, ResponsesListResp, ResponsesListRespCreate, ResponsesListRespUpdate, \
    ResponsesListRespDelete

app_name = 'Board'

urlpatterns = [
    path('', NotificationList.as_view(), name='notification_list'),
    path('notification_detail/<int:pk>', NotificationDetail.as_view(), name='notification_detail'),
    path('search/', NotificationSearch.as_view(), name='notification_search'),
    path('create/', NotificationCreate.as_view(), name='notification_create'),
    path('notification_detail/<int:pk>/update', NotificationUpdate.as_view(), name='notification_update'),
    path('notification_detail/<int:pk>/delete', NotificationDelete.as_view(), name='notification_delete'),
    path('myresponses/', ResponsesListResp.as_view(), name='my_responses_list'),
    path('notification_detail/<int:pk>/responses/create', ResponsesListRespCreate.as_view(), name='responses_create'),
    path('notification_detail/<int:pk>/responses/update', ResponsesListRespUpdate.as_view(), name='my_responses_update'),
    path('notification_detail/<int:pk>/responses/delete', ResponsesListRespDelete.as_view(), name='my_responses_delete'),
    path('responses/', ResponsesListNotif.as_view(), name='other_responses_list'),

]

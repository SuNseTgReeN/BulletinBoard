from django.urls import path

from .views import NotificationList, NotificationDetail, NotificationSearch, NotificationCreate, NotificationUpdate, \
    NotificationDelete, ResponsesListNotif, ResponsesListResp, ResponsesListRespCreate

app_name = 'Board'

urlpatterns = [
    path('', NotificationList.as_view(), name='notification_list'),
    path('detail/<int:pk>', NotificationDetail.as_view(), name='notification_detail'),
    path('search/', NotificationSearch.as_view(), name='notification_search'),
    path('create/', NotificationCreate.as_view(), name='notification_create'),
    path('<int:pk>/update', NotificationUpdate.as_view(), name='notification_update'),
    path('<int:pk>/delete', NotificationDelete.as_view(), name='notification_delete'),
    path('responses/', ResponsesListNotif.as_view(), name='responses_list_notif'),
    path('myresponses/', ResponsesListResp.as_view(), name='responses_list_resp'),
    path('detail/<int:pk>/response_create', ResponsesListRespCreate.as_view(), name='responses_create'),


]

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import ProductFilter
from .models import Notification


class NotificationList(ListView):
    model = Notification
    template_name = 'Board/notification_list.html'
    context_object_name = 'Board'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NotificationDetail(DetailView):
    model = Notification
    template_name = 'Board/notification_detail.html'
    context_object_name = 'notification_detail'


class NotificationSearch(ListView):
    model = Notification
    ordering = '-date_creation', 'rating'
    template_name = 'Board/notification_search.html'
    context_object_name = 'search'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NotificationCreate(CreateView):
    pass


class NotificationUpdate(UpdateView):
    pass


class NotificationDelete(DeleteView):
    pass


class ResponsesList(ListView):
    pass


class CategoryListView(ListView):
    pass

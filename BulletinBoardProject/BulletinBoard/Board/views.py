from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import ProductFilter
from .forms import NotificationForm, ResponsesForm
from .models import Notification, Responses


class NotificationList(ListView):
    model = Notification
    ordering = '-date_creation', 'rating'
    template_name = 'Board/notification_list.html'
    context_object_name = 'notification_list'
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
    form_class = NotificationForm
    model = Notification
    template_name = 'Board/notification_create.html'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.notification_user = self.request.user
        fields.save()
        return super().form_valid(form)


class NotificationUpdate(UpdateView):
    form_class = NotificationForm
    model = Notification
    template_name = 'Board/notification_create.html'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.notification_user = self.request.user
        fields.save()
        return super().form_valid(form)


class NotificationDelete(DeleteView):
    model = Notification
    template_name = 'Board/notification_delete.html'
    success_url = reverse_lazy('Board:notification_list')


class ResponsesListNotif(ListView):
    """ Тут описаны все отлкики которые пришли вам, как автору объявления """
    model = Responses
    ordering = '-date_creation', 'status'
    template_name = 'Board/responses_list.html'
    context_object_name = 'responses'
    paginate_by = 4

    def get_queryset(self):
        return Responses.objects.filter(responses_advertising__notification_user=self.request.user)


class ResponsesListResp(ListView):
    """ Тут описаны все отлкики которые вы отправили """
    model = Responses
    ordering = '-date_creation', 'status'
    template_name = 'Board/my_responses_list.html'
    context_object_name = 'responses'
    paginate_by = 4

    def get_queryset(self):
        return Responses.objects.filter(responses_user=self.request.user)


class ResponsesListRespCreate(CreateView):
    form_class = ResponsesForm
    model = Responses
    template_name = 'Board/responses_create.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            resp = form.save(commit=False)
            resp.responses_user = request.user
            resp.save()
            return self.form_valid(form)
        return redirect('Board:notification_detail', **kwargs)
            

# class ResponsesListRespUpdate(UpdateView):
#     form_class = ResponsesForm
#     model = Responses
#     template_name = ''
#
#     def form_valid(self, form):
#         fields = form.save(commit=False)
#         fields.notification_user = self.request.user
#         fields.save()
#         return super().form_valid(form)


class CategoryListView(ListView):
    pass

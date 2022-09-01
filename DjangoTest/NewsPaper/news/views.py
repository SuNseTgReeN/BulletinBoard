from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import PostForm
from .models import Post, Author
from .filters import ProductFilter


class PostList(ListView):
    model = Post
    ordering = '-date_creation', 'rating'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class SearchList(ListView):
    model = Post
    ordering = '-date_creation', 'rating'
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'news.view_Post'
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'news.add_Post'
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.post_author = Author.objects.get(author_user=self.request.user)
        fields.save()
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'news.change_Post'
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'


class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'news.delete_Post'
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')

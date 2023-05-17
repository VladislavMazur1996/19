from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView

from .forms import PostForm, CommentForm
from .models import Post, Comment
from .filters import *


@login_required
def advert_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'advert/post_edit.html', {'form': form})


@login_required
def comment_new(request, *args, **kwargs):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = Post.objects.get(pk=int(request.path_info.split('/')[2]))
            comment.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm()
    return render(request, 'advert/comment_new.html', {'form': form})


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'advert/post_edit.html'


class PostList(ListView):
    form_class = PostForm
    model = Post
    template_name = 'advert/post_list.html'
    context_object_name = 'posts'
    ordering = ['-id']


class PostDetail(DetailView):
    form_class = PostForm
    model = Post
    template_name = 'advert/post_detail.html'
    context_object_name = 'post'


class CommentDetail(DetailView):
    form_class = CommentForm
    model = Comment
    template_name = 'advert/comment_detail.html'
    context_object_name = 'comment'


class CommentList(ListView):
    form_class = CommentForm
    model = Comment
    template_name = 'advert/comment_list.html'
    context_object_name = 'comment'
    ordering = ['post_id']

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CommentFilter(self.request.GET, queryset)
        return self.filterset.qs
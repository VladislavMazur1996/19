import django_filters

from django_filters import FilterSet
from .models import Post
from django.forms import widgets


class CommentFilter(FilterSet):
    model = Post
    post = django_filters.ModelChoiceFilter(queryset=Post.objects.all())

    class Meta:
        model = Post
        fields = {}

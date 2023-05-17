from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'text',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]

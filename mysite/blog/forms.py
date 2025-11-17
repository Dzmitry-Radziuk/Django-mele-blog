from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Форма для добавления комментария к посту."""

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class EmailPostForm(forms.Form):
    """Форма для отправки поста на email."""

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class SearchForm(forms.Form):
    """Форма для поиска постов по ключевому слову."""

    query = forms.CharField()

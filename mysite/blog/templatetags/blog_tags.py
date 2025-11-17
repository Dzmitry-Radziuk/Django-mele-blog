from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag
def total_posts():
    """Возвращает общее количество опубликованных постов."""
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    """Возвращает словарь с последними опубликованными постами."""
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    """Возвращает список самых комментируемых опубликованных постов."""
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    """Преобразует Markdown в HTML и помечает как безопасный для шаблона."""
    return mark_safe(markdown.markdown(text))

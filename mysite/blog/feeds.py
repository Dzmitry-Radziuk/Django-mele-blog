import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords, strip_tags
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    """RSS-лента с последними опубликованными постами блога."""

    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        html_content = markdown.markdown(item.body)
        clean_text = strip_tags(html_content)
        return truncatewords(clean_text, 30)

    def item_pubdate(self, item):
        return item.publish

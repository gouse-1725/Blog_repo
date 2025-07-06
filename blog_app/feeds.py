# blog_app/feeds.py

from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import Blog 

class LatestBlogPostsFeed(Feed):
    title = "My Blog - Latest Posts"
    link = reverse_lazy('home') 
    description = "Updates on the latest blog posts from My Blog."

    def items(self):
        return Blog.objects.order_by('-created_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content 

    def item_link(self, item):
        return reverse_lazy('blog_detail', kwargs={'slug': item.slug})

    def item_description_html(self, item):
        return item.content 
from django.contrib.sitemaps import Sitemap
from posts.models import Post
from django.shortcuts import reverse

class PostSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Post.objects.all()

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['aboutus', 'index', 'top10_list']

    def location(self, item):
        return reverse(item)

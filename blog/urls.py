from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap, StaticViewSitemap

from posts.views import index, blog, post, search, aboutus, top10

sitemaps = {
'posts': PostSitemap,
'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='post-list'),
    path('top10/', top10, name='top10_list'),
    path('search/', search, name='search'),
    path('post/<slug:slug>,<int:id>/', post, name='post-detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('tinymce/', include('tinymce.urls')),
    path('aboutus', aboutus, name='aboutus'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

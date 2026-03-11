from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from .views import home, church_news_archive, reading_page, youth_church_landing, gallery, book, map, menfellow, wemenfellow, youth, child, podcast

# Define your sitemaps
sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("game/", include("game.urls")),
    path("subscribe/", include("newsletter.urls")),  
    path("", home, name="home"), 
    path('church-news-archive/', church_news_archive, name='church_news_archive'),
    path('youth-church-landing/', youth_church_landing, name='youth_church_landing'),
    path('gallery/', gallery, name='gallery'),
    path('map/', map, name='map'),
    path('menfellow/', menfellow, name='menfellow'),
    path('wemenfellow/', wemenfellow, name='wemenfellow'),
    path('youth/', youth, name='youth'),
    path('book/', book, name='book'),
    path('child/', child, name='child'),
    path('reading/', reading_page, name='reading_page'),
    path('podcast/', podcast, name='podcast'),
    
    # Sitemap URL
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
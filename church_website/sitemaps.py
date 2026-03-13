# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        # Return a list of URL names for your static views
        return [
            'home', 
            'church_news_archive', 
            'youth_church_landing', 
            'gallery', 
            'map', 
            'menfellow', 
            'wemenfellow', 
            'youth', 
            'book', 
            'child', 
            'reading_page', 
            'podcast', 
            
        ]

    def location(self, item):
        return reverse(item)
# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class HighPrioritySitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)

class MediumPrioritySitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return [
            'church_news_archive', 
            'youth_church_landing', 
            'gallery', 
            'map', 
            'youth', 
        ]

    def location(self, item):
        return reverse(item)

class StandardPrioritySitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return [
            'menfellow', 
            'wemenfellow', 
            'book', 
            'child', 
            'reading_page', 
            'podcast', 
        ]

    def location(self, item):
        return reverse(item)

class GameSectionSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return [
            'register',
            'login',
        ]

    def location(self, item):
        return reverse(item)
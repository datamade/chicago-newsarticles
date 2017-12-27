from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from itertools import groupby
from collections import OrderedDict

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


@python_2_unicode_compatible
class NewsSource(models.Model):
    name = models.CharField(max_length=256)
    short_name = models.CharField(max_length=256, db_index=True)
    legacy_feed_id = models.CharField(max_length=8, blank=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

@python_2_unicode_compatible
class ScraperResult(models.Model):
    """
    A single run of a scraper.
    """
    news_source = models.ForeignKey(NewsSource, db_index=True)

    completed_time = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField()
    added_count = models.PositiveSmallIntegerField(default=0)
    error_count = models.PositiveSmallIntegerField(default=0)
    total_count = models.PositiveSmallIntegerField(default=0)

    output = models.TextField(blank=True)

    def __str__(self):
        return '{} - {}'.format(self.news_source.name, self.completed_time)

@python_2_unicode_compatible
class Article(models.Model):
    """
    Base article contents. Should never change after initial scraping
    """
    news_source = models.ForeignKey(NewsSource, null=True, db_index=True)
    url = models.CharField(max_length=1024, unique=True, db_index=True)
    title = models.TextField()
    author = models.CharField(max_length=1024, default="", blank=True)
    bodytext = models.TextField()
    orig_html = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    last_modified = models.DateTimeField(auto_now=True)

    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.url[:60]


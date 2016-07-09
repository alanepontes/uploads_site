from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class PostDocument(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    resume = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

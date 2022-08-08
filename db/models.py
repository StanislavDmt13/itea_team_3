from django.db import models
from django.contrib.auth import models as author_models


class Task(models.Model):

    title = models.CharField(max_length=200)

    author = models.ForeignKey(author_models.User, on_delete=models.CASCADE)

    opened_at = models.DateTimeField(auto_created=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    content = models.TextField(max_length=500)

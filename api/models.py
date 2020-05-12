from django.db import models
from django.conf import settings


class List(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.title)


class Task(models.Model):
    _list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title

from django.db import models
from django.utils import timezone


class Post(models.Model):

    title = models.CharField('タイトル', max_length=255)
    timekeeper = models.CharField('タイトル',default=0, max_length=255)
    jfile = models.FileField(upload_to='',default='graph.json')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title

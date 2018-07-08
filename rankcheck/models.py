from django.db import models
from django.utils import timezone


class Post(models.Model):

    title = models.CharField('タイトル', max_length=255)
    url = models.URLField('URL',max_length = 200, default="URLを入力して下さい")
    r_url = models.CharField('タイトル', max_length=255, default="a")
    rank = models.CharField('タイトル', max_length=255, default="b")
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title

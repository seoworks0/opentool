from django.db import models
from django.utils import timezone


class Post(models.Model):

    title = models.CharField('タイトル', max_length=255)
    n_kyokiword = models.CharField('タイトル', max_length=255, default="a")
    n_example = models.CharField('タイトル', max_length=255, default="b")
    n_url = models.URLField('URL',max_length = 200, default="URLを入力して下さい")
    v_kyokiword = models.CharField('タイトル', max_length=255, default="c")
    v_example = models.CharField('タイトル', max_length=255, default="d")
    v_url = models.URLField('URL',max_length = 200, default="URLを入力して下さい")
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title

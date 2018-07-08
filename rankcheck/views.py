from django.http import JsonResponse
from django.views import generic
from .models import Post
from .juni import main
#import time


class PostList(generic.ListView):
    model = Post


def rankfunc(request):

    # 新規作成
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        for i,key in enumerate(title.split("\n")):
            rank,r_url=main(key,url)
            pass
        #time.sleep(10)
        #r_url = "unko.jp"
        #rank = "1"
        print(rank)

        post = Post(title=title,url=url,r_url=r_url,rank=rank)
        post.save()
        d = {
            'pk': post.pk,
            'created_at': post.created_at,
            'title': post.title,
            'url': post.url,
            'r_url': post.r_url,
            'rank': post.rank,
        }
        return JsonResponse(d)

from django.http import JsonResponse
from django.views import generic
from .models import Post
from .juni import main
#import time


class PostList(generic.ListView):
    model = Post


def rankfunc(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        title_list = title.split("\n")
        rank_list , url_list = main(title_list,url)
        
        post = Post(title=title_list,url=url,r_url=url_list,rank=rank_list)
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

from django.http import JsonResponse
from django.views import generic
from .models import Post
from .suggest import main

class PostList(generic.ListView):
    model = Post


def suggestfunc(request):

    # 新規作成
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        main(title)
        timekeeper = 1
        post = Post(title=title, timekeeper=timekeeper)
        post.save()
        d = {
            'timekeeper': post.timekeeper,
            'pk': post.pk,
            'created_at': post.created_at,
            'title': post.title,
        }

        #query = request.GET.get('query')
        return JsonResponse(d)

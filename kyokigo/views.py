from django.http import JsonResponse
from django.views import generic
from .models import Post
from .juni import main
from .kyokigo import kyoki


class PostList(generic.ListView):
    model = Post


def kyokifunc(request):
    n_kyokiword=[]
    n_example=[]
    n_url=[]
    v_kyokiword=[]
    v_example=[]
    v_url=[]

    # 新規作成
    if request.method == 'POST':
        keyword = request.POST.get('title')
        #kyokigo_v,kyokigo_n = kyoki(keyword)
        #print(len(kyokigo_n[0]))
        kyokigo_n=[['ああああ', 'おおおおお', 'https://www.youtube.com/watch?v=kzkSnSGBlEk'], ['保護', '終了いたしました。ご了承ください。, , , , 会社概要, 個人情報保護への取り組み', 'https://unkokanji.com/survey']]
        kyokigo_v=[['いいいい', ', 1111, 111', 'https://www.youtube.com/watch?v=kzkSnSGBlEk'], ['22', '333', 'https://unkokanji.com/survey']]

        length = len(kyokigo_n)
        for i in kyokigo_n:
            n_kyokiword.append(i[0])
            n_example.append(i[1])
            n_url.append(i[2])

        for i in kyokigo_v:
            v_kyokiword.append(i[0])
            v_example.append(i[1])
            v_url.append(i[2])

        #time.sleep(10)
        post = Post(title=keyword,n_kyokiword=n_kyokiword,n_example=n_example,n_url=n_url,v_kyokiword=v_kyokiword,v_example=v_example,v_url=v_url)
        post.save()
        d = {
            'length':length,
            'pk': post.pk,
            'created_at': post.created_at,
            'title': post.title,
            'n_kyokiword': post.n_kyokiword,
            'n_example': post.n_example,
            'n_url': post.n_url,
            'v_kyokiword': post.v_kyokiword,
            'v_example': post.v_example,
            'v_url': post.v_url,
        }
        return JsonResponse(d)

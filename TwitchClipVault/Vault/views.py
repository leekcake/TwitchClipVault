from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from Vault.models import Clip


def index(request):
    query = request.GET.get('p', 0)
    try:
        query = int(query)
    except:
        return HttpResponse("")

    mode = request.GET.get('mode', 0)
    try:
        mode = int(mode)
    except:
        return HttpResponse("")

    previous_query = query - 1
    next_query = query + 1
    clip_list = None
    if mode == 0:
        clip_list = Clip.objects.order_by('-CreatedAt')[query*50:(query*50+50)]
    elif mode == 1:
        clip_list = Clip.objects.order_by('CreatedAt')[query * 50:(query * 50 + 50)]
    elif mode == 2:
        clip_list = Clip.objects.order_by('-ViewCount')[query*50:(query*50+50)]
    context = {
        'clip_list': clip_list,
        'previous_query': previous_query,
        'next_query': next_query,
        'mode': mode
    }
    return render(request, 'Vault/index.html', context)

def view(request, videoId):
    context = {
        'videoId': videoId
    }
    return render(request, 'Vault/view.html', context)
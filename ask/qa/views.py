from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseNotFound


from qa import models


def test(request, *args, **kwargs):
    return HttpResponse('OK')

def page(request, *args, **kwargs):
    page = request.GET.get('page', 1)
    posts = models.Question.objects.new()
    if posts is None:
        raise Http404

    # posts = Post.objects.filter(is_published=True)
    limit = 10#request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page) # Page
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    
    r = render(request, 'nquestions.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
    })
    print(r.content)
    return r


def popular(request, *args, **kwargs):
    page = request.GET.get('page', 1)
    posts = models.Question.objects.popular()
    if posts is None:
        raise Http404
    # posts = Post.objects.filter(is_published=True)
    limit = 10#request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page) # Page
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    
    r = render(request, 'pquestions.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
    })
    print(r.content)
    return r

def question(request, *args, **kwargs):
    try:
        slug = int(kwargs['slug'])
    except ValueError:
        raise Http404
        # return HttpResponseNotFound()

    concreate = models.Question.objects.concreate(slug)
    if concreate is None:
        raise Http404
        # return HttpResponseNotFound()

    r = render(request, 'cquestion.html', {
        'question' : concreate, 
        'slug' : slug
    })
    print(r.content)
    return r

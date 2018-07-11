from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from django.http import HttpResponse, Http404
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as login2
from django.contrib.auth import logout as logout2

from datetime import datetime, timedelta

from qa import models
from qa import forms

def test(request, *args, **kwargs):
    return HttpResponse('OK')
    # return HttpResponseRedirect('/new_url/')


def page(request, *args, **kwargs):
    page = request.GET.get('page', 1)
    posts = models.Question.objects.new()
    if posts is None:
        raise Http404

    # posts = Post.objects.filter(is_published=True)
    limit = 10  # request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)  # Page
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    r = render(request, 'nquestions.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
    })
    # print(r.content)
    return r


def popular(request, *args, **kwargs):
    page = request.GET.get('page', 1)
    posts = models.Question.objects.popular()
    if posts is None:
        raise Http404
    # posts = Post.objects.filter(is_published=True)
    limit = 10  # request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)  # Page
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    r = render(request, 'pquestions.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
    })
    # print(r.content)
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
    answers = models.Answer.objects.filter(question=concreate)

    if request.method == 'POST':
        form = forms.AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            if request.user.is_authenticated:
                answer.author = request.user
            url = request.path
            return HttpResponseRedirect(url)
    else:
        form = forms.AnswerForm(initial={'question': concreate.pk})

    action = request.path

    r = render(request, 'cquestion.html', {
        'question': concreate,
        'slug': slug,
        'answers': answers,
        'form': form,
        'action': action,
    })
    # print(r.content)
    return r


# @login_required(login_url='/login/')
def ask(request):
    if request.method == 'POST':
        form = forms.AskForm(request.POST)
        if form.is_valid():
            # form.user = request.user
            question = form.save()
            if request.user.is_authenticated:
                question.author = request.user
            question.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = forms.AskForm()

    action = '/ask/'
    r = render(request, 'ask.html', {
        'form': form,
        'action': action,
    })
    # print(r.content)
    return r


def login(request):
    if request.method == 'POST':
        # print('1')
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # print('2')
            user = form.save()
            # login(request, user)
            # print('2.5')
            login2(request, user)
            # print('3')

            r = HttpResponseRedirect('/')
            print(r)
            return r
            # if sessid:
            #     print('4')
            #     response = HttpResponseRedirect('/')
            #     response.set_cookie(
            #         sessid=sessid,
            #         domain='127.0.0.1',
            #         httponly=True,
            #         expires=datetime.now()+timedelta(days=5)
            #     )
            #     return response
    else:
        # print('5')
        form = forms.LoginForm()
    # print('6')
    action = '/login/'
    r = render(request, 'login.html', {
        'form': form,
        'action': action,
    })
    # print(r.content)
    return r

def logout(request):
    logout2(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = forms.SignupForm()
    action = '/signup/'
    r = render(request, 'signup.html', {
        'form': form,
        'action': action,
    })
    # print(r.content)
    return r

# def post_add(request):
#     if request.method = 'POST':
#         form = forms.AddPostForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             url = post.get_url()
#             return HttpResponseRedirect(url)
#     else:
#         form = AddPostForm()
#     return render(request, '', {'form': form})


# @login_required
# def post_add2(request):
#     if request.method = 'POST':
#         form = forms.AddPostForm(request.user, request.POST)
#         if form.is_valid():
#             post = form.save()
#             url = post.get_url()
#             return HttpResponseRedirect(url)
#     else:
#         form = AddPostForm()
#     return render(request, '', {'form': form})

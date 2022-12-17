from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.template.context_processors import csrf
from django.urls import reverse

from . import models
from .forms import LoginForm, RegistrationForm, AskForm


def paginate(request, objects_list, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return paginator, page_obj


def index(request):
    QUESTIONS = models.Question.objects.all()
    paginator, page_obj = paginate(request, QUESTIONS, 3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    username = auth.get_user(request).username
    context = {'paginator': paginator,
               'page': page_obj,
               'popular_tags': models.POP_TAGS,
               'best_members': models.BEST_MEMBERS,
               'username': username}
    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    if question_id <= models.Question.objects.last().id:
        question_item = models.Question.objects.get(id=question_id)
        paginator, page_obj = paginate(request, question_item.get_answers(), 5)

        context = {'paginator': paginator,
                   'page': page_obj,
                   'popular_tags': models.POP_TAGS,
                   'question_item': question_item,
                   'best_members': models.BEST_MEMBERS}
        return render(request, 'question.html', context=context)
    else:
        return HttpResponse(status=404, content="Not found")


def login(request):
    print(request.GET)
    print(request.POST)
    if request.method == 'GET':
        user_form = LoginForm()
    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request=request, **user_form.cleaned_data)
            if user:
                return redirect(reverse('index'))
            else:
                user_form.add_error(field=None, error="Wrong username or password")

    return render(request, 'login.html', {'form': user_form})


def settings(request):
    return render(request, 'settings.html')


def new_question(request):
    if request.method == 'GET':
        ask_form = AskForm()
    if request.method == 'POST':
        ask_form = AskForm(request.POST)
        if ask_form:

            return redirect(reverse('index'))
        else:
            ask_form.add_error(field=None, error="Wrong question", )

    return render(request, 'new_question.html', {'form': ask_form})


def filter_tag(request):
    return render(request, 'filter_tag.html')


def signup(request):
    args = {}
    args.update(csrf(request))
    # user_form = RegistrationForm()
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        print(request.POST)
        print('not good yet')
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            print('good')
            return redirect(reverse('index'))
        else:
            print('oh no')
            args['form'] = newuser_form
    # if request.method == 'GET':
    #     user_form = RegistrationForm()
    # if request.method == 'POST':
    #     user_form = RegistrationForm(request.POST)
    #     if user_form.is_valid():
    #
    #         if user:
    #             return redirect(reverse('index'))
    #         else:
    #             user_form.add_error(field=None, error="Wrong username or password")
    # return render(request, 'signup.html')
    return render(request, 'signup.html', args)


def hot(request):
    return render(request, 'hot.html')


def tag(request, tag_id: str):
    if models.Tags.objects.filter(name=tag_id).count() > 0:
        tag = models.Tags.objects.get(name=tag_id)
        tag_questions = tag.tag_question()
        paginator, page_obj = paginate(request, tag_questions, 3)
        context = {'paginator': paginator,
                   'page': page_obj,
                   'tag': tag_id,
                   'pop_tags': models.POP_TAGS,
                   'best_members': models.BEST_MEMBERS}
        return render(request, 'tag.html', context=context)
    else:
        return HttpResponse(status=404, content="Not found such tag")


def logout(request):
    auth.logout(request)
    return redirect('/')
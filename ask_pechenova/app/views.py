from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from . import models


def index(request):
    paginator = Paginator(models.QUESTIONS, 3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {'paginator': paginator,
               'page': page_obj,
               'popular_tags': models.POP_TAGS,
               'best_members': models.BEST_MEMBERS}
    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    if question_id < len(models.QUESTIONS):
        question_item = models.QUESTIONS[question_id]
        paginator = Paginator(question_item['answers'], 3)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        context = {'paginator': paginator,
                   'page': page_obj,
                   'popular_tags': models.POP_TAGS,
                   'question_item': question_item,
                   'best_members': models.BEST_MEMBERS}
        return render(request, 'question.html', context=context)
    else:
        return HttpResponse(status=404, content="Not found")


def log_in(request):
    return render(request, 'log_in.html')


def settings(request):
    return render(request, 'settings.html')


def new_question(request):
    return render(request, 'new_question.html')


def filter_tag(request):
    return render(request, 'filter_tag.html')


def registration(request):
    return render(request, 'registration.html')


def hot(request):
    return render(request, 'hot.html')


def tag(request, tag_id: str):
    tag_questions = []
    for question_item in models.QUESTIONS:
        if tag_id in question_item['tags']:
            tag_questions.append(question_item)

    if len(tag_questions) > 0:
        paginator = Paginator(tag_questions, 3)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        context = {'paginator': paginator,
                   'page': page_obj,
                   'tag': tag_id,
                   'pop_tags': models.POP_TAGS,
                   'best_members': models.BEST_MEMBERS}
        return render(request, 'tag.html', context=context)
    else:
        return HttpResponse(status=404, content="Not found")
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


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
    context = {'paginator': paginator,
               'page': page_obj,
               'popular_tags': models.POP_TAGS,
               'best_members': models.BEST_MEMBERS}
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
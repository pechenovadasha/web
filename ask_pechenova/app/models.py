from django.db import models
HOT = [
    1, 2, 3
]

ANSWERS = [
    {
        'id': answer_id,
        'text': f'Text of answer #{answer_id}',

    }for answer_id in range(10)
]

QUESTIONS = [
    {
        'id': question_id,
        'title': f'Question #{question_id}',
        'text': f'Text of question #{question_id}',
        'tags': [f'tag{i}' for i in range(question_id)],
        'answers_number': question_id * question_id,
        'answers': ANSWERS,
    }for question_id in range(20)
]


POP_TAGS = [
    {'name': 'teg1', 'style': 'tegs line'},
    {'name': 'teg7', 'style': 'tegs line'},
    {'name': 'teg3', 'style': 'tegs line'}
]

BEST_MEMBERS = [
    {'name': 'Member 1'},
    {'name': 'Member 2'},
    {'name': 'Member 3'}
]
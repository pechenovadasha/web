import django.contrib.auth.backends
from django.db import models
from django.db.models import Count

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


class Member(models.Model):
    info = models.OneToOneField(django.contrib.auth.backends.UserModel, on_delete=models.CASCADE)
    avatar = models.ImageField(default='../static/img/img1.png')
    rank = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.info.__str__()

    def avatar(self):
        return self.avatar.name


class Question(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.CharField(max_length=10000)
    date = models.DateField(auto_now_add=True)
    like = models.ManyToManyField(Member, related_name="question_likes", blank=True)
    dislike = models.ManyToManyField(Member, related_name="question_dislikes", blank=True)
    author = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name="questions")

    def get_text(self):
        return self.text

    def get_date(self):
        return f'{self.date}'

    def get_author(self):
        return self.author

    def get_tags(self):
        return self.tags.all()

    def get_num_answers(self):
        return self.answers.all().count()

    def get_answers(self):
        return self.answers.all()

    def get_likes(self):
        return self.question_like.all().count()

    def get_dislikes(self):
        return self.question_dislike.all().count()

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.CharField(max_length=10000)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name="answers")
    is_correct = models.BooleanField(default=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,
                                 related_name="answers", related_query_name="answers")
    like = models.ManyToManyField(Member, related_name="answer_likes", blank=True)
    dislike = models.ManyToManyField(Member, related_name="answer_dislikes", blank=True)

    def __str__(self):
        return self.text

    def get_date(self):
        return f'{self.date}'

    def get_author(self):
        return self.author

    def get_likes(self):
        return self.like.all().count()

    def get_dislikes(self):
        return self.dislike.all().count()


class TagManager(models.Manager):
    def pop_tags(self):
        return self.all().annotate(rank=Count('questions')).order_by('rank').reverse()[:5]


class Tags(models.Model):
    name = models.CharField(max_length=100)
    question = models.ManyToManyField(Question, related_name="tags", related_query_name="tag")
    # question = models.ForeignKey(Question, related_name="tags",on_delete=models.CASCADE, related_query_name="tag")
    objects = TagManager()

    def rank(self) -> int:
        return self.question.all().count()

    def tag_question(self):
        return self.question.all()

    def __str__(self):
        return self.name


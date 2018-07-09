from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return Question.objects.order_by('-id')

    def popular(self):
        return self.order_by('-rating')

    def concreate(self, slug):
        try:
            question = Question.objects.get(pk=slug)
        except Question.DoesNotExist:
            question = None
        return question


class Question(models.Model):
    objects=QuestionManager()

    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)#, models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='likes_set')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.OneToOneField(Question, related_name='answer_set')
    author = models.ForeignKey(User)#, models.DO_NOTHING)

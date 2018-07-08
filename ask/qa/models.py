from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects=QuestionManager()

    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ManyToManyField(User, related_name='ques_author')
    likes = models.ManyToManyField(User, related_name='likes_set')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.OneToOneField(Question)
    author = models.ForeignKey(User, blank=True)

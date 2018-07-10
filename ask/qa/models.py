from django.db import models
from django.contrib.auth.models import User


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
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    # !!!!!!!!!!
    author = models.ForeignKey(User, blank=True, null=True) # models.DO_NOTHING,
    likes = models.ManyToManyField(User, related_name='likes_set', blank=True)

    def get_url(self):
        return '/question/{}/'.format(self.pk)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    # !!!!!!!!!!
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, blank=True, null=True)#, models.DO_NOTHING)

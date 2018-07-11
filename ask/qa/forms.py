from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate

from qa import models


class AskForm(forms.Form):
    title = forms.CharField(max_length=128)
    text = forms.CharField(widget=forms.Textarea)
    author = forms.HiddenInput()

    def clean(self):
        if len(self.cleaned_data['title']) == 0 or len(self.cleaned_data['text']) == 0:
            raise forms.ValidationError('Empty!')
        # return self.cleaned_data

    def save(self):
        # print(self.cleaned_data)
        question = models.Question(**self.cleaned_data)
        # question.author = self.user
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        if len(self.cleaned_data['text']) == 0:
            raise forms.ValidationError('Empty!')

    def clean_question(self):
        return models.Question.objects.concreate(self.cleaned_data['question'])

    def save(self):
        answer = models.Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    
    def clean_username(self):
        username = self.cleaned_data['username']
        # print(username)
        try:
            models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return username
        raise forms.ValidationError('User already exists.')


    def clean_email(self):
        email = self.cleaned_data['email']
        # print(email)
        try:
            models.User.objects.get(email=email)
        except models.User.DoesNotExist:
            return email
        raise forms.ValidationError('User already exists.')

    def save(self):
        # print(self.cleaned_data)
        user = models.User.objects.create_user(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        self._user = authenticate(username=username, password=password)
        if self._user is None:
            raise forms.ValidationError('User don`t exists.')
        # print(self._user.username)
        return self.cleaned_data
    
    def save(self):
        return self._user


# class FeedbackForm(forms.Form):
#     email = forms.EmailField(max_length=128)
#     message = forms.CharField(widget=forms.Textarea)

#     def clean(self):
#         if is_spam(self.cleaned_data):
#             raise forms.ValidationError('It`s spam!', code='spam')


# class AddPostForm(forms.Form):
#     title = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea)

#     def clean_message(self):
#         message = self.cleaned_data['message']
#         if not is_ethic(message):
#             raise forms.ValidationError('Incorrrect!', code=12)
#         return message + ' attention.'

#     def save(self):
#         post = Post(**self.cleaned_data)
#         post.save()
#         return post


# class ArticleForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'category', 'tags']


# class AddPost2Form(forms.Form):
#     def __init__(self, user, **kwargs):
#         self._user = user
#         super().__init__(**kwargs)

#     def clean(self):
#         if self._user.is_banned:
#             raise ValidationError('Access block')

#     def save(self):
#         self.cleaned_data['author'] = self._user
#         return Post.objects.create(**self.cleaned_data)

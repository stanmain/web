from django import forms
from django.forms import ModelForm


from qa import models


class AskForm(forms.Form):
    title = forms.CharField(max_length=128)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        if len(self.cleaned_data['title']) < 5 or len(self.cleaned_data['text']) < 5:
            raise forms.ValidationError('Empty!')
        # return self.cleaned_data

    def save(self):
        print(self.cleaned_data)
        question = models.Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.CharField(widget=forms.HiddenInput)

    def clean(self):
        if len(self.cleaned_data['text']) < 5:
            raise forms.ValidationError('Empty!')

    def clean_question(self):
        return models.Question.objects.concreate(self.cleaned_data['question'])

    def save(self):
        answer = models.Answer(**self.cleaned_data)
        answer.save()
        return answer


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

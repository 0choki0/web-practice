from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
#     title = forms.CharField(
#         label='제목입니다.',
#         widget=forms.TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )
#     title = forms.CharField(
#         label='내용입니다.',
#         widget=forms.TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )


    
    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('user', )
        # fields = ('title', 'content',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
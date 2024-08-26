from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        exclude = ("author", "like_users",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 제목 필드에 placeholder 추가
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력하세요'
        })
        # 내용 필드에 placeholder 추가
        self.fields['content'].widget.attrs.update({
            'placeholder': '내용을 입력하세요'
        })
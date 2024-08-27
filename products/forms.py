from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        exclude = ("author", "like_users",)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력하세요'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': '내용을 입력하세요'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '가격을 입력하세요'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import User


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="사용자ID",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="사용자ID",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="<li>귀하의 비밀번호는 귀하의 다른 개인정보와 너무 유사할 수 없습니다.</li><li>비밀번호는 8자 이상이어야 합니다.</li><li>비밀번호는 일반적으로 사용되는 비밀번호일 수 없습니다.</li><li>비밀번호는 숫자로만 구성할 수 없습니다.</li>"
    )

    password2 = forms.CharField(
        label="비밀번호 확인: ",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="<li>확인을 위해 이전과 동일한 비밀번호를 입력하세요.</li>"
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "email",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["first_name"].label = "이름"
        self.fields["last_name"].label = "성"
        self.fields["email"].label = "이메일"
        self.fields["password"].label = "비밀번호"

        if self.fields.get("password"):
            password_help_text = ("비밀번호 변경을 원하시면 " '<a href="{}">여기</a>를 눌러주세요.'
                                  ).format(f"{reverse('accounts:change_password')}")
            self.fields["password"].help_text = password_help_text

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 필드 라벨 수정
        self.fields['old_password'].label = "현재 비밀번호"
        self.fields['new_password1'].label = "새 비밀번호"
        self.fields['new_password2'].label = "새 비밀번호 확인"

        # (선택 사항) 도움말 텍스트 수정
        self.fields['new_password1'].help_text = "<li>8자 이상이어야 합니다.</li><li>비밀번호는 일반적으로 사용되는 비밀번호일 수 없습니다.</li><li>비밀번호는 숫자로만 구성될 수 없습니다.</li>"

        # (선택 사항) 필드의 위젯 속성 수정
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
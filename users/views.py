from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from products.models import Article
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


def users(request):
    return render(request, "users/users.html")


def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    user_articles = Article.objects.filter(
        author=member).order_by('-created_at')
    liked_articles = Article.objects.filter(
        like_users=member).order_by('-created_at')

    # 팔로워와 팔로잉 숫자를 계산
    followers_count = member.followers.count()
    following_count = member.following.count()

    context = {
        "member": member,
        "articles": user_articles,  # 사용자의 글 목록을 추가
        "liked_articles": liked_articles,  # 사용자가 찜한 글 목록 추가
        "followers_count": followers_count,
        "following_count": following_count,
    }
    return render(request, "users/profile.html", context)

# 팔로우 기능 구현


@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_id)
        if member != request.user:
            if member.followers.filter(pk=request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", username=member.username)
    else:
        return redirect("accounts:login")

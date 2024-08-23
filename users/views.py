from django.shortcuts import render
from products.models import Article


def users(request):
    return render(request, "users/users.html")


def profile(request):
    user_articles = Article.objects.filter(author=request.user).order_by('-created_at')
    liked_articles = Article.objects.filter(like_users=request.user).order_by('-created_at')

    
    context = {
        "username": request.user.username,
        "articles": user_articles,  # 사용자의 글 목록을 추가
        "liked_articles": liked_articles, #사용자가 찜한 글 목록 추가
    }
    
    return render(request, "users/profile.html", context)
from django.shortcuts import redirect, render, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.db.models import Count


# Create your views here.
@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "products/create.html", context)


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    article.views += 1
    article.save()

    formatted_price = f"{article.price:,.0f}"

    context = {
        "article": article,
        "formatted_price": formatted_price,
    }

    return render(request, "products/product_detail.html", context)



from django.db.models import Count
from .models import Article

def articles(request):
    sort_option = request.GET.get('sort', 'latest')

    if sort_option == 'popular':
        articles = Article.objects.annotate(
            like_count=Count('like_users')
        ).order_by("-like_count", "-pk").distinct()
    else:
        articles = Article.objects.annotate(
            like_count=Count('like_users')
        ).order_by("-pk").distinct()

    for article in articles:
        article.formatted_price = f"{article.price:,.0f}"

    context = {
        "articles": articles,
        "sort_option": sort_option,
    }
    return render(request, "products/products.html", context)




@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if article.author != request.user:
        return redirect("articles:articles")

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        "form": form,
        "article": article,
    }
    return render(request, "products/update.html", context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if article.author == request.user:
            article = get_object_or_404(Article, pk=pk)
            article.delete()
    return redirect("articles:articles")


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect("articles:article_detail", pk=pk)
    return redirect("accounts:login")


@require_POST
def like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user

    if user in article.like_users.all():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)

    # Save the article to update the like_users field
    article.save()

    # Return the new like count
    return JsonResponse({
        'success': True,
        'like_count': article.like_users.count()
    })

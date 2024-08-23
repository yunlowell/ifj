from django.shortcuts import redirect, render, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


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
    context = {
        "article": article,
    }
    
    return render(request, "products/product_detail.html", context)

def articles(request):
    articles = Article.objects.all().order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "products/products.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)


    context = {
        "form": form,
        "article": article,
    }
    return render(request, "products/update.html", context)


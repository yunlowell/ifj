from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

# Create your views here.
@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("products:article_detail", article.pk)
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "products/create.html", context)
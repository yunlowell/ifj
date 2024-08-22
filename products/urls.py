from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
]
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.users, name="users"),
    path("profile/", views.profile, name="profile"),
]

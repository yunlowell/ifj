from django.shortcuts import render


def users(request):
    return render(request, "users/users.html")


def profile(request):
    context = {
        "username": request.user.username,
    }
    return render(request, "users/profile.html", context)

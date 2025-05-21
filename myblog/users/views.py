from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

import users.models


@login_required
def me(request):
    template = "users/profile.html"
    user = get_object_or_404(users.models.User, username=request.user.username)
    context = {
        "user": user,
    }

    return render(request, template, context)


def get_user(request, user_id):
    template = "users/profile.html"
    user = get_object_or_404(users.models.User, id=user_id)
    context = {
        "user": user,
    }
    return render(request, template, context)

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

import users.forms
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


@login_required
def edit_profile(request, user_id):
    template = "users/includes/edit_profile.html"
    if request.user.id == user_id:
        user = get_object_or_404(users.models.User, id=user_id)
        if request.method == "POST":
            form = users.forms.EditUserForm(
                                            request.POST,
                                            request.FILES,
                                            instance=user)
            if form.is_valid():
                form.save()
                return redirect("profile")
        else:
            form = users.forms.EditUserForm(instance=user)
        context = {
            "form": form,
        }
    else:
        return HttpResponse("<h1>Not bad, dude, but chill...</h1>")
    return render(request, template, context)


@login_required
def delete_profile(request, user_id):
    if request.user.id == user_id and request.method == "POST":
        post = get_object_or_404(users.models.User, pk=user_id)
        post.delete()
    else:
        return HttpResponse("<h1>Don't try to delete users.</h1>")
    return redirect("items_list")
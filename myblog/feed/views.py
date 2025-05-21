import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

import comments.forms
import comments.models

import feed.forms
import feed.models


def items_list(request):
    template = "feed/index.html"
    posts = feed.models.Feed.objects.all()[:10][::-1]
    context = {
        "posts": posts,
    }
    return render(request, template, context)


def item_detail(request, pk):
    template = "feed/includes/detail.html"
    post = get_object_or_404(feed.models.Feed, id=pk)
    comms = post.comments.filter()
    comment_form = None
    if request.method == "POST" and request.user.is_authenticated:
        comment_form = comments.forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect("item_detail", pk=post.id)
    else:
        comment_form = comments.forms.CommentForm()

    context = {
        "post": post,
        "comments": comms,
        "comment_form": comment_form,
    }
    return render(request, template, context)


@login_required
def create_post(request):
    template = "feed/includes/create_post.html"
    if request.method == "POST":
        form = feed.forms.CreatePostFrom(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("item_detail", pk=post.id)
        else:
            form = feed.forms.CreatePostFrom()
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    template = "feed/includes/edit_post.html"
    post = get_object_or_404(feed.models.Feed, pk=post_id)
    if request.method == "POST":
        form = feed.forms.CreatePostFrom(request.POST,
                                         request.FILES,
                                         instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_edited = datetime.datetime.now()
            post.save()
            return redirect("items_list")
    else:
        form = feed.forms.CreatePostFrom(instance=post)
    context = {
        "post": post,
        "form": form,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(feed.models.Feed, pk=post_id)
        post.delete()
    return redirect("items_list")


@login_required
def like(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(feed.models.Feed, pk=post_id)
        user = request.user
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
        else:
            post.likes.add(user)

    return redirect(request.META.get("HTTP_REFERER", "feed"))


@login_required
def dislike(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(feed.models.Feed, pk=post_id)
        user = request.user
        if post.dislikes.filter(id=user.id).exists():
            post.dislikes.remove(user)
        else:
            post.dislikes.add(user)

    return redirect(request.META.get("HTTP_REFERER", "feed"))


@login_required
def edit_comment(request, comment_id):
    template = "feed/includes/edit_comment.html"
    comment = get_object_or_404(comments.models.Comments, pk=comment_id)
    if request.method == "POST":
        form = comments.forms.EditCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save(commit=False)
            return redirect("items_list")
    else:
        form = feed.forms.CreatePostFrom(instance=comment)
    context = {
        "comment": comment,
        "form": form,
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(comments.models.Comments, id=comment_id)
    if request.method == "POST" and comment.user == request.user:
        comment.delete()
    return redirect("items_list")


def switch_theme(request):
    current_theme = request.session.get("theme", "light")
    # Toggle theme
    if current_theme == "light":
        request.session["theme"] = "dark"
    else:
        request.session["theme"] = "light"
    # Redirect to the previous page or homepage
    return redirect(request.META.get("HTTP_REFERER", "/"))

from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

import account.forms
import account.tokens

import users.models


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = users.models.User.objects.get(pk=uid)
    except (OverflowError, TypeError, ValueError):
        user = None
    if user is not None and account.tokens.account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        from django.contrib.auth import login
        login(request, user)
        messages.success(request, "Thank you for your email confirmation. Now you can log in to your account.")
        return redirect("items_list")
    else:
        return HttpResponse("Activation link is invalid!")


def activateEmailMessage(request, user, user_form):
    mail_subject = "Blogly is here. Confirm your email."
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account.tokens.account_activation_token.make_token(user)
    message = render_to_string(
       "account/activate_account.html",
       {
            "user": user,
            "domain": request.get_host(),
            "uid": uid,
            "token": token,
        },
    )
    to_email = user_form.cleaned_data.get("email")
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
    messages.success(
        request,
        f"Dear {user.username}, please confirm your email. "
        f"We have sent the link to your email: {user.email}!",
    )


def register(request):
    template = "account/sign_up.html"
    if request.method == "POST":
        user_form = account.forms.CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_active = False
            user_form.save()
            activateEmailMessage(request, user, user_form)
            redirect("items_list")
    else:
        user_form = account.forms.CustomUserCreationForm(request.POST)
    return render(request, template, context={"user_form": user_form})


def register_done(request):
    template = "account/sing_up_done.html"
    context = {
        "user": request.user,
    }
    return render(request, template, context)

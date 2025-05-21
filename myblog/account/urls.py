import django.contrib.auth.views
import django.urls

import account.views


urlpatterns = [
    django.urls.path("sign_up/", view=account.views.register, name="sign_up"),
    django.urls.re_path(r"^account/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z\-]+)/$",
                        account.views.activate, name="activate"),
    django.urls.path(
        "sign_up_done/", view=account.views.register_done, name="sign_up_done",
    ),
    django.urls.path(
        "login/",
        view=django.contrib.auth.views.LoginView.as_view(
            template_name="account/login.html",
        ),
        name="login",
    ),
    django.urls.path(
        "logout/",
        view=django.contrib.auth.views.LogoutView.as_view(
            template_name="account/logout.html",
        ),
        name="logout",
    ),
    django.urls.path(
        "password_change/",
        view=django.contrib.auth.views.PasswordChangeView.as_view(
            template_name="account/password_change.html",
        ),
        name="password_change",
    ),
    django.urls.path(
        "password_change/done/",
        view=django.contrib.auth.views.PasswordChangeDoneView.as_view(
            template_name="account/password_change_done.html",
        ),
        name="password_change_done",
    ),
    django.urls.path(
        "password_reset/",
        view=django.contrib.auth.views.PasswordResetView.as_view(
            template_name="account/password_reset.html",
        ),
        name="password_reset",
    ),
    django.urls.path(
        "password_reset/done/",
        view=django.contrib.auth.views.PasswordResetDoneView.as_view(
            template_name="account/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    django.urls.path(
        "reset/<uidb64>/<token>/",
        view=django.contrib.auth.views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_confirm.html",
        ),
        name="password_reset_confirm",
    ),
    django.urls.path(
        "reset/done/",
        view=django.contrib.auth.views.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
]

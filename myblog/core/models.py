import django.db.models

import django_ckeditor_5.fields

import users.models


class AbstractPostModel(django.db.models.Model):
    name = django.db.models.CharField(
        name="name",
        max_length=150,
        verbose_name="Header of the post",
    )
    content = django_ckeditor_5.fields.CKEditor5Field(
        name="content",
        max_length=10000,
        verbose_name="Content",
        help_text="Max length is 10000 characters",
    )
    user = django.db.models.ForeignKey(
        users.models.User,
        verbose_name="User",
        on_delete=django.db.models.CASCADE,
    )

    class Meta:
        abstract = True

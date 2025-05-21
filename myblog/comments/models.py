import django.db.models

import feed.models

import users.models


class Comments(django.db.models.Model):
    name = django.db.models.CharField(
        name="name",
        max_length=150,
        verbose_name="Comment Header",
        help_text="Header of a comment",
    )
    content = django.db.models.TextField(
        name="content",
        max_length=5000,
        verbose_name="Comment Content",
        help_text="Max length 5000 characters",
    )
    post = django.db.models.ForeignKey(
        to=feed.models.Feed,
        on_delete=django.db.models.CASCADE,
        name="post",
        verbose_name="Post",
        related_name="comments",
    )
    # parent_comment = django.db.models.ForeignKey(
    #     to="self",
    #     on_delete=django.db.models.CASCADE,
    #     name="comment_parent_comment",
    #     verbose_name="Parent Comment",
    #     null=True,
    # )
    user = django.db.models.ForeignKey(
        to=users.models.User,
        on_delete=django.db.models.CASCADE,
        name="user",
        verbose_name="User",
    )
    created_on = django.db.models.DateTimeField(
        name="created_on",
        verbose_name="Created On",
        auto_now_add=True,
    )

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.user.username, self.name)

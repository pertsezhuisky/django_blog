import django.db.models

import core.models

import users.models


class Feed(core.models.AbstractPostModel):
    date_published = django.db.models.DateTimeField(
        name="date_published",
        verbose_name="Date posted",
        auto_now_add=True,
    )
    date_edited = django.db.models.DateTimeField(
        name="date_edited",
        verbose_name="Date edited",
        auto_now_add=True,
    )
    image = django.db.models.ImageField(
        name="image",
        upload_to="users_content/",
        verbose_name="Post image",
        null=True,
        blank=True,
    )
    likes = django.db.models.ManyToManyField(
        to=users.models.User,
        related_name="likes",
    )
    dislikes = django.db.models.ManyToManyField(
        to=users.models.User,
        related_name="dislikes",
    )

    def __str__(self) -> str:
        return str(self.name)

    @property
    def get_like_score(self):
        return self.likes.count() - self.dislikes.count()

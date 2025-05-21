import django.contrib.admin

import feed.models


@django.contrib.admin.register(feed.models.Feed)
class FeedChangeFields(django.contrib.admin.ModelAdmin):
    list_display = (
        feed.models.Feed.name.field.name,
        feed.models.Feed.content.field.name,
        feed.models.Feed.date_published.field.name,
        feed.models.Feed.date_edited.field.name,
        feed.models.Feed.image.field.name,
        feed.models.Feed.user.field.name,
    )

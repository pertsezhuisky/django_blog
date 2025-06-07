import django.urls

import feed.views


urlpatterns = [
    django.urls.path("", feed.views.items_list, name="items_list"),
    django.urls.path("<int:pk>/", feed.views.item_detail, name="item_detail"),
    django.urls.path("create/", feed.views.create_post, name="create_post"),
    django.urls.path("edit/<int:post_id>",
                     feed.views.edit_post,
                     name="edit_post"),
    django.urls.path("delete/<int:post_id>",
                     feed.views.delete_post,
                     name="delete_post"),
    django.urls.path("like/<int:post_id>",
                     feed.views.like,
                     name="like"),
    django.urls.path("dislike/<int:post_id>",
                     feed.views.dislike,
                     name="dislike"),
    django.urls.path("comment/edit/<int:post_id>/<int:comment_id>",
                     feed.views.edit_comment,
                     name="edit_comment"),
    django.urls.path("comment/delete/<int:comment_id>",
                     feed.views.delete_comment,
                     name="delete_comment"),
    django.urls.path("switch-theme/",
                     feed.views.switch_theme,
                     name="switch_theme"),
]

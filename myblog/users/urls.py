import django.urls

import users.views

urlpatterns = [
    django.urls.path("me/", users.views.me, name="profile"),
    django.urls.path("<int:user_id>/", users.views.get_user, name="user_profile"),
    django.urls.path("edit/<int:user_id>", users.views.edit_profile, name="edit_profile"),
    django.urls.path("delete/<int:user_id>", users.views.delete_profile, name="delete_profile"),
]

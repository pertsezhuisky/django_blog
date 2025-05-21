import django.urls

import users.views

urlpatterns = [
    django.urls.path("me/", users.views.me, name="profile"),
    django.urls.path("<int:user_id>/", users.views.get_user, name="user_profile"),
]

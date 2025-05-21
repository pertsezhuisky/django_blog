import django.contrib.admin

import users.models


@django.contrib.admin.register(users.models.User)
class UserChangeFields(django.contrib.admin.ModelAdmin):
    list_display = (
        users.models.User.username.field.name,
        users.models.User.email.field.name,
        users.models.User.bio.field.name,
        users.models.User.date_birth.field.name,
        users.models.User.date_joined.field.name,
        users.models.User.avatar.field.name,
    )
    list_filter = (
        users.models.User.username.field.name,
        users.models.User.email.field.name,
        users.models.User.date_birth.field.name,
        users.models.User.date_joined.field.name,
    )

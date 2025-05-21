from django.contrib import admin

import comments.models


@admin.register(comments.models.Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        comments.models.Comments.name.field.name,
        comments.models.Comments.content.field.name,
        comments.models.Comments.user.field.name,
        comments.models.Comments.created_on.field.name,
        comments.models.Comments.post.field.name,
    )
    list_filter = (
        comments.models.Comments.created_on.field.name,
    )
    search_fields = (
        comments.models.Comments.name.field.name,
        comments.models.Comments.user.field.name,
    )
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

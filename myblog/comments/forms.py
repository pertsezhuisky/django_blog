import django.forms

import comments.models


class CommentForm(django.forms.ModelForm):
    class Meta:
        model = comments.models.Comments
        fields = [
            comments.models.Comments.name.field.name,
            comments.models.Comments.content.field.name,
            comments.models.Comments.image.field.name,
        ]


class EditCommentForm(CommentForm):
    pass

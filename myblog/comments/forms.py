import django.forms

import django_ckeditor_5.widgets

import comments.models


class CommentForm(django.forms.ModelForm):
    class Meta:
        model = comments.models.Comments
        fields = [
            comments.models.Comments.name.field.name,
            comments.models.Comments.content.field.name,
        ]
        widgets = {
              "text": django_ckeditor_5.widgets.CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="comment"),
          }


class EditCommentForm(CommentForm):
    pass

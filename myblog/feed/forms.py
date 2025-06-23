import django.forms
from django.core.exceptions import ValidationError

import django_ckeditor_5.widgets

import feed.models


class CreatePostFrom(django.forms.ModelForm):
    class Meta:
        model = feed.models.Feed
        fields = (
            feed.models.Feed.name.field.name,
            feed.models.Feed.content.field.name,
        )
        widgets = {
              "text": django_ckeditor_5.widgets.CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="comment"),
          }

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image and image.size > 4 * 1024 * 1024:
            raise ValidationError("Image file too large ( > 4mb )")
        return image


class EditPostForm(CreatePostFrom):
    pass

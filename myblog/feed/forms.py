import django.forms
from django.core.exceptions import ValidationError

import feed.models


class CreatePostFrom(django.forms.ModelForm):
    class Meta:
        model = feed.models.Feed
        fields = (
            feed.models.Feed.name.field.name,
            feed.models.Feed.content.field.name,
            feed.models.Feed.image.field.name,
        )

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image and image.size > 4 * 1024 * 1024:
            raise ValidationError("Image file too large ( > 4mb )")
        return image


class EditPostForm(CreatePostFrom):
    pass

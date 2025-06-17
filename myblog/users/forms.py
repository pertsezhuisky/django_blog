import django.forms
from django.core.exceptions import ValidationError

import users.models


class UserFrom(django.forms.ModelForm):
    class Meta:
        model = users.models.User
        fields = (
            users.models.User.first_name.field.name,
            users.models.User.last_name.field.name,
            users.models.User.bio.field.name,
            users.models.User.date_birth.field.name,
            users.models.User.avatar.field.name,
            )

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image and image.size > 4 * 1024 * 1024:
            raise ValidationError("Image file too large ( > 4mb )")
        return image


class EditUserForm(UserFrom):
    pass

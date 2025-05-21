from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.contrib.auth.forms import UserCreationForm

import users.models


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = users.models.User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Continue", css_class="btn btn-primary w-100"))

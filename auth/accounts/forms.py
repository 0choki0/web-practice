from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUsercreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class CustomAuthenticationForm(AuthenticationForm):
    pass
from django.contrib.auth.forms import UserCreationForm
from . models import User

class CustomUserFreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'profile_image', )
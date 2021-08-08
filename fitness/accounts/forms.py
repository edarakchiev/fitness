from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from fitness.accounts.models import FitnessUser
from fitness.core.forms import BootstrapFormMixin


class LoginForm(AuthenticationForm):
    pass


class UserForm(BootstrapFormMixin, UserCreationForm):
    class Meta:
        model = FitnessUser
        fields = ('first_name', 'last_name', 'email', 'profile_image')

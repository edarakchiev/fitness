from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from fitness.accounts.models import FitnessUser
from fitness.core.forms import BootstrapFormMixin


class LoginForm(BootstrapFormMixin, AuthenticationForm):
    pass


class UserForm(BootstrapFormMixin, UserCreationForm):
    class Meta:
        model = FitnessUser
        fields = ('first_name', 'last_name', 'email')


class EditUserForm(BootstrapFormMixin, ModelForm):
    class Meta:
        model = FitnessUser
        fields = ('first_name', 'last_name', 'profile_image',)

from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from fitness.accounts.models import Profile
from fitness.core.forms import BootstrapFormMixin

UserModel = get_user_model()


class LoginForm(AuthenticationForm):
    pass


class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)


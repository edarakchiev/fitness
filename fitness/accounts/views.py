from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from fitness.accounts.forms import LoginForm, ProfileForm, RegistrationForm
from fitness.accounts.models import Profile
from fitness.fitness_workout_app.models import Workout


class LoginUserView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
    redirect_field_name = 'index'


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'register_user.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


# class LogoutUser(LogoutView):
#     pass

def logout_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(FormView):
    template_name = 'user_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile details')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.profile_image = form.cleaned_data['profile_image']
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['workouts'] = Workout.objects.filter(id=self.request.user.id)
        context['profile'] = self.object

        return context

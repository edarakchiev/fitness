from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from fitness.accounts.forms import LoginForm, UserForm, EditUserForm
from fitness.accounts.models import  FitnessUser
from fitness.fitness_workout_app.models import Workout


class LoginUserView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
    redirect_field_name = 'index'


class RegisterView(CreateView):
    form_class = UserForm
    template_name = 'register_user.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class LogoutUser(LogoutView):
    def get(self, request):
        logout(request)
        return redirect('index')


class EditProfile(UpdateView):
    model = FitnessUser
    form_class = EditUserForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('index')


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'user_profile.html'
    model = FitnessUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['workouts'] = Workout.objects.filter(user_id=self.request.user.id)

        return context


class DeleteUserView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_user.html'
    model = FitnessUser
    success_url = reverse_lazy('index')

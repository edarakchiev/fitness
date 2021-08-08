from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, UpdateView, DetailView

from fitness.accounts.forms import LoginForm, UserForm
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


# class LogoutUser(LogoutView):
#     pass

def logout_user(request):
    logout(request)
    return redirect('index')


class EditProfile(UpdateView):
    model = FitnessUser
    # form_class = RegistrationForm
    template_name = 'edit_profile.html'
    fields = ('first_name', 'last_name', 'profile_image',)
    success_url = 'index'


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'user_profile.html'
    model = FitnessUser
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['workouts'] = Workout.objects.filter(user_id=self.request.user.id)

        return context


# class ProfileDetailsView(LoginRequiredMixin, FormView):
#     template_name = 'user_profile.html'
#     form_class = FitnessUser
#     success_url = reverse_lazy('profile details')
#     context_object_name = 'user'
#     object = None
#
#     def get(self, request, *args, **kwargs):
#         self.object = FitnessUser.objects.get(pk=request.user.id)
#         return super().get(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         self.object = FitnessUser.objects.get(pk=request.user.id)
#         return super().post(request, *args, **kwargs)
#
#     # def form_valid(self, form):
#     #     self.object.profile_image = form.cleaned_data['profile_image']
#     #     self.object.save()
#     #     return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['workouts'] = Workout.objects.filter(id=self.request.user.id)
#         context['profile'] = self.object
#
#         return context

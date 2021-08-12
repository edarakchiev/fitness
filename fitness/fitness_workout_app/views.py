from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from fitness.fitness_workout_app.forms import CreateWorkoutForm
from fitness.fitness_workout_app.models import Workout


class IndexView(ListView):
    model = Workout
    template_name = 'index.html'
    context_object_name = 'workouts'


class WorkoutDetailsView(LoginRequiredMixin, DeleteView):
    model = Workout
    template_name = 'details_workout.html'
    context_object_name = 'workout'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workout = context['workout']
        context['is_owner'] = workout.user == self.request.user
        return context


class CreateWorkoutView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = CreateWorkoutForm

    template_name = 'create_workout.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        workout = form.save(commit=False)
        workout.user = self.request.user
        workout.save()
        return super().form_valid(form)


class EditWorkoutView(LoginRequiredMixin, UpdateView):
    model = Workout
    form_class = CreateWorkoutForm
    template_name = 'edit_workout.html'
    success_url = reverse_lazy('index')


class DeleteWorkoutView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_workout.html'
    model = Workout
    success_url = reverse_lazy('index')

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from fitness.fitness_workout_app.models import Workout


class IndexView(ListView):
    model = Workout
    template_name = 'index.html'
    context_object_name = 'workouts'


class WorkoutDetailsView(DeleteView):
    model = Workout
    template_name = 'details_workout.html'
    context_object_name = 'workout'


class CreateWorkoutView(CreateView):
    model = Workout
    fields = '__all__'
    template_name = 'create_workout.html'
    success_url = reverse_lazy('index')


class EditWorkoutView(UpdateView):
    model = Workout
    fields = '__all__'
    template_name = 'edit_workout.html'
    success_url = reverse_lazy('index')


class DeleteWorkoutView(DeleteView):
    template_name = 'delete_wokout.html'
    model = Workout
    success_url = reverse_lazy('index')

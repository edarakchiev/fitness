from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from fitness.fitness_workout_app.models import Workout


class IndexView(ListView):
    model = Workout
    template_name = 'index.html'
    context_object_name = 'workouts'


class WorkoutDetailsView(ListView):
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
    template_name = 'create_workout.html'
    success_url = reverse_lazy('index')


class DeleteWorkoutView(DeleteView):
    model = Workout
    success_url = 'index'

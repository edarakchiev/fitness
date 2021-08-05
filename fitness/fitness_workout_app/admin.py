from django.contrib import admin

from fitness.fitness_workout_app.models import Workout


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    pass
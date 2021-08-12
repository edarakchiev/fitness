from django.forms import ModelForm

from fitness.core.forms import BootstrapFormMixin
from fitness.fitness_workout_app.models import Workout


class CreateWorkoutForm(BootstrapFormMixin, ModelForm):
    class Meta:
        model = Workout
        fields = ('muscle_group', 'title', 'schema', 'series', 'repetitions', 'description')



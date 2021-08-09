from fitness.accounts.models import FitnessUser
from fitness.fitness_workout_app.models import Workout


class WorkoutTestUtils:
    def create_workout(self, **kwargs):
        return Workout.objects.create(**kwargs)

    def create_user(self, **kwargs):
        return FitnessUser.objects.create(**kwargs)
from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Workout(models.Model):
    TYPE_CHOICES = (
        ('Chest', 'Chest'),
        ('Back', 'Back'),
        ('Arms', 'Arms'),
        ('Abdominals', 'Abdominals'),
        ('Legs', 'Legs'),
        ('Shoulders', 'Shoulders'),
        ('Cardio', 'Cardio'),
    )

    muscle_group = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
    )
    title = models.CharField(
        max_length=30
    )
    schema = models.ImageField(
        upload_to='schema',
    )
    series = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
    description = models.TextField()
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE
    )

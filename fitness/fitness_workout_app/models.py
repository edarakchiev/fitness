from django.db import models


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
    series = models.IntegerField()
    repetitions = models.IntegerField()
    description = models.TextField()


class Like(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

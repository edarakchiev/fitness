from django.db import models


class Workout(models.Model):
    schema = models.ImageField(
        upload_to='schema',
    )
    description = models.TextField()

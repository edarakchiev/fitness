# Generated by Django 3.2.6 on 2021-08-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_workout_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='repetitions',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='workout',
            name='series',
            field=models.PositiveIntegerField(),
        ),
    ]
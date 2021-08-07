# Generated by Django 3.2.6 on 2021-08-07 19:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210807_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessuser',
            name='first_name',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fitnessuser',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fitnessuser',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profiles'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]

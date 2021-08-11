from django.urls import reverse

from fitness.fitness_workout_app.models import Workout
from tests.base.mixins import WorkoutTestUtils
from tests.base.tests import FitnessTestCase


class WorkoutDetailsTest(WorkoutTestUtils, FitnessTestCase):

    def test_workoutDetails_whenUserIsOwner(self):
        self.client.force_login(self.user)
        workout = self.create_workout(
            muscle_group='Chest',
            title='test title',
            schema='image.png',
            series=3,
            repetitions=7,
            description='test description',
            user=self.user
        )
        response = self.client.get(reverse('workout details', kwargs={'pk': workout.id}))

        self.assertTrue(response.context['is_owner'])

    def test_workoutDetails_whenUserIsNotOwner(self):
        user = self.create_user(email='emo@emo.bg', password='112233qqwwee')
        self.client.force_login(user)

        workout = self.create_workout(
            muscle_group='Chest',
            title='test title',
            schema='image.png',
            series=3,
            repetitions=7,
            description='test description',
            user=self.user
        )
        response = self.client.get(reverse('workout details', kwargs={'pk': workout.id}))

        self.assertFalse(response.context['is_owner'])

    def test_details_statusCode(self):
        self.client.force_login(self.user)
        response = self.client.get('')

        self.assertEqual(response.status_code, 200)

    def test_indexView_when_userIsLoggedIn(self):
        self.client.force_login(self.user)

        workout = self.create_workout(
            muscle_group='Chest',
            title='test title',
            schema='image.png',
            series=3,
            repetitions=7,
            description='test description',
            user=self.user
        )

        response = self.client.get(reverse('index'))

        self.assertEqual(list(response.context['workouts']), [workout])

    def test_IndexTemplateUsed(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_numberOfWorkouts(self):
        self.client.force_login(self.user)
        self.assertEqual(Workout.objects.all().count(), 0)

    def test_data(self):
        workout = Workout.objects.create(muscle_group='Chest', title='test title', schema='image.png', series=3,
                                         repetitions=7, description='test description', user=self.user)

        self.assertEqual(workout.muscle_group, 'Chest')
        self.assertEqual(workout.title, 'test title')
        self.assertEqual(workout.schema, 'image.png')
        self.assertEqual(workout.series, 3)
        self.assertEqual(workout.repetitions, 7)
        self.assertEqual(workout.description, 'test description')

    def test_statusCodeEdit_whenLoggedInUserAndUserIsOwner(self):
        workout = Workout.objects.create(muscle_group='Chest', title='test title', schema='image.png', series=3,
                                         repetitions=7, description='test description', user=self.user)

        self.client.force_login(self.user)

        response = self.client.get(reverse('edit workout', kwargs={'pk': workout.id}))

        self.assertEqual(workout.user, self.user)
        self.assertEqual(response.status_code, 200)

    def test_deleteWorkout(self):
        self.client.force_login(self.user)

        workout = Workout.objects.create(muscle_group='Chest', title='test title', schema='image.png', series=3,
                                         repetitions=7, description='test description', user=self.user)

        get_response = self.client.get(reverse('delete workout', kwargs={'pk': workout.id}), follow=True)
        self.assertContains(get_response, 'Delete Workouts')

        post_response = self.client.post(reverse('delete workout', kwargs={'pk': workout.id}), follow=True)
        self.assertRedirects(post_response, reverse('index'), status_code=302)

    def test_createView(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('create workout'),
                                        {
            'muscle_group': 'Chest',
            'title': 'test title',
            'schema': 'image.png',
            'series': 3,
            'repetitions': 7,
            'description': 'test description',
            'user': self.user
        }
        )
        self.assertEqual(response.status_code, 200)

    def test_CreateTemplateUsed(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create workout'))
        self.assertTemplateUsed(response, 'create_workout.html')

    def test_statusCodeCreate_whenLoggedInUser(self):
        self.client.force_login(self.user)
        response = self.client.post('/create_workout/')
        self.assertEqual(response.status_code, 200)
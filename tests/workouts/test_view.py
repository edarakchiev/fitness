from django.urls import reverse

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



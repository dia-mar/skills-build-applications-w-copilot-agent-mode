from django.test import TestCase
from rest_framework.test import APIClient
from .models import Team, User, Activity, Workout, Leaderboard

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=spiderman, activity='Running', duration=30)
        Workout.objects.create(name='Full Body', suggested_for='All')
        Leaderboard.objects.create(user=spiderman, points=120)

    def test_api_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)

    def test_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

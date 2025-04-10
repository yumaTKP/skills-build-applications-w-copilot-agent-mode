from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test User', age=20)
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Team Test')
        self.assertEqual(team.name, 'Team Test')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='test@example.com', name='Test User', age=20)
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30)
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Team Test')
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Yoga', description='Morning Yoga Session')
        self.assertEqual(workout.name, 'Yoga')
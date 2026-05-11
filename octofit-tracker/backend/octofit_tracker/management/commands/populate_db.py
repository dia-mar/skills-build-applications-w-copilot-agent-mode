from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from bson import ObjectId
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Teams
        marvel_id = ObjectId()
        dc_id = ObjectId()
        teams = [
            {'_id': marvel_id, 'name': 'Team Marvel'},
            {'_id': dc_id, 'name': 'Team DC'},
        ]
        db.teams.insert_many(teams)

        # Users
        users = [
            {'_id': ObjectId(), 'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team_id': marvel_id},
            {'_id': ObjectId(), 'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': marvel_id},
            {'_id': ObjectId(), 'name': 'Batman', 'email': 'batman@dc.com', 'team_id': dc_id},
            {'_id': ObjectId(), 'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': dc_id},
        ]
        db.users.insert_many(users)
        db.users.create_index([('email', 1)], unique=True)

        # Activities
        activities = [
            {'_id': ObjectId(), 'user_email': 'spiderman@marvel.com', 'activity': 'Running', 'duration': 30},
            {'_id': ObjectId(), 'user_email': 'ironman@marvel.com', 'activity': 'Cycling', 'duration': 45},
            {'_id': ObjectId(), 'user_email': 'batman@dc.com', 'activity': 'Swimming', 'duration': 60},
            {'_id': ObjectId(), 'user_email': 'wonderwoman@dc.com', 'activity': 'Yoga', 'duration': 50},
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {'_id': ObjectId(), 'name': 'Full Body', 'suggested_for': 'All'},
            {'_id': ObjectId(), 'name': 'Cardio Blast', 'suggested_for': 'Marvel'},
            {'_id': ObjectId(), 'name': 'Strength Builder', 'suggested_for': 'DC'},
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {'_id': ObjectId(), 'user_email': 'spiderman@marvel.com', 'points': 120},
            {'_id': ObjectId(), 'user_email': 'ironman@marvel.com', 'points': 110},
            {'_id': ObjectId(), 'user_email': 'batman@dc.com', 'points': 130},
            {'_id': ObjectId(), 'user_email': 'wonderwoman@dc.com', 'points': 125},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

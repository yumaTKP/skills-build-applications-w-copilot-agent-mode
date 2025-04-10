# Test data for octofit_db

def get_test_data():
    return {
        "users": [
            {"email": "user1@example.com", "name": "User One", "age": 25},
            {"email": "user2@example.com", "name": "User Two", "age": 30}
        ],
        "teams": [
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]}
        ],
        "activities": [
            {"user": "user1@example.com", "activity_type": "Running", "duration": 30},
            {"user": "user2@example.com", "activity_type": "Cycling", "duration": 45}
        ],
        "leaderboard": [
            {"team": "Team Alpha", "score": 100}
        ],
        "workouts": [
            {"name": "Morning Yoga", "description": "A relaxing morning yoga session"}
        ]
    }

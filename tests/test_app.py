import copy

from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


def test_unregister_participant_from_activity():
    original_participants = copy.deepcopy(activities["Chess Club"]["participants"])

    try:
        response = client.delete(
            "/activities/Chess Club/signup",
            params={"email": "michael@mergington.edu"},
        )

        assert response.status_code == 200
        assert "Unregistered" in response.json()["message"]

        updated_activities = client.get("/activities").json()
        assert "michael@mergington.edu" not in updated_activities["Chess Club"]["participants"]
    finally:
        activities["Chess Club"]["participants"] = original_participants

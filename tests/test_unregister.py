from urllib.parse import quote

from src.app import activities


def _unregister_path(activity_name):
    return f"/activities/{quote(activity_name, safe='')}/signup"


def test_unregister_removes_existing_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = activities[activity_name]["participants"][0]
    assert email in activities[activity_name]["participants"]

    # Act
    response = client.delete(_unregister_path(activity_name), params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]


def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "someone@mergington.edu"

    # Act
    response = client.delete(_unregister_path(activity_name), params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_returns_404_when_student_not_signed_up(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not.enrolled@mergington.edu"
    assert email not in activities[activity_name]["participants"]

    # Act
    response = client.delete(_unregister_path(activity_name), params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Student is not signed up for this activity"}

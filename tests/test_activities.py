def test_get_activities_returns_all_activities_with_expected_fields(client):
    # Arrange
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert data

    first_activity = next(iter(data.values()))
    assert expected_fields.issubset(first_activity.keys())
    assert isinstance(first_activity["participants"], list)

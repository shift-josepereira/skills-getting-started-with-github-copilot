import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

_original_activities = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Keep tests independent by restoring in-memory state around each test."""
    # Arrange
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))

    yield

    # Cleanup
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))


@pytest.fixture
def client():
    # Arrange
    return TestClient(app)

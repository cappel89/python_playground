from unittest import mock

import pytest

from python_playground.simple_test import Dependency, SimpleTest


@pytest.fixture
def simple_test():
    """Fixture to create a SimpleTest instance."""
    mock_dependency = mock.MagicMock(spec=Dependency)
    return SimpleTest(name="Test", injected_dependency=mock_dependency)


def test_add(simple_test):
    """Test the add method of SimpleTest."""
    assert simple_test.add(1, 2) == 3
    assert simple_test.add(-1, 1) == 0
    assert simple_test.add(0, 0) == 0

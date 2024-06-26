"""
This module contains unit tests for the `simulate_zombie_outbreak` function in
the `zombie_outbreak_sim` module.
"""

import pytest
from zombie_outbreak_sim import City, simulate_zombie_outbreak


@pytest.fixture
def city():
    """Initial city grid for testing. H: Human, Z: Zombie, E: Empty"""
    initial_grid = [
        ["H", "H", "H", "Z"],
        ["H", "H", "E", "H"],
        ["H", "H", "H", "H"],
        ["H", "H", "H", "H"],
    ]
    return City(initial_grid)


@pytest.fixture
def expected_grid_after_1_day():
    """City grid after 1 day of simulation. H: Human, Z: Zombie, E: Empty"""
    return [
        ["H", "H", "Z", "Z"],
        ["H", "H", "E", "Z"],
        ["H", "H", "H", "H"],
        ["H", "H", "H", "H"],
    ]


@pytest.fixture
def expected_grid_after_3_days():
    """City grid after 3 days of simulation. H: Human, Z: Zombie, E: Empty"""
    return [
        ["Z", "Z", "Z", "Z"],
        ["H", "Z", "E", "Z"],
        ["H", "H", "Z", "Z"],
        ["H", "H", "H", "Z"],
    ]


def test_day_1_simulation(city, expected_grid_after_1_day):
    """Test case for 1 day simulation"""
    result_after_1_day = simulate_zombie_outbreak(city, 1)
    assert result_after_1_day == expected_grid_after_1_day, "Test case for 1 day failed"


def test_day_3_simulation(city, expected_grid_after_3_days):
    """Test case for 3 days simulation"""
    result_after_3_days = simulate_zombie_outbreak(city, 3)
    assert (
        result_after_3_days == expected_grid_after_3_days
    ), "Test case for 3 days failed"


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
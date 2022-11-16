from logic import Ball
import pytest


balls1 = [(1.0), (3.5), (2.3)]


@pytest.mark.parametrize('radius', balls1)
def test_balls1(radius: float):
    """Function tests if the radius of ball.

    Args:
        radius (float): radius of a ball.
    """
    assert Ball(radius).radius == radius


@pytest.mark.xfail(raises=Exception)
def test_validball():
    """Function tests the existence of ball."""
    assert Ball(-1).is_valid()


balls2 = [(2.0, 3.0, 4.0, 343.77), (3.0, 5.4, 3.0, 309.4), (5.4, 3.0, 2.5, 79.58)]


@pytest.mark.parametrize('radius, speed, time, answer', balls2)
def test_balls2(radius: float, speed: float, time: float, answer: float):
    """Function tests a method evenMovement of Ball.

    Args:
        radius (float): radius of ball.
        speed (float): speed of ball.
        time (float): ball movement time.
        answer (float): expected response.
    """
    assert Ball(radius).evenMovement(speed, time) == answer


balls3 = [(1.0, 2.0, 4.0, 196.73), (2.3, 4.0, 3.2, 150.18), (5.6, 4.5, 4.5, 106.17)]


@pytest.mark.parametrize('radius, accel, time, answer', balls3)
def test_balls3(radius: float, accel: float, time: float, answer: float):
    """Function tests a method acceleratedMovement of Ball.

    Args:
        radius (float): radius of ball.
        accel (float): speed of ball.
        time (float): ball movement time.
        answer (float): expected response.
    """
    assert Ball(radius).acceleratedMotion(accel, time) == answer

"""Class of ball with validation and movement methods."""
from math import pi


class Ball:

    def __init__(self, radius: float) -> None:
        """Ball initialization. If this ball doesn't exists raise error.
        Args:
            radius (float): radius of ball.
        Raises:
            Exception: if radius of ball isn't valid.
        """
        self.radius = radius
        self.length = 2 * pi * self.radius
        if not self.is_valid():
            raise Exception

    def is_valid(self) -> bool:
        """Check if such a ball exists.
        Returns:
            bool: result.
        """
        if not isinstance(self.radius, float):
            return False
        return self.radius > 0

    def evenMovement(self, speed: float, time: float) -> float:
        """Counts the angle of deviation of the ball point with even motion.
        Rounds it to the 2nd digit after the dot.
        Args:
            speed (float): speed of ball.
            time (float): ball movement time.
        
        Raises:
            Exception: if time or speed isn't valid.
        """
        if not isinstance(speed, float) or speed < 0:
            return False
        if not isinstance(time, float) or time < 0:
            return False
        result = round((speed * time) / (self.length) * 360, 2)
        while result > 360:
            result -= 360
        return round(result, 2)

    def acceleratedMotion(self, accel: float, time: float) -> float:
        """Counts the angle of deviation of the ball point with accelerated motion.
        Rounds it to the 2nd digit after the dot.
        Args:
            accel (float): acceleration of ball.
            time (float): ball movement time.
        
        Raises:
            Exception: if time or acceleration isn't valid.
        """
        if not isinstance(accel, float) or accel < 0:
            return False
        if not isinstance(time, float) or time < 0:
            return False
        movement = (accel * (time ** 2)) / 2
        result = movement / self.length * 360
        while result > 360:
            result -= 360
        return round(result, 2)

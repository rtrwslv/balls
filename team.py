from math import pi

class Ball:

    def __init__(self, radius: float):
        """Init

        Args:
            radius (float): radius of ball.

        Raises:
            Exception: if radius of ball isn't valid.
        """
        self.radius = radius
        if not self.is_valid():
            raise Exception
    
    def motion(self, speed: float, time: float):
        """

        Args:
            speed (float): _description_
            time (float): _description_
        """
        result = (speed * time) / (2 * pi * self.radius) * 360
        while result > 360:
            result -= 360
        return round(result, 2)
    
    def acceleration(self, accel, time):
        """

        Args:
            speed (float): _description_
            time (float): _description_
        """
        movement = (accel * (time ** 2)) / 2
        result = movement / self.length * 360
        while result > 360:
            result -= 360
        return round(result, 2)
    
    def is_valid(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if not isinstance(self.radius, (float, int)):
            return False
        return self.radius > 0

#print(balls = Ball(-1))    
ball = Ball(1)
print(ball.motion(4, 1))
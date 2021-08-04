import math


class Charge:
    def __init__(self, **kwargs):
        self.magnitude = kwargs.get('magnitude') * 10e5
        self.position = kwargs.get('position')

    def get_sq_distance_from(self, position: tuple):
        return (self.position[0] - position[0]) ** 2 + (self.position[1] - position[1]) ** 2

    def get_component_factors(self, position: tuple):
        if self.position[0] == position[0]:
            return 0, 1
        slope = (self.position[1] - position[1]) / (self.position[0] - position[0])
        angle = math.atan(slope)
        return math.cos(angle), math.sin(angle)

    def get_shifted_position(self):
        return self.position[0] - 10, self.position[1] - 10


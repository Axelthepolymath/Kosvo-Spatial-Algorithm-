#Primary Goal: This code models spatial relationships by determining distance, activating a third-person perspective, identifying direction, and simulating rotational movement (Loom) around an object.

import math

class SpatialObserver:
    def __init__(self, observer_position):
        self.observer_position = observer_position

    def distance(self, object_position):
        """Calculate distance between observer and object."""
        x1, y1 = self.observer_position
        x2, y2 = object_position

        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def check_relationship(self, object_position):
        """Determine if the observer is near or far from the object."""
        d = self.distance(object_position)

        if d < 5:
            return "Observer is beside/near the object. Loom analysis is limited."

        else:
            return "Observer is far away. Third perspective activated."

    def third_perspective(self, object_position):
        """Determine viewing direction from a distant perspective."""
        ox, oy = self.observer_position
        x, y = object_position

        dx = x - ox
        dy = y - oy

        if abs(dx) > abs(dy):
            if dx > 0:
                return "East perspective"
            else:
                return "West perspective"
        else:
            if dy > 0:
                return "North perspective"
            else:
                return "South perspective"

    def loom(self, object_position, radius=10, steps=8):
        """Create circular rotational movement around an object."""
        x, y = object_position

        positions = []

        for i in range(steps):
            angle = (2 * math.pi / steps) * i

            new_x = x + radius * math.cos(angle)
            new_y = y + radius * math.sin(angle)

            positions.append((round(new_x, 2), round(new_y, 2)))

        return positions


# Example usage

object_location = (0, 0)

observer = SpatialObserver((15, 5))

print(observer.check_relationship(object_location))

print("Third perspective:",
      observer.third_perspective(object_location))

print("Loom movement:")
for position in observer.loom(object_location):
    print(position)

import math

def calculate_distance_and_bearing(point1, point2):
    """
    Calculate distance and bearing between two points.

    Args:
        point1 (tuple): (x1, y1)
        point2 (tuple): (x2, y2)

    Returns:
        tuple: (distance, bearing)
    """
    x1, y1 = point1
    x2, y2 = point2

    # Calculate changes in x and y
    dx = x2 - x1
    dy = y2 - y1

    # Calculate distance using Pythagorean theorem
    distance = math.sqrt(dx**2 + dy**2)

    # Calculate bearing using arctangent
    bearing = math.degrees(math.atan2(dy, dx))

    # Normalize bearing to [0, 360]
    if bearing < 0:
        bearing += 360

    return distance, bearing

# Example usage:
point1 = (3, 2)  # (x1, y1)
point2 = (4, 6)  # (x2, y2)

distance, bearing = calculate_distance_and_bearing(point1, point2)
print(f"Distance: {distance:.2f}")
print(f"Bearing: {bearing:.2f}°")




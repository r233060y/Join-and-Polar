import math

def calculate_distance(point1, point2):
    """
    Calculate distance between two points.

    Args:
        point1 (tuple): (x1, y1)
        point2 (tuple): (x2, y2)

    Returns:
        float: Distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2

    # Calculate changes in x and y
    dx = x2 - x1
    dy = y2 - y1

    # Calculate distance using Pythagorean theorem
    distance = math.sqrt(dx**2 + dy**2)

    return distance

def calculate_bearing(point1, point2):
    """
    Calculate bearing between two points.

    Args:
        point1 (tuple): (x1, y1)
        point2 (tuple): (x2, y2)

    Returns:
        float: Bearing between the two points in degrees.
    """
    x1, y1 = point1
    x2, y2 = point2

    # Calculate changes in x and y
    dx = x2 - x1
    dy = y2 - y1

    # Calculate bearing using arctangent
    bearing = math.degrees(math.atan2(dy, dx))

    # Normalize bearing to [0, 360]
    if bearing < 0:
        bearing += 360

    return bearing

def calculate_polar_coordinates(point1, distance, bearing):
    """
    Calculate polar coordinates (x2, y2) given point1, distance, and bearing.

    Args:
        point1 (tuple): (x1, y1)
        distance (float): Distance from point1
        bearing (float): Bearing from point1 in degrees

    Returns:
        tuple: (x2, y2)
    """
    x1, y1 = point1

    # Convert bearing to radians
    bearing_rad = math.radians(bearing)

    # Calculate x2 and y2 using polar coordinates formula
    x2 = x1 + distance * math.cos(bearing_rad)
    y2 = y1 + distance * math.sin(bearing_rad)

    return x2, y2

# Example usage:
point1 = (1, 2)  # (x1, y1)
point2 = (4, 6)  # (x2, y2)

distance = calculate_distance(point1, point2)
bearing = calculate_bearing(point1, point2)
polar_coordinates = calculate_polar_coordinates(point1, distance, bearing)

print(f"Distance: {distance:.2f}")
print(f"Bearing: {bearing:.2f}°")
print(f"Polar Coordinates: ({polar_coordinates[0]:.2f}, {polar_coordinates[1]:.2f})")


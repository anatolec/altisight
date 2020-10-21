from math import acos

earth_radius = 6371000  # Average earth radius in meters


def horizon_distance(altitude):
    alpha = acos(earth_radius / (earth_radius + altitude))
    distance = earth_radius * alpha
    return distance

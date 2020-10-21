from math import acos

earth_radius = 6371000  # Average earth radius in meters


def horizon_distance(altitude):
    """
    Returns the distance between an observer and the horizon he sees.
    Makes the assumption that earth is perfectly round
    :param altitude: Altitude of the observer, in meters
    :return: The distance between the observer and the horizon, in meters
    """

    alpha = acos(earth_radius / (earth_radius + altitude))
    distance = earth_radius * alpha
    return distance

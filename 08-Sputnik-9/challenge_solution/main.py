def calculate_descent(altitude):

    total_time = 0.0

    # Exosphere (700–10000 km)
    if altitude > 700:
        distance = (altitude - 700) * 1000
        total_time += distance / 2000
        altitude = 700

    # Thermosphere (85–700 km)
    if altitude > 85:
        distance = (altitude - 85) * 1000
        total_time += distance / 500
        altitude = 85

    # Mesosphere (50–85 km)
    if altitude > 50:
        distance = (altitude - 50) * 1000
        total_time += distance / 200
        altitude = 50

    # Stratosphere (12–50 km)
    if altitude > 12:
        distance = (altitude - 12) * 1000
        total_time += distance / 75
        altitude = 12

    # Troposphere (0–12 km)
    if altitude > 0:
        distance = altitude * 1000
        total_time += distance / 20

    return round(total_time, 1)

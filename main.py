from altisight import horizon_distance

if __name__ == '__main__':
    eye_altitude = 1.8
    print(f"From {eye_altitude} meters high, you can see {int(horizon_distance(eye_altitude))} meters away")

import numpy as np

class RaceEngine:
    def __init__(self, telemetry_data):
        self.telemetry_data = telemetry_data
        self.current_time = 0
        self.playback_speed = 1
        self.max_time = self._calculate_max_time()

    def _calculate_max_time(self):
        return max(data["time"][-1] for data in self.telemetry_data.values())

    def update(self, delta_time):
        self.current_time += delta_time * self.playback_speed
        if self.current_time > self.max_time:
            self.current_time = self.max_time

    def get_positions(self):
        positions = {}

        for driver, data in self.telemetry_data.items():
            times = data["time"]
            x = data["x"]
            y = data["y"]

            # interpolation
            xi = np.interp(self.current_time, times, x)
            yi = np.interp(self.current_time, times, y)

            positions[driver] = (xi, yi)

        return positions
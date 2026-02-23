class TelemetryProcessor:
    def __init__(self, session):
        self.session = session
        self.telemetry_data = {}

    def process(self):
        for driver in self.session.drivers:
            laps = self.session.laps.pick_drivers(driver)
            telemetry = laps.get_telemetry()

            telemetry = telemetry[['Time', 'X', 'Y']].dropna()
            telemetry['Time'] = telemetry['Time'].dt.total_seconds()

            self.telemetry_data[driver] = {
                "time": telemetry['Time'].values,
                "x": telemetry['X'].values,
                "y": telemetry['Y'].values
            }

        return self.telemetry_data
class TelemetryProcessor:
    def __init__(self, session):
        self.session = session
        self.drivers = session.drivers
        self.telemetry_data = {}

    def extract_driver_telemetry(self, driver):
        laps = self.session.laps.pick_drivers(driver)
        telemetry = laps.get_telemetry()
        return telemetry

    def filter_columns(self, telemetry):
        return telemetry[['Time', 'X', 'Y']]

    def clean_data(self, telemetry):
        return telemetry.dropna()

    def convert_time(self, telemetry):
        telemetry['Time'] = telemetry['Time'].dt.total_seconds()
        return telemetry

    def process(self):
        for driver in self.drivers:
            telemetry = self.extract_driver_telemetry(driver)
            telemetry = self.filter_columns(telemetry)
            telemetry = self.clean_data(telemetry)
            telemetry = self.convert_time(telemetry)

            self.telemetry_data[driver] = {
                "time": telemetry['Time'].tolist(),
                "x": telemetry['X'].tolist(),
                "y": telemetry['Y'].tolist()
            }

        return self.telemetry_data
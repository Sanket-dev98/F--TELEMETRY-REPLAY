from data.loader import SessionLoader

loader = SessionLoader(2024 , 1 , "R")
session = loader.load()
print(session.drivers)

driver = session.drivers[0]
print(driver)

laps = session.laps.pick_drivers(driver)
print(laps.head())

telemetry = laps.get_telemetry()
print(telemetry.head())
print(telemetry.columns)

print(session.drivers)
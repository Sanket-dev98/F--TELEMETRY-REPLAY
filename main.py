from data.loader import SessionLoader
from data.preprocessor import TelemetryProcessor
from engine.race_engine import RaceEngine
from render.arcade_renderer import ReplayWindow
import arcade

loader = SessionLoader(2024, 1, "R")
session = loader.load()

processor = TelemetryProcessor(session)
telemetry_data = processor.process()

engine = RaceEngine(telemetry_data)

window = ReplayWindow(engine)
arcade.run()
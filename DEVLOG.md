Day 1:
- Created project structure
- Setup virtual environment
- Installed dependencies
- Pushed initial commit

Observations:
- In day 1 all things are easy to setup and i only a felt when i update a requirements.txt it gets some error

Next Goal:
- Build SessionLoader (Data Layer)





Day 2 – SessionLoader Implementation

Objective:
Design and implement the data loading layer for the application.

Work Completed:
- Created SessionLoader class inside data/loader.py
- Added __init__ method to store year, round number, and session type
- Designed enable_cache() method (placeholder for now)
- Implemented load() method to:
    • Call enable_cache()
    • Fetch session using fastf1.get_session()
    • Load session data using session.load()
    • Store session in self.session
    • Return loaded session object
- Verified session loading from main.py

Observations:
- Understood that FastF1 requires explicit session.load() call
- Learned importance of storing session internally for reuse
- Clarified separation between preparation, loading, and returning data

Improvements Needed:
- Implement proper cache enabling logic
- Add error handling (try/except) for invalid year or round
- Follow Python naming conventions strictly (method names lowercase)

Next Goal (Day 3):
Extract driver telemetry data and design TelemetryProcessor module.





Day 3 – Telemetry Processing Layer

Objective:
Design and implement telemetry extraction and preprocessing pipeline.

Work Completed:
- Explored FastF1 session structure
- Retrieved drivers list and lap data
- Extracted telemetry for individual drivers
- Identified required telemetry columns (Time, X, Y)
- Designed TelemetryProcessor class
- Implemented telemetry extraction, filtering, and cleaning
- Converted Time column to numeric seconds
- Stored processed telemetry in structured dictionary
- Verified processor output from main.py

Observations:
- FastF1 telemetry is accessed through laps
- Raw telemetry contains NaN values requiring cleaning
- Time normalization is essential for simulation engines
- Dictionary structure simplifies future replay logic

Next Goal (Day 4):
Design RaceEngine to simulate time progression and driver movement.
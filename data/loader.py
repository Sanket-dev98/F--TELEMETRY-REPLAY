import fastf1
import os

class SessionLoader:
    def __init__(self, year, round_number, session_type):
        self.year = year
        self.round_number = round_number
        self.session_type = session_type
        self.session = None

    def enable_cache(self):
        cache_dir = os.path.join(os.getcwd(), "cache")
        fastf1.Cache.enable_cache(cache_dir)

    def load(self):
        self.enable_cache()
        session = fastf1.get_session(self.year, self.round_number, self.session_type)
        session.load()
        self.session = session
        return self.session
import fastf1

class SessionLoader:
    def __init__(self , year , round_number , session_type):
        self.year = year
        self.round_number = round_number
        self.session_type = session_type

    def enable_cache(self):
        pass

    def load(self):
        self.enable_cache()
        session = fastf1.get_session(self.year , self.round_number , self.session_type)
        session.load()
        self.session = session
        return self.session

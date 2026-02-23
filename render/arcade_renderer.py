import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
CAR_RADIUS = 4

class ReplayWindow(arcade.Window):
    def __init__(self, engine):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "F1 Replay")
        self.engine = engine
        self.paused = False

    def on_update(self, delta_time):
        if not self.paused:
            self.engine.update(delta_time)

    def on_draw(self):
        self.clear()

        positions = self.engine.get_positions()

        for driver, (x, y) in positions.items():
            sx = (x + 5000) / 10
            sy = (y + 5000) / 10
            arcade.draw_circle_filled(sx, sy, CAR_RADIUS, arcade.color.RED)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            self.paused = not self.paused
        if symbol == arcade.key.UP:
            self.engine.playback_speed *= 2
        if symbol == arcade.key.DOWN:
            self.engine.playback_speed /= 2
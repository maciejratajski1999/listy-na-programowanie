
class Timer:

    def __init__(self, bpm):
        self.bpm = bpm
        self.beat_duration = int(60000 / bpm)
        self.timer = 0
        self.tab_index = -1

    def __call__(self, pg_timer):
        self.timer += pg_timer

    def check(self):
        barrier = (self.tab_index + 1) * self.beat_duration
        return self.timer >= barrier

    def tab_index_up(self):
        self.tab_index += 1
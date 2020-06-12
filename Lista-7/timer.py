from time import time_ns
class Timer:

    def __init__(self, bpm):
        self.bpm = bpm
        self.beat_duration = 60000 / (bpm*2)
        self.timer = 0
        self.start = time_ns() // 1000000
        self.tab_index = -1

    def __call__(self):
        diff = time_ns() // 1000000
        self.timer = self.timer + (diff - self.start)
        self.start = diff

    def check(self):
        barrier = (self.tab_index + 1) * self.beat_duration
        return self.timer >= barrier

    def tab_index_up(self):
        self.tab_index += 1

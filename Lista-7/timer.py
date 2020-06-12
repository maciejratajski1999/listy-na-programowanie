from time import time
class Timer:

    def __init__(self, bpm):
        self.bpm = bpm
        self.beat_duration = 60000 / (bpm*2)
        self.timer = 0
        self.start = time()
        self.tab_index = -1

    def __call__(self):
        self.timer = self.timer + (time() - self.start)

    def check(self):
        if self.tab_index >0 :
            print(self.timer / self.tab_index)
        barrier = (self.tab_index + 1) * self.beat_duration
        return self.timer >= barrier

    def tab_index_up(self):
        self.tab_index += 1